"""
Computational Model of Post-Dissemination Metastatic Cascade
with Absorbent Intermediary Compartment

Discrete-time stochastic agent-based simulation.
Speculative modeling only; no clinical claims.

Author: Caitlyn C. Randels
November 2026
"""

import random
import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Cell:
    state: str = "circulating"  # circulating, dormant, sponge, overt, cleared
    organ: str = None
    microenv_fit: float = 0.5
    age: int = 0

@dataclass
class SpongeCompartment:
    capacity: float = 50.0
    permeability: float = 0.1
    membrane_gate: float = 0.5
    hard_cap: float = 100.0
    contents: List[Cell] = field(default_factory=list)
    
    def fill_level(self) -> float:
        return len(self.contents) / self.capacity if self.capacity > 0 else 0.0
    
    def can_accept(self) -> bool:
        return len(self.contents) < self.hard_cap
    
    def absorb(self, cell: Cell) -> bool:
        if self.can_accept() and random.random() < self.membrane_gate:
            cell.state = "sponge"
            self.contents.append(cell)
            return True
        return False
    
    def release(self) -> List[Cell]:
        released = []
        remaining = []
        for cell in self.contents:
            if random.random() < self.permeability:
                cell.state = "dormant"
                released.append(cell)
            else:
                remaining.append(cell)
        self.contents = remaining
        return released

class MetastaticCascadeModel:
    def __init__(self, config: Dict, sponge_enabled: bool = False, seed: int = None):
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        self.config = config
        self.sponge_enabled = sponge_enabled
        self.sponge = SpongeCompartment(
            capacity=config.get("sponge_capacity", 50.0),
            permeability=config.get("sponge_permeability", 0.1),
            membrane_gate=config.get("sponge_membrane", 0.5),
            hard_cap=config.get("sponge_hard_cap", 100.0)
        )
        self.cells: List[Cell] = []
        self.month = 0
        self.overt_colonies = 0
        self.dormant_count = 0
        
    def shed_cells(self, n: int):
        for _ in range(n):
            cell = Cell(
                microenv_fit=random.uniform(0.3, 0.9),
                organ=self._choose_organ()
            )
            self.cells.append(cell)
    
    def _choose_organ(self) -> str:
        organs = self.config.get("organs", {"bone": 0.4, "lung": 0.3, "liver": 0.3})
        return random.choices(list(organs.keys()), weights=list(organs.values()))[0]
    
    def step(self):
        self.month += 1
        # Shedding with inter-patient heterogeneity
        base_shed = self.config.get("shed_rate", 2.0)
        hetero = self.config.get("shed_heterogeneity", 0.3)
        n_shed = max(0, int(np.random.normal(base_shed, base_shed * hetero)))
        self.shed_cells(n_shed)
        
        new_cells = []
        for cell in self.cells:
            cell.age += 1
            if cell.state == "circulating":
                # Circulating clearance
                if random.random() < self.config.get("circ_clearance", 0.7):
                    cell.state = "cleared"
                    continue
                # Attempt establishment or sponge absorption
                if self.sponge_enabled and self.sponge.absorb(cell):
                    continue
                # Establishment
                est_thresh = self.config.get("establishment_threshold", 0.65)
                if random.random() < cell.microenv_fit and random.random() > est_thresh:
                    cell.state = "dormant"
                else:
                    if random.random() < 0.3:
                        cell.state = "cleared"
            elif cell.state == "dormant":
                # Dormant clearance or reawakening
                if random.random() < self.config.get("dormant_clearance", 0.02):
                    cell.state = "cleared"
                    continue
                if random.random() < self.config.get("reawaken_rate", 0.01):
                    if random.random() < cell.microenv_fit * self.config.get("colonization_prob", 0.1):
                        cell.state = "overt"
                        self.overt_colonies += 1
                    # else remain dormant
            elif cell.state == "sponge":
                pass  # handled by sponge.release()
            
            if cell.state not in ("cleared",):
                new_cells.append(cell)
        
        # Sponge release
        if self.sponge_enabled:
            released = self.sponge.release()
            new_cells.extend(released)
        
        self.cells = new_cells
        self.dormant_count = sum(1 for c in self.cells if c.state in ("dormant", "sponge"))
    
    def run(self, months: int = 120) -> Dict:
        for _ in range(months):
            self.step()
        return {
            "month": self.month,
            "overt_colonies": self.overt_colonies,
            "dormant_or_sponge": self.dormant_count,
            "full_elimination": self.overt_colonies == 0 and self.dormant_count == 0,
            "sponge_fill": self.sponge.fill_level() if self.sponge_enabled else 0.0
        }

def run_comparison(n_runs: int = 2000, seed_base: int = 42):
    """Run matched sponge-on vs sponge-off comparison."""
    configs = {
        "prostate": {"organs": {"bone": 0.85, "lung": 0.1, "liver": 0.05}, "establishment_threshold": 0.65},
        "er_breast": {"organs": {"bone": 0.70, "lung": 0.2, "liver": 0.1}, "establishment_threshold": 0.65},
        "lung": {"organs": {"lung": 0.60, "bone": 0.2, "liver": 0.2}, "establishment_threshold": 0.65},
        "melanoma": {"organs": {"lung": 0.55, "brain": 0.25, "liver": 0.2}, "establishment_threshold": 0.65},
        "colorectal": {"organs": {"liver": 0.75, "lung": 0.15, "bone": 0.1}, "establishment_threshold": 0.65},
    }
    
    results = {}
    for name, cfg in configs.items():
        on_elim = off_elim = on_overt = off_overt = 0
        for i in range(n_runs):
            seed = seed_base + i
            m_off = MetastaticCascadeModel(cfg, sponge_enabled=False, seed=seed)
            r_off = m_off.run()
            m_on = MetastaticCascadeModel(cfg, sponge_enabled=True, seed=seed)
            r_on = m_on.run()
            off_elim += r_off["full_elimination"]
            on_elim += r_on["full_elimination"]
            off_overt += r_off["overt_colonies"] > 0
            on_overt += r_on["overt_colonies"] > 0
        results[name] = {
            "off_elimination": off_elim / n_runs,
            "on_elimination": on_elim / n_runs,
            "off_overt_fraction": off_overt / n_runs,
            "on_overt_fraction": on_overt / n_runs,
        }
    return results

if __name__ == "__main__":
    print("Running matched sponge on/off comparison (demo scale)...")
    res = run_comparison(n_runs=100)  # reduced for quick demo
    for k, v in res.items():
        print(f"{k}: off_elim={v['off_elimination']:.3f}, on_elim={v['on_elimination']:.3f}")
