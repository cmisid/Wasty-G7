# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 07:29:53 2017

@author: Valentin
"""


import psycopg2
import sys
import numpy
import math
from numpy.random import randn
import random
from random import *
import xlrd
from xlwt import Workbook, Formula
import json

#Listes des modalités pour les variables
sex=["M","W"]
age=range(15,100)
csp=["agriculteur","artisans, comm, Cent.","cadres et prof. Intellectuels","prof intermediaire","employes","ouvriers","retraites","chomage","student","others"]
centre_interet=["","sport","theatre","cinema","travel","music","jeux-videos","informatique","recyclage","jardinage","animals","photographie","lecture","painting","decoration interieure","peche","camping","mode","chasse","automobile","cook","other"]
quartier=["CAPITOLE","SAINT-GEORGES","JUNCASSE - ARGOULETS","GRAMONT","LA TERRASSE","ZONES D'ACTIVITES SUD","FONTAINE-LESTANG","PONT-DES-DEMOISELLES","PATTE D'OIE","LE BUSCA","CROIX-DE-PIERRE","REYNERIE","MATABIAU","FAOURETTE","SAINT-ETIENNE","SAINT-SIMON","LES IZARDS","SAINT-MARTIN-DU-TOUCH","LES CHALETS","LARDENNE","ARENES","AMIDONNIERS","MIRAIL-UNIVERSITE","LES PRADETTES","COMPANS","GINESTOUS","SAINT-MICHEL","FER-A-CHEVAL","BELLEFONTAINE","SOUPETARD","PAPUS","POUVOURVILLE","BASSO-CAMBO","ARNAUD BERNARD","SAINT-AUBIN - DUPUY","JULES JULIEN","CROIX-DAURADE","CASSELARDIT","MINIMES","RAMIER","LA CEPIERE","EMPALOT","LALANDE","RANGUEIL - CHR - FACULTES","CARMES","LA FOURGUETTE","BARRIERE-DE-PARIS","MONTAUDRAN - LESPINET","SAINT-AGNE","PURPAN","SAUZELONG - RANGUEIL","SAINT-CYPRIEN","BAGATELLE","GUILHEMERY","MARENGO - JOLIMONT","COTE PAVEE","CHATEAU-DE-L'HERS","ROSERAIE","BONNEFOY","SEPT DENIERS"]              

#Tirage aléatoire des modalités pour chaque variable et génération d'un individu
def generation(n):
    data=[] 
    z = {}                                                   
    for i in range(n):
            centre_interet=["","sport","theatre","cinema","voyage","musique","jeux-videos","informatique","recyclage","jardinage","animaux","photographie","lecture","peinture","decoration interieure","peche","camping","mode","chasse","automobile","cuisine","autres"]
            S=choice(sex)
            A=choice(age)
            Q=choice(quartier)
            CSP=choice(csp)
            CI1=choice(centre_interet)
            centre_interet.remove(CI1)
            CI2=choice(centre_interet)
            centre_interet.remove(CI2)
            CI3=choice(centre_interet)
            if CI1=="":   
               CI2=CI1=CI3 
            if CI2=="":
                CI3=CI2
            
            z = {"id_U":i,"age":A,"sex":S,"CSP":CSP,"interest1":CI1,"interest2":CI2,"interest3":CI3,"quartier":Q}
            data.append(z)
    return data


data = generation(1000)

#Conversion en fichier JSON
 
jsonData=json.dumps(data)
print(jsonData)
with open ('C:/Users/Valentin/Documents/projet poub py/Users.json','w')as f:
    json.dump(jsonData,f)

#Alimentation dans un fichier EXCEL

#Création des champs
book = Workbook()
users = book.add_sheet('users')
users.write(0,0,"id_U")
users.write(0,1,"quartier")
users.write(0,2,"age")
users.write(0,3,"sex")
users.write(0,4,"interets1")
users.write(0,5,"interest2")
users.write(0,6,"interest3")
users.write(0,7,"CSP")

#Alimentation des champs via les valeurs du dictionnaire

for i in range(1,len(data)):
        users.write(i,0,data[i]["id_U"])
        users.write(i,1,data[i]["quartier"])
        users.write(i,2,data[i]["age"])
        users.write(i,3,data[i]["sex"])
        users.write(i,4,data[i]["interest1"])
        users.write(i,5,data[i]["interest2"])
        users.write(i,6,data[i]["interest3"])
        users.write(i,7,data[i]["CSP"]) 
book.save('C:/Users/Valentin/Documents/projet poub py/tt_users3.xls')#Enregistrement fichier EXCEL




