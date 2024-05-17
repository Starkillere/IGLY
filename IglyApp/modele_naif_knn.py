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

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def chargement_des_donnees() -> tuple:

    """
    """

        # Importation des données

    df_questions = pd.read_csv('IglyApp/data/q_divorce.csv', delimiter=';', encoding='utf-8')
    df_reponses = pd.read_csv('IglyApp/data/result_divorce.csv', delimiter=';', encoding='utf-8')

        # Renommer les colonnes du dataframe des réponses avec les entêtes des questions

    df_reponses.columns = df_questions['cle'].tolist() + ['Class']

        # Séparation des fonctionnalités

    X = df_reponses.iloc[:, :-1] # données réponses questions

    y = df_reponses['Class'] # Situation

        # Diviser les données en ensembles de formation et de test

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return (X_train, X_test, y_train, y_test)

class Situation:
    
    """

    """

    MARIER =  1
    DIVORCER = 0

class ModeleKNN:

    """

    """

    def __init__(self, k=5) -> None:
        self.__k = k
        self.__knn_model = KNeighborsClassifier(n_neighbors=k)
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = chargement_des_donnees()
        self.__y_pred = self.__entrainement()
    
    def __entrainement(self) :

        self.__knn_model.fit(self.__X_train, self.__y_train)
        y_pred = self.__knn_model.predict(self.__X_test)

        return y_pred
    
    def performances(self):

        accuracy = accuracy_score(self.__y_test, self.__y_pred)

        return accuracy
    
    def prediction(self, nouvel_utilisateur_reponses:list):

        assert type(nouvel_utilisateur_reponses) == list and [l for l in nouvel_utilisateur_reponses if type(l) == int] == nouvel_utilisateur_reponses

        situation_predite = self.__knn_model.predict([nouvel_utilisateur_reponses])[0]

        if situation_predite == Situation.DIVORCER:
            situation_predite = "DIVORCER"
        else:
            situation_predite =  "MARIER"

        return situation_predite