"""
    IGLY (Iel gonna let you) 
    modele : Naif_KNN
    langage : python3
    createur : AYOUBA Anrezki
    initalisation : 14/05/2024 11h14 (en cours d'informatique au lycée clémenceau Nantes 44)
    MAJ : 14/05/2024
    Dépots : https://github.com/Starkillere/IGLY
"""

__all__ =  ["ModeleKNN"]

# Importation

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


def chargement_des_donnees() -> tuple:

    """
    """

        # Importation des données

    base_path = os.path.dirname(__file__)
    df_questions = pd.read_csv(os.path.join(base_path, 'data/q_divorce.csv'), delimiter=';', encoding='utf-8')
    df_reponses = pd.read_csv(os.path.join(base_path, 'data/result_divorce.csv'), delimiter=';', encoding='utf-8')

        # Renommer les colonnes du dataframe des réponses avec les entêtes des questions

    df_reponses.columns = df_questions['cle'].tolist() + ['Class']

        # Séparation des fonctionnalités

    X = df_reponses.iloc[:, :-1] # données réponses questions

    y = df_reponses['Class'] # Situation

        # Diviser les données en ensembles de formation et de test

    return (X, y)

class Situation:
    
    """

    """

    MARIER =  1
    DIVORCER = 0

class ModeleBayesien:

    """

    """

    def __init__(self) -> None:
        self.__g_model = GaussianNB()
        self.__X, self.__y = chargement_des_donnees()
        self.__entrainement()

    def __entrainement(self) :
        self.__g_model.fit(self.__X, self.__y)
    
    def prediction(self, nouvel_utilisateur_reponses:list):

        assert type(nouvel_utilisateur_reponses[0]) == list and [l for l in nouvel_utilisateur_reponses [0] if type(l) == int] == nouvel_utilisateur_reponses[0]

        probabilites = self.__g_model.predict_proba(nouvel_utilisateur_reponses)[0]
        classes =self.__g_model.classes_
        resultat = {classes[i]: round(probabilites[i],2) for i in range(len(classes))}
        t_result = {}

        for k in resultat.keys():
            if k == Situation.MARIER:
                t_result["MARIER"] = resultat[k]*100
            else:
                t_result["DIVORCER"] = resultat[k]*100

        return t_result
    
    def clas_prediction(self, nouvel_utilisateur_reponses:list):
        assert type(nouvel_utilisateur_reponses[0]) == list and [l for l in nouvel_utilisateur_reponses [0] if type(l) == int] == nouvel_utilisateur_reponses[0]
        situation_predite = self.__g_model.predict(nouvel_utilisateur_reponses)[0]
         
        if situation_predite == Situation.DIVORCER:
            situation_predite = "DIVORCE"
        else:
            situation_predite =  "MARIAGE"

        return situation_predite
