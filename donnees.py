# -*-coding:utf-8 -*


liste_mots = ["voiture", "avion", "homme", "femme", "airpods", "feuille", "stylo", "ciseaux"]

essaie = 8


try:
    fichier = open("score.txt", "r")
    score = int(fichier.read())
    fichier.close()
except:
    fichier = open("score.txt", "w")
    fichier.close()
    score = 0