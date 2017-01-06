# Groupe 7 Génération des données 

# Importation des modules

import random
from random import *
import xlrd
from xlwt import Workbook, Formula
import json
from random import randrange
from datetime import date, datetime, timedelta
import pandas as pd

# Generation d'une liste dans laquelle il y a toutes les dates du 1 octobre 
# 2016 à dans 30 jours à compter d'aujourd'hui.
# Pour prendre en compte la condition des 30 jours d'une annonce en ligne.


# "Since" correspond à la date : 1er octobre 2016 qui est la date de départ 
# pour les générations de date
since = datetime(year=2016, month=10, day=1)

# "Until" correspond à la date d'aujourd'hui + 30 jours pour prendre en compte 
# les délais de mise en ligne des annonces 
until = datetime.now() + timedelta(days=30)

# Création de la variable date_range sous forme de liste 
# vide à l'initialisation
date_range = []

# Création des dates et des heures de manière aléatoire
# draft_date_list : ébauche de la liste contenant les dates
# nécessaire pour la création de la liste finale
draft_date_list = pd.date_range(since,until,freq='12H')
# Transformation de la liste des dates en liste de caractère
# nécessaire pour lancer Jyson.
date_list = pd.Series(draft_date_list.format())
    
# Entrée : N, un entier tq la valeur correspond à un tirage d'échantillon.
# Objectif de la fonction : Générer des données de la table recovery
# de manière aléatoire.
# Sortie : Données aléatoires de la table recovery/récupération. 

def recovery(N):
	data = [] 
	z = {}                                                  
	for i in range(N):
		dl = choice(date_list)
		z = {'id_recovery' : i, 'recovery_date' : dl, 'id_advert' : i, 'recovery_user' : i}
		data.append(z)
	return data

# Génération des 50 données aléatoires
random_data = recovery(50)

# Création un fichier Recovery/Récupération en JSON
jsonData = json.dumps(random_data)
print(jsonData)
with open ('C:/Users/Claire/Desktop/Recovery.json','w') as f:
	json.dump(jsonData,f)
    
# Création d'un fichier Recovery.xls
book = Workbook()
table_recovery = book.add_sheet('recovery')
table_recovery.write(0,0,"id_recovery")
table_recovery.write(0,1,"recovery_date")
table_recovery.write(0,2,"id_advert")
table_recovery.write(0,3,"recovery_user")

for i in range(1,len(random_data)):
        table_recovery.write(i,0,random_data[i]["id_recovery"])
        table_recovery.write(i,1,random_data[i]["recovery_date"])
        table_recovery.write(i,2,random_data[i]["id_advert"])
        table_recovery.write(i,3,random_data[i]["recovery_user"])   

# Créer un fichier csv
pd.DataFrame(random_data)
pd.DataFrame(random_data).to_csv('Recovery.csv')
book.save('C:/Users/Claire/Desktop/Recovery.csv')