"""
    IGLY (Iel gonna let you) 
    modele : Naif_KNN
    langage : python3
    createur : AYOUBA Anrezki
    initalisation : 14/05/2024 11h14 (en cous d'informatique au lycée clémenceau Nantes 44)
    MAJ : 14/05/2024
    Dépots : https://github.com/Starkillere/IGLY
"""

# Importation

from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
from . import modele_naif_knn
from datetime import timedelta

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]
app.permanent_session_lifetime = timedelta(days=5)
my_ai = modele_naif_knn.ModeleKNN()
df_questions = pd.read_csv('IglyApp//data/q_divorce.csv', delimiter=';', encoding='utf-8')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        reponses_utilisateur = []
        for i in range(1, 55):
            reponse = int(request.form[f'reponse_{i}'])
            reponses_utilisateur.append(reponse)
        
        situation_predite = my_ai.prediction(reponses_utilisateur)
        
        return render_template('resultat.html', situation_predite=situation_predite)
    
    return render_template('questionnaire.html', questions=df_questions['Q'].tolist())