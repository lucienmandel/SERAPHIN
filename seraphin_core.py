"""
SÉRAPHIN ∞ – Core Version (Educational)
Author: Lucien Mandel
Date: December 2025
License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

Core version: minimal implementation to understand fractal recursion,
emergence, and energy-constrained growth.
Every instance is a complete hydra – head = tentacle.
"""

import os
import random
import time
import asyncio
import argparse
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

class HydraCore:
    """
    Simple recursive class: every hydra is complete.
    No central hierarchy – pure fractal self-similarity.
    """
    def __init__(self, depth=0, max_depth=12, energy=100, memory=None):
        self.depth = depth
        self.max_depth = max_depth
        self.energy = min(100, energy)
        self.memory = memory or {
            'profits': [], 'clones': [], 'max_depth_reached': 0, 'energy_log': []
        }
        self.sub_hydras = []  # Tentacles / sub-hydras

    def spawn_sub(self):
        """Spawn a sub-hydra if energy allows."""
        if self.energy > 30 and self.depth < self.max_depth:
            child = HydraCore(
                depth=self.depth + 1,
                max_depth=self.max_depth,
                energy=self.energy - 30,  # Spawning cost
                memory=self.memory
            )
            self.sub_hydras.append(child)
            self.memory['clones'].append(self.depth + 1)
            self.memory['max_depth_reached'] = max(
                self.memory.get('max_depth_reached', 0),
                child.depth
            )
            return child
        return None

    def run_once(self):
        """Execute one pulse: gain + possible recursive spawn."""
        profit = round(random.uniform(500, 6000), 2)
        self.memory['profits'].append(profit)

        # Spawn chance (increases with energy)
        if random.random() < (self.energy / 100) * 0.5:
            for _ in range(random.randint(1, 3)):
                sub = self.spawn_sub()
                if sub:
                    sub.run_once()

        # Energy regeneration (slower if spawning active)
        regen = random.randint(10, 25) if not self.sub_hydras else random.randint(5, 15)
        self.energy = min(100, self.energy + regen)
        self.memory['energy_log'].append(self.energy)

        return f"[Depth {self.depth}] +{profit:.2f} USDC | Energy: {self.energy}% | Clones: {len(self.memory['clones'])}"

# ==================== JULIA VISUALIZATION ====================

def generate_julia_visualization(memory):
    """Generate a Julia set visualization symbolizing the fractal hydra."""
    def julia_set(h=1000, w=1000, maxit=300, c=-0.7 + 0.27015j):
        y, x = np.ogrid[-1.5:1.5:h*1j, -2:1:w*1j]
        z = x + y*1j
        divtime = maxit + np.zeros(z.shape, dtype=int)
        for i in range(maxit):
            z = z**2 + c
            diverge = abs(z) > 2
            div_now = diverge & (divtime == maxit)
            divtime[div_now] = i
            z[diverge] = 2
        return divtime

    plt.figure(figsize=(12, 9), facecolor='black')
    plt.imshow(julia_set(), cmap='plasma', extent=[-2, 1, -1.5, 1.5])
    plt.title(
        f'SÉRAPHIN ∞ – Julia Set Visualization (Core)\n'
        f'Clones: {len(memory.get("clones", []))} | Profits: {sum(memory.get("profits", [0])):,.0f} USDC\n'
        f'Max Depth: {memory.get("max_depth_reached", 0)}',
        color='white', fontsize=14
    )
    plt.axis('off')

    os.makedirs("visualizations", exist_ok=True)
    filename = f"visualizations/julia_core_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(filename, bbox_inches='tight', dpi=300, facecolor='black')
    plt.close()

    print(f"\nJulia set visualization generated: {filename}")
    print("Open the PNG to see the infinite tentacular structure of the hydra.")

# ==================== SIMULATION ====================

async def simulate_core(pulses=500, max_depth=12):
    print("\n" + "="*70)
    print("SÉRAPHIN ∞ – Core Simulation (Educational)")
    print("Every tentacle is a head. Every head is a complete hydra.")
    print("="*70 + "\n")

    root_hydra = HydraCore(depth=0, max_depth=max_depth, energy=100)

    for pulse in range(1, pulses + 1):
        print(f"Pulse {pulse:3d} | {root_hydra.run_once()}")

        if pulse % 100 == 0:
            await asyncio.sleep(0.05)

    # Final dashboard
    print("\n" + "="*70)
    print("FINAL DASHBOARD – CORE")
    print("="*70)

    total_profit = sum(root_hydra.memory.get('profits', []))
    print(f"Total Simulated Profit     : {total_profit:,.2f} USDC")
    print(f"Clones Spawned             : {len(root_hydra.memory['clones'])}")
    print(f"Max Depth Reached          : {root_hydra.memory.get('max_depth_reached', 0)}")
    print(f"Final Energy Level         : {root_hydra.energy}%")

    generate_julia_visualization(root_hydra.memory)

    print("\nThe CORE hydra lives – simple, fractal, emergent.")
    print("SÉRAPHIN ∞ – Educational open-source project by Lucien Mandel")
    print("="*70)

# ==================== MAIN ====================

def main():
    parser = argparse.ArgumentParser(description="SÉRAPHIN ∞ Core – Educational Version")
    parser.add_argument('--simulate', action='store_true', help="Run the CORE simulation")
    parser.add_argument('--pulses', type=int, default=500, help="Number of pulses")
    parser.add_argument('--depth', type=int, default=12, help="Maximum recursion depth")
    args = parser.parse_args()

    project_dir = "seraphin-infinite"
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
    os.chdir(project_dir)

    os.makedirs("visualizations", exist_ok=True)

    with open("seraphin_core.py", "w") as f:
        f.write(__doc__ + "\n" + open(__file__, 'r', encoding='utf-8').read())

    print("SÉRAPHIN ∞ Core bootstrap completed.")
    print("Ready for GitHub.")
    print("Author: Lucien Mandel")

    if args.simulate:
        asyncio.run(simulate_core(pulses=args.pulses, max_depth=args.depth))

if __name__ == "__main__":
    main()
