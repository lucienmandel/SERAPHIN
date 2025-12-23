ENGLISH BELOW

### Comment lancer les simulations 

Le repo contient deux versions :

**seraphin_core.py** : version pédagogique (simple, claire)
**seraphin_ultimate.py** : version avancée (épigénétique, consensus, quantum, etc.)

**Prérequis** (une seule fois dans Terminal) :


```bash
pip3 install numpy matplotlib qiskit  # Pour visualisation + quantum simulé (optionnel)

Lancer la version CORE (pédagogique) :
Bash
python seraphin_core.py --simulate


Lancer la version ULTIMATE (recherche) :
Bash
python seraphin_ultimate.py --simulate

ULTIMATE avec mode quantum forcé (simulation boostée) :
Bash
python seraphin_ultimate.py --simulate --quantum-force

Options supplémentaires :

--pulses 2000 : plus de pulses (ex: 2000 au lieu de 1000)
--depth 18 : profondeur récursive plus grande

Chaque lancement génère :

Une simulation en direct dans le terminal
Un fichier PNG dans le dossier visualizations/ (Julia set tentaculaire représentant l’hydre)

Aucun déploiement réel, aucune blockchain – tout est simulé et éducatif.
text### Version anglaise (si tu veux un repo bilingue)



How to run the simulations

The repo contains two versions:

seraphin_core.py: educational version (simple, clear)
seraphin_ultimate.py: advanced research version (epigenetics, consensus, quantum, etc.)

Requirements (run once in Terminal):

Bash
pip3 install numpy matplotlib qiskit  # For visualization + quantum simulation (optional)

Run the CORE version (educational):
Bash
python seraphin_core.py --simulate

Run the ULTIMATE version (research):
Bash
python seraphin_ultimate.py --simulate

ULTIMATE with quantum-forced mode (boosted simulation):
Bash
python seraphin_ultimate.py --simulate --quantum-force

Additional options:

--pulses 2000: more pulses (e.g. 2000 instead of 1000)
--depth 18: greater recursion depth

Each run generates:

Live simulation in the terminal
A PNG file in the visualizations/ folder (Julia set representing the tentacular hydra)

No real deployment, no blockchain – everything is simulated and educational.
