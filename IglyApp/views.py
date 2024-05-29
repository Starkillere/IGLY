"""
    IGLY (Iel gonna let you) 
    modele : Naif_KNN
    langage : python3
    createur : AYOUBA Anrezki
    initalisation : 14/05/2024 11h14 (en cours d'informatique au lycée clémenceau Nantes 44)
    MAJ : 14/05/2024
    Dépots : https://github.com/Starkillere/IGLY
"""

# Importation

from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
from . import modele_naif_knn, approche_bayesien
from datetime import timedelta

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]
app.permanent_session_lifetime = timedelta(days=5)
my_ai = modele_naif_knn.ModeleKNN()
my_bayes = approche_bayesien.ModeleBayesien()
df_questions = pd.read_csv('IglyApp//data/q_divorce.csv', delimiter=';', encoding='utf-8')
position_des_questions_non_compatible = [6, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 43, 46, 48, 49, 51, 52]


@app.route('/', methods=['GET', 'POST'])
def home():

    def correcteur(x:int) -> int:
        l =  [0,1,2,3,4]
        pos =  l.index(x)
        return l[-pos-1]


    if request.method == 'POST':
        reponses_utilisateur = []
        for i in range(1, 55):
            reponse = int(request.form[f'reponse_{i}'])
            if i+1 in position_des_questions_non_compatible:
                reponse = correcteur(reponse)
            reponses_utilisateur.append(reponse)
        
        #situation_predite = my_ai.prediction(reponses_utilisateur)
        situation_predite = my_bayes.clas_prediction([reponses_utilisateur])
        situation_predite2 = my_bayes.prediction([reponses_utilisateur])
        
        return render_template('resultat.html', situation_predite_f=situation_predite, situation_predite_b=situation_predite2)
    
    return render_template('questionnaire.html', questions=df_questions['Q'].tolist())
