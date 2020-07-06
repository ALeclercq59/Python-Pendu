# -*-coding:utf-8 -*
import os

import fonctions

import donnees

essaie = donnees.essaie

mot_alea = fonctions.mot_alea()

mot_ = fonctions.mot_alea_(mot_alea)


while 1:
    os.system("cls")
    mot = " ".join(mot_)
    print(mot)
    print("Nombres d'essaies restants :", essaie)
    lettre = input("Saisir une lettre : ")
    indice = fonctions.rechercher_lettre(lettre, mot_alea)
    
    
    if len(indice) == 0:
        essaie -= 1
        if essaie == 0:
            break
    else:
        mot_ = fonctions.remplacer(mot_, lettre, indice)
        
    
    verif1 = fonctions.verif(mot_alea, mot_)
    if verif1:
        break
    
if essaie == 0:
    print("\nVous avez perdu le mot était",mot_alea) 

if verif1 == True:
    os.system("cls")
    print(mot_alea)
    fonctions.ajouterScore(essaie)
    score = fonctions.score()
    print("Bravo, vous avez réussi à deviner le mot", mot_alea)
    print("Votre score est de", score, "points")

    
os.system("pause")