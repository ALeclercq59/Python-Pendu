import donnees

import random

import os

def mot_alea ():
    liste_mots = donnees.liste_mots
    indice_mot_alea = random.randrange(9)
    
    return liste_mots[indice_mot_alea]


def mot_alea_(mot_alea):
    mot_ = []
    for lettre in mot_alea:
        mot_.append("*")
    return mot_
    

def rechercher_lettre(lettre, mot_alea):
    mot_alea1 = []
    indice_lettre = []
    for lettre1 in mot_alea:
        mot_alea1.append(lettre1)
    for i, elt in enumerate(mot_alea1):
        if lettre == elt:
            indice_lettre.append(i)
    
    return indice_lettre

    
def remplacer(mot_alea, lettre, indice):
    mot_alea1 = list(mot_alea)
    for indice1 in indice:
        mot_alea1[indice1] = lettre
    
    return mot_alea1


def verif(mot_alea, mot_cacher):
    if " ".join(mot_alea) == " ".join(mot_cacher):
        return True
    else:
        return False

    
def ajouterScore(scoreJoueur):
    score = donnees.score
    score += scoreJoueur
    
    with open ("score.txt", "w") as fichier:
        fichier.write(str(score))

        
def score():
    with open("score.txt", "r") as fichier:
        score = fichier.read()
    
    return score


