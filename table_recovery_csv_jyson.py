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
import csv, math

"""
Ici on récupère l'attribut id_users de la table users
Attribut nécéssaire pour l'élaboration de la table finale
Pour faire cela, on utilise le fichier user.json précédemment généré
"""

fichier_users_json = pd.read_json('users.json', sep = ';') ####### bon titre de document par ce que pas encore de fichier de données
fichier_users_json_trie = fichier_users_json[['id_users']]

"""
Ici on récupère les attributs id_advert, advert_datetime et sub_category de la table advert
Attributs nécéssaire soit pour l'élaboration de la table finale, soit pour une meilleure génération de données
Pour faire cela, on utilise le fichier advert.json précédemment généré
fichier_advert_json : tout le fichier json, avec toutes les informations
fichier_advert_json_trie : le fichier json qu'avec les attributs que l'on veut utiliser
"""

fichier_advert_json = pd.read_json('advert.json', sep = ';') ####### bon titre de document par ce que pas encore de fichier de données
fichier_advert_json_trie = fichier_advert_json[['id_advert','advert_datetime', 'sub_category', 'advert_state']]

# Boucle for pour récupérer les identifiants des catégories à partir des libellés des sous-catégories
for i in range(len(tab_advert_json_trie)):
	if libelle_souscateg == 'chaises/tabourets' or 'tables' or 'fauteuil' or 'canape' or 'literie' or 'armoire' or 'etageres' :
		id_categ = 1
	if libelle_souscateg == 'tapisseries' or 'tapis' or 'luminaires' or 'objets' :
		id_categ = 2
	if libelle_souscateg == 'outils' or 'accessoires' :
		id_categ = 3
	if libelle_souscateg == 'verre' or 'bois' or 'bois/carton' or 'gravier/gravat' or 'carrelage' or 'acier' or 'plastique' :
		id_categ = 4
	if libelle_souscateg == 'electromenager'
		id_categ = 5
	if libelle_souscateg == 'cuisine' or 'menage' or 'autres' :
		id_categ = 6
	if libelle_souscateg == 'maison' or 'homme' or 'femme' or 'enfant' :
		id_categ = 7
	if libelle_souscateg == 'vaisselle'
		id_categ = 8
	if libelle_souscateg == 'velo' or 'skate' or 'snow' or 'roller' or 'ski' or 'trotinette' :
		id_categ = 9
	if libelle_souscateg == 'autres/divers' :
		id_categ = 10

"""
"Since" correspond à la date référence : la date de la mise en ligne de l'annonce
Informations nécéssaire pour les générations de date
tab_since =  tab_advert_json_trie[['advert_datetime']]
"""

"""
Création de la table until pour stocker les valeurs
"Until" correspond à la date de mise en ligne + nombre de jours estimés par catégorie 
recupérer la colonne état dans annonce. 
"""

tab_recov_date = []

"""
Ici on génère des dates de récupération d'objet selon leur état (en ligne, récupéré...) 
Si l'objet est en ligne, on détermine une date de récupération selon le type de catégorie
Tout en respectant le délais de 30 jours maximum de mise en ligne d'une annonce
tab_transition : tableau qui contient une date de récupération
"""
for i in range(len(tab_advert_json_trie)):
	if tab_advert_json_trie[['advert_state']] == 'en ligne' :
		if tab_advert_json_trie[2][i] == 1 or tab_advert_json_trie[2][i] == 7 : # vérifier le numéro de colonne 
			tab_recov_date = [][i] = tab_since[i] + timedelta(days = 15)
		if tab_advert_json_trie[2][i] == 2 :
			tab_recov_date = [][i] = tab_since[i] + timedelta(days = 25)
		if tab_advert_json_trie[2][i] == 8 or tab_advert_json_trie[2][i] == 10 :
			tab_recov_date = [][i] = tab_since[i] + timedelta(days = 30)
		else :
			tab_recov_date = [][i] = tab_since[i] + timedelta(days = 20)
	else :
		tab_recov_date = [][i] = NULL		

"""
Entrée : N, un entier tq la valeur correspond à un tirage d'échantillon.
Objectif de la fonction : Générer des données de la table recovery
de manière aléatoire.
Sortie : Données aléatoires de la table recovery/récupération. 
"""

def recovery(N) :
	data = [] 
	z = {}                                                  
	for i in range(N) :
		for j in range(len(tab_advert_json_trie)) :
			for k in range(len(fichier_users_json_trie)) :
		dr = tab_recov_date
        a = tab_advert_json_trie
		z = {'id_recovery' : i, 'recovery_datetime' : dr[j], 'advert' : a[j], 'recovery_user' : k}
		data.append(z)
	return data

# Génération des 2000 données aléatoires
random_data = recovery(2000)

# Création un fichier Recovery/Récupération en JSON
jsonData = json.dumps(random_data)
print(jsonData)
with open ('Recovery.json','w') as f:
	json.dump(jsonData,f)
