# Groupe 7

# Importation des modules
import json
import numpy
import math
from numpy.random import randn
import random
import xlrd
from datetime import date, datetime, timedelta
from xlwt import Workbook, Formula
import pandas as pd
import string

advert_state = ["Online","Expired","Recovered"] # expire au bout de 30jours
object_state = ["Poor condition","Good condition","Very good condition"]
forecast_price = range(1,200)

# Il se peux que pour un debarrasement une compensation soit associee à l'annonce
# et soit renseignee dans la variable forecast_price.

type_place = ["Sale to private","In the street","In the treatment center"]
situation = ["To sale","To give","To get rid of"]
volume = ["small","cumbersome","very cumbersome"]
buy_place = ["grande distribution","artisan","magasin specialise","indefini"]

# Generer une liste dans laquelle il y a toute les dates du 1 octobre 2016 à aujourd'hui
gen_date = pd.date_range(datetime(2016,10,1),datetime.today(), freq = '12H')
# Convertion en format liste

date_list = pd.Series(gen_date.format())
id_sub_category = range(1,36)
id_user = range(1,50)

# Definition de la fonction annonce qui cree un dictionnaire

def advert(N):
    data = [] 
    z = {}                                                  
    for i in range(N):

            vol = choice(volume)
            adv_st = choice(advert_state)
            obj_sta = choice(object_state)
            typ_pla = choice(type_place)
            situ = choice(situation)
            dat_lis = choice(date_list)
            id_sub_cat = choice(id_sub_category)
            buy_pl = choice(buy_place)
            id_us = choice(id_user)
            
            # Conditions :
            # si un utilisateur poste une annonce d'un objet qui se trouve dans
            # ou dans un centre de collecte alors l'objet est gratuit
            
            if typ_pla!= "chez un particulier":
                situ1 = choice(["a donner","a debarrasser"])
                z = {"id_advert":i,"forecast_price":"","situation":situ1,"advert_state":adv_st,"object_state":obj_sta,"volume":vol,"type_place":typ_pla,"date":dat_lis,"id_sub_category":id_sub_cat,"quantite":1,"buy_place":buy_pl,"id_user":id_us}
            else:
                # Mais si l'objet à recuperer se trouve chez un particulier,
                # si c'est "à donner" alors l'objet est gratuit
                if situ == "a donner" :
                    z = {"id_advert":i,"forecast_price":0,"situation":situ,"advert_state":adv_st,"object_state":obj_sta,"volume":vol,"type_place":typ_pla,"date":dat_lis,"id_sub_category":id_sub_cat,"quantite":1,"buy_place":buy_pl,"id_user":id_us}
                else:
                    # Et si la situation de l'objet est "à vendre" 
                    # un prix est forcement attribue
                    if situ == "a vendre" :
                        p = choice(forecast_price)
                        z = {"id_advert":i,"forecast_price":p,"situation":situ,"advert_state":adv_st,"object_state":obj_sta,"volume":vol,"type_place":typ_pla,"date":dat_lis,"id_sub_category":id_sub_cat,"quantite":1,"buy_place":buy_pl,"id_user":id_us}
                    # Pour finir si un objet chez un particulier
                    # n'est ni à vendre ni à donner alors l'utilisateur
                    # cherche à ce qu'on le debarrasse de cet objet en echange d'une compensation ou pas
                    else :
                        pr = choice(range(0,20))
                        z = {"id_advert":i,"forecast_price":pr,"situation":situ,"advert_state":adv_st,"object_state":obj_sta,"volume":vol,"type_place":typ_pla,"date":dat_lis,"id_sub_category":id_sub_cat,"quantite":1,"buy_place":buy_pl,"id_user":id_us}
            
            data.append(z)
    return data

data = advert(50)
  
# Creer un fichier Generation en JSON
jsonData = json.dumps(data)
print(jsonData)
with open ('advert.json','w') as f:
    json.dump(jsonData,f)
    
# Creer un fichier Generation.xls
book = Workbook()
annonces = book.add_sheet('annonce')
annonces.write(0,0,"id_advert")
annonces.write(0,1,"advert_state")
annonces.write(0,2,"situation")
annonces.write(0,3,"object_state")
annonces.write(0,4,"forecast_price")
annonces.write(0,5,"volume")
annonces.write(0,6,"type_place")
annonces.write(0,7,"date")
annonces.write(0,8,"id_sub_category")
annonces.write(0,9,"quantite")
annonces.write(0,10,"buy_place")
annonces.write(0,11,"id_user")

for i in range(1,len(data)):
        annonces.write(i,0,data[i]["id_advert"])
        annonces.write(i,1,data[i]["advert_state"])
        annonces.write(i,2,data[i]["situation"])
        annonces.write(i,3,data[i]["object_state"])
        annonces.write(i,4,data[i]["forecast_price"])
        annonces.write(i,5,data[i]["volume"])
        annonces.write(i,6,data[i]["type_place"])
        annonces.write(i,7,data[i]["date"])
        annonces.write(i,8,data[i]["id_sub_category"])
        annonces.write(i,9,data[i]["quantite"])
        annonces.write(i,10,data[i]["buy_place"])
        annonces.write(i,11,data[i]["id_user"])   
book.save('Generation.xls')


category = {"mobilier" : ["chaises / tabouret" , "table", 
"fauteuil", "canape", "literie", "armoire", "etageres"], 
"decos" : ["tapisserie" , "tapis", "luminaires" , "objets"], 
"jardin" : ["outils", "accessoires"], 
"textiles":["maison","hommes","femmes","enfants"],
"vaisselles":[],
"transports":["velo","skate","snow","roller","ski","trotinette"],
"autres/divers":[], 
"materiaux_encombrant":["verres","bois","papier/carton","gravier/gravat","carrelage","acier","plastique"],
"electromenager":[],
"petits_electromenager":["cuisine","menage","autres"]}

def gene_category(n):    
  data = [] 
  list_category = {} # Creation d'un tableau de donnee
  category_keys = []


  for iteration_keys in category.keys():
     category_keys.append(iteration_keys)                                           
  for i in range(n):
          categ = category_keys[random.randint(0,len(category_keys)-1)]
          if len(category[categ]) !=  0:
             sub_categ = category[categ][random.randint(0,len(category[categ])-1)]
          else :
               sub_categ = ""
          list_category = {"id_ui" : i , "Category" : categ, "Sub_Category" :sub_categ}
          data.append(list_category)
  return data

data1 = gene_category(50)

jsonData1 = json.dumps(data1)
print(jsonData1)
with open ('category.json','w') as f:
    json.dump(jsonData1,f)

#Alimentation dans un fichier EXCEL

category_xls = book.add_sheet('Category')
category_xls.write(0,0,"id_ui")
category_xls.write(0,1,"Category")
category_xls.write(0,2,"Sub_Category")

# Alimentation des champs via les valeurs du dictionnaire

for i in range(1,len(data1)):
    category_xls.write(i,0,data1[i]["id_ui"])
    category_xls.write(i,1,data1[i]["Category"])
    category_xls.write(i,2,data1[i]["Sub_Category"])

book.save('Generation.xls') # Enregistrement fichier EXCEL


# Listes des modalites pour les variables
sex = ["M","W"]
age = range(15,100)
csp = ["agriculteur","artisans, comm, Cent.","cadres et prof. Intellectuels","prof intermediaire","employes","ouvriers","retraites","chomage","student","others"]
interest = ["","sport","theatre","cinema","travel","music","jeux-videos","informatique","recyclage","jardinage","animals","photographie","lecture","painting","decoration interieure","peche","camping","mode","chasse","automobile","cook","other"]
district = ["CAPITOLE","SAINT-GEORGES","JUNCASSE - ARGOULETS","GRAMONT",
"LA TERRASSE","ZONES D'ACTIVITES SUD","FONTAINE-LESTANG","PONT-DES-DEMOISELLES",
"PATTE D'OIE","LE BUSCA","CROIX-DE-PIERRE","REYNERIE","MATABIAU","FAOURETTE",
"SAINT-ETIENNE","SAINT-SIMON","LES IZARDS","SAINT-MARTIN-DU-TOUCH","LES CHALETS",
"LARDENNE","ARENES","AMIDONNIERS","MIRAIL-UNIVERSITE","LES PRADETTES","COMPANS",
"GINESTOUS","SAINT-MICHEL","FER-A-CHEVAL","BELLEFONTAINE","SOUPETARD","PAPUS",
"POUVOURVILLE","BASSO-CAMBO","ARNAUD BERNARD","SAINT-AUBIN - DUPUY","JULES JULIEN",
"CROIX-DAURADE","CASSELARDIT","MINIMES","RAMIER","LA CEPIERE","EMPALOT","LALANDE",
"RANGUEIL - CHR - FACULTES","CARMES","LA FOURGUETTE","BARRIERE-DE-PARIS",
"MONTAUDRAN - LESPINET","SAINT-AGNE","PURPAN","SAUZELONG - RANGUEIL","SAINT-CYPRIEN",
"BAGATELLE","GUILHEMERY","MARENGO - JOLIMONT","COTE PAVEE","CHATEAU-DE-L'HERS","ROSERAIE",
"BONNEFOY","SEPT DENIERS"]

permission = range(1,6)
#Informations pour creation de variables
domain = ["@hotmail.fr","@hotmail.com","@gmail.com","@live.fr","@yahoo.fr","@live.com"]
liste_char = string.ascii_letters + string.digits
k = 7          

#Tirage aleatoire des modalites pour chaque variable et generation d'un individu
def users(n):
    data = [] 
    z = {}                                                   
    for i in range(n):
            interest = ["","sport","theatre","cinema","voyage","musique","jeux-videos","informatique","recyclage","jardinage","animaux","photographie","lecture","peinture","decoration interieure","peche","camping","mode","chasse","automobile","cuisine","autres"]
            sx = choice(sex)
            old = choice(age)
            distr = choice(district)
            cp = choice(csp)
            list_choice1 = choice(interest)
            interest.remove(list_choice1)
            list_choice2 = choice(interest)
            interest.remove(list_choice2)
            list_choice3 = choice(interest)
            if list_choice1 == "":
                list_choice2 = list_choice1
                list_choice3 = list_choice1
            if list_choice2 == "":
                list_choice3 = list_choice2
            if (list_choice2 == list_choice1 or list_choice2 == list_choice3):   
               list_choice2 = "" 
            if (list_choice3 == list_choice1 or list_choice3 == list_choice2):
                list_choice3 = ""
            
            list_email = ''.join(sample(liste_char,k)) + choice(domain)
            perm = choice(permission)
                
            z = {"id_U":i,"age":old,"sex":sx,"CSP":cp,"interest1":list_choice1,
            "interest2":list_choice2,"interest3":list_choice3,"district":distr, "email" : list_email, 
            "user_permission" : perm}

            data.append(z)
    return data

data2 = users(50)

#Conversion en fichier JSON
 
jsonData2 = json.dumps(data2)
print(jsonData2)
with open ('users.json','w') as f:
    json.dump(jsonData2,f)

#Alimentation dans un fichier EXCEL

#Creation des champs
users = book.add_sheet('users')
users.write(0,0,"id_U")
users.write(0,1,"district")
users.write(0,2,"age")
users.write(0,3,"sex")
users.write(0,4,"interets1")
users.write(0,5,"interest2")
users.write(0,6,"interest3")
users.write(0,7,"CSP")
users.write(0,8,"email")
users.write(0,9,"user_permission")

#Alimentation des champs via les valeurs du dictionnaire

for i in range(1,len(data2)):
        users.write(i,0,data2[i]["id_U"])
        users.write(i,1,data2[i]["district"])
        users.write(i,2,data2[i]["age"])
        users.write(i,3,data2[i]["sex"])
        users.write(i,4,data2[i]["interest1"])
        users.write(i,5,data2[i]["interest2"])
        users.write(i,6,data2[i]["interest3"])
        users.write(i,7,data2[i]["CSP"])
        users.write(i,8,data2[i]["email"])
        users.write(i,9,data2[i]["user_permission"])
book.save('Generation.xls') #Enregistrement fichier EXCEL


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
		dat_lis = choice(date_list)
		z = {'id_recovery' : i, 'recovery_date' : dat_lis, 'id_advert' : i, 'recovery_user' : i}
		data.append(z)
	return data

# Génération des 50 données aléatoires
random_data = recovery(50)

# Création un fichier Recovery/Récupération en JSON
jsonData = json.dumps(random_data)
print(jsonData)
with open ('Recovery.json','w') as f:
	json.dump(jsonData,f)


# Création d'un fichier Recovery.xls
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
"""pd.DataFrame(random_data)
pd.DataFrame(random_data).to_csv('Recovery.csv')"""
book.save('Generation.xls')









