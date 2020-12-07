#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:29:43 2020

@author: chretien
"""
#header
#programme réalisant la partie graphique du jeu pendu
#réalisé le 07/12/2020
#Auteur: Paul Chrétien
#ToDo : réussir à appeler ma fonction jeu_ameliore pour afficher les nouvelles lettres petit à petit
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
    global record, photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8 
    record=8
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
        if score<record:
            record = score
            print("Nouveau record :",record)
        else:
            print("Dommage, le record était de", record, "mais vous avez fait", score)
    
    else:
        print("Perdu")
        
    return rejouer()



#fonction permettant d'afficher la premiere lettre du mot choisi au hasard ainsi que des underscore représentant les autres lettres de ce mot
#entrées:fichier texte contenant des mots de plus de 5 lettres
#sorties:mot avec la première lettre ainsi que des underscore représentant les autres lettres d'un mot choisi au hasard dans la liste créée à partir du fichier texte 
def affichage_debut_mot_2(fichier):
    global p 
    l=creation_liste(fichier)
    p=choix_mot_hasard(l)
    n=len(p)
    lettre.set(p[0]+(n-1)*" _")
    





from tkinter import *
#création de la fenetre principale
creation_fenetre = Tk()
creation_fenetre.title('Jeu du pendu')

#images de fond
photo1 = PhotoImage(file = 'bonhomme1.gif')
photo2 = PhotoImage(file = 'bonhomme2.gif')
photo3 = PhotoImage(file = 'bonhomme3.gif')
photo4 = PhotoImage(file = 'bonhomme4.gif')
photo5 = PhotoImage(file = 'bonhomme5.gif')
photo6 = PhotoImage(file = 'bonhomme6.gif')
photo7 = PhotoImage(file = 'bonhomme7.gif')
photo8 = PhotoImage(file = 'bonhomme8.gif')

#création de la zone graphique
largeur = 550
hauteur = 550
canevas = Canvas(creation_fenetre, width = largeur , height = hauteur)
item = canevas.create_image(150,150,anchor = NW, image = photo1)
print ("Image de fond (item",item,")")
canevas.pack()

lettre=StringVar()

#bouton qui propose à l'utilisateur de rentrer une lettre dans la zone de texte dédiée à cela
bouton_proposer = Button(creation_fenetre, text="proposer", command=affichage_debut_mot_2("mots"))
bouton_proposer.pack(side = LEFT, padx = 10, pady = 10)

#bouton qui propose à l'utilisateur de quitter la fenetre
bouton_quit = Button(creation_fenetre, text="quitter", command=creation_fenetre.destroy)
bouton_quit.pack(side = LEFT, padx = 10, pady = 10)

texte_label=Label(creation_fenetre, textvariable=lettre)
texte_label.pack()

creation_fenetre.mainloop()






