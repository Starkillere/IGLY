"""
    IGLY (Iel gonna let you) 
    langage : python3
    createur : AYOUBA Anrezki
    initalisation : 14/05/2024 11h14 (en cousr d'informatique au lycée clémenceau Nantes 44)
    MAJ : 14/05/2024
    Dépots : https://github.com/Starkillere/IGLY
"""

# Importation

#!/usr/bin/env python

import sys
import subprocess

# Chemin vers votre environnement virtuel
venv_path = '/home/your_username/venv/bin/activate'

# Activer l'environnement virtuel
activate_this = venv_path
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})


from IglyApp import app

if __name__ == "__main__":
    app.run()