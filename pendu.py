#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:16:06 2020

@author: chretien
"""
#header
#programme réalisant le jeu "pendu"
#réalisé le 30/11/2020
#Auteur: Paul Chrétien, lien GITHub: https://github.com/paulchretien/TP_pendu
import random as rd



#fonction permettant de créer une liste des mots triés par longueur et par ordre alphabétique
 #entrées:fichier texte contenant des mots de plus de 5 lettres
#sorties:liste des mots du fichier texte qui sont dans triés par longueur et par ordre alphabétique
def creation_liste(fichier):
    fich = open(fichier+'.txt','r')
    l = []
    for mot in fich:
        l += [mot]
    fich.close()
    return l




#fonction permettant de choisir un mot au hasard parmi la liste de mots
#entrées:liste de mots de plus de 5 lettres
#sorties:un mot, type string, choisi au hasard dans la liste donnée en entrée 
def choix_mot_hasard(l):
    return(rd.choice(l))




#fonction permettant d'afficher la premiere lettre du mot choisi au hasard ainsi que des underscore représentant les autres lettres de ce mot
#entrées:fichier texte contenant des mots de plus de 5 lettres
#sorties:liste contenant la première lettre ainsi que des underscore représentant les autres lettres d'un mot choisi au hasard dans la liste créée à partir du fichier texte 
def affichage_debut_mot(fichier):
    global p
    l = creation_liste(fichier)
    p = choix_mot_hasard(l)
    ln = len(p)
    j = p[0] + (ln - 1) * '_'
    return list(j)




#fonction laissant 8 chances au joueur pour trouver le mot mystère et affichant petit à petit dans le mot mystère les lettres qu'il a trouvé
#entrées:fichier texte contenant des mots de plus de 5 lettres
#sorties: retourne "vous avez perdu" si les 8 tentatives sont fausses et renvoie le mot dans une liste si le joueur a trouvé toutes les lettres
def jeu(fichier):
    k = 7
    j = affichage_debut_mot(fichier)
    m = len(j)-2 #pour ne pas prendre en compte l'espace et le /n du saut de ligne présents dans le fichier texte
    v = j[:m] 
    b = list(p)
    q = b[:len(b)-2] #pour enlever l'espace et le /n du saut de ligne présents dans le fichier texte
  
    while k >= 0: 
        
        if m <= 1: 
            break
        l = input("Choisir une lettre:")
        
        if l not in q and m != 0:
            print("Erreur, plus que",k," chances restantes")
            k -= 1
        
        elif l in q and m > 1:
            x = [indice for indice, valeur in enumerate(q) if valeur == l]
            if l not in v:
                m -= len(x)
            for i in x:
                v[i] = l
            print(v)
            print("Bonne lettre")
    
    if m <= 1:
        print("Vous avez trouvé le mot mystère")
    else:
        print("Perdu")



        
#fonction permettant de demander a un joueur s'il veut recommencer une partie, et si oui, démarre une partie
#entrée: aucune, mais mot écrit par le joueur une fois la fonction appellée
#sortie: du texte indiquant "tant pis" ou un message d'erreur, ou bien appel de la fonction jeu_ameliore("mots") si le joueur le veut
def rejouer():
    a = input("Voulez-vous rejouer ?:")
    if a == "oui":
        return jeu_ameliore("mots")
    if a == "non":
        print("Tant pis")
    else:
        print("Je ne comprends pas votre réponse, tapez oui on non en minuscule")
        return rejouer()
 



       
#même fonction que jeu(fichier) mais précise au joueur s’il donne une lettre déjà donnée auparavant, propose au joueur de rejouer en fin de partie et retient le meilleur score des parties déjà jouées
#entrées:fichier texte contenant des mots de plus de 5 lettres
#sorties: retourne "vous avez perdu" si les 8 tentatives sont fausses et renvoie le mot dans une liste si le joueur a trouvé toutes les lettres, renvoie une fontion proposant de rejouer 
def jeu_ameliore(fichier):
    global record
    k = 7
    j = affichage_debut_mot(fichier)
    m = len(j)-2 #pour ne pas prendre en compte l'espace et le /n du saut de ligne présents dans le fichier texte
    v = j[:m] 
    b = list(p)
    q = b[:len(b)-2] #pour enlever l'espace et le /n du saut de ligne présents dans le fichier texte
    score = 0
    
    while k >= 0: 
        
        if m <= 1: 
            break
        l = input("Choisir une lettre:")
        
        if l not in q and m != 0:
            print("Erreur, plus que",k," chances restantes")
            k -= 1
            score += 1
        
        elif l in q and m > 1:
            x = [indice for indice, valeur in enumerate(q) if valeur == l]
            if l in v:
                print("Vous avez déjà choisi ce mot !")
            if l not in v:
                m -= len(x)
            for i in x:
                v[i] = l
            print(v)
            print("Bonne lettre")
    
    if m <= 1:
        print("Vous avez trouvé le mot mystère")
        if record == None:
            record = score
            print("Nouveau record :",record)
        if score<record:
            record = score
            print("Nouveau record :",record)
        else:
            print("Dommage, le record était de", record, "mais vous avez fait", score)
    
    else:
        print("Perdu")
        
    return rejouer()
        


    
    
    


