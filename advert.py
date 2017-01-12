"""
 Groupe7
 v1.1.0
"""
# Importation des modules
import json
import numpy
import math
from numpy.random import randn
import random
from random import *
from xlwt import Workbook
from datetime import date, datetime, timedelta
import pandas as pd

# Creation des variables du dictionnaire Advert 

advert_state = ["en ligne", "expire", "recupere"]

price = range(1,200)

""" Il se peux que pour un debarrasement une compensation soit associée à l'annonce
et soit renseignée dans la variable price."""

situation = ["a vendre", "a donner", "a debarrasser"]
volume = ["peu encombrant", "encombrant", "tres encombrant"]
buy_place = ["grande distribution", "artisan", "magasin specialise", "indefini"]

# Generer une liste dans laquelle il y a toute les dates du 1 octobre 2016 à aujourd'hui
var_date = pd.date_range(datetime(2016,10,1), datetime.today(), freq='12H')

# Convertion en format liste
Date_list = pd.Series(var_date.format())

# Générer contraint_time_begin et contraint_time_end
constraint_time_begin = pd.to_datetime( pd.date_range( "16:00", "20:30", freq = "15min20S").strftime('%H:%M:%S'))
constraint_time_end = (constraint_time_begin[0] + timedelta(hours = 3)).strftime('%H:%M:%S')

# A modifier selon le nombre de utilisateurs générés
advert_user = range(1,950)
advert_address = range(1,66124)

# Ouvrir le fichier json avec les url d'images
# Lecture du fichier json
with open('images.json') as data_file:    
    img = json.load(data_file)
img[0]

url_img = []
url = {}
for i in range(len(img)):
    url = img[i]['URL Image']
    url_img.append(url)

"""
Entrée : Le nombre de ligne à générer pour la table annonce
Objectif de la fnction : Définition de la fonction advert qui crée un dictionnaire
Sortie : jeu de donnée composé de tous les attributs de la table annonce
"""

def advert(N):
    data = [] 
    list_init = {}
    vol = {}
    object_state = numpy.random.choice(["mauvais etat", "etat moyen", "bon etat"], N, replace = True, p = [0.2, 0.7, 0.1])
    type_place = numpy.random.choice(["chez un particulier", "dans la rue", "dans un point de collecte"], N, replace = True, p = [0.8, 0.12, 0.08])
    sub_category = numpy.random.choice(['10', '11', '12', '13', '14', '15', '16', '20', '21', '22', '23', '30', '31', '40', '41', '42', '43', '44', '45', '46', '50', '60', '61', '62', '70', '71', '72', '73', '80', '90', '91', '92', '93', '94', '95', '100'], N, replace = True, p = [0.026, 0.0125, 0.0030, 0.0020, 0.0050, 0.0250, 0.03, 0.027, 0.026, 0.027, 0.03, 0.025, 0.035, 0.03, 0.028, 0.037, 0.006, 0.018, 0.002, 0.042, 0.11, 0.02, 0.013, 0.002, 0.072, 0.043, 0.062, 0.092, 0.05, 0.03, 0.025, 0.002, 0.012, 0.0025, 0.01, 0.018])        
    for i in range(N):
            choice_advert_state = choice(advert_state)
            choice_object_state = choice(object_state)
            choice_type_place = choice(type_place)
            choice_situation = choice(situation)
            choice_Date_list = choice(Date_list)
            choice_sub_category = choice(sub_category)
            choice_buy_place = choice(buy_place)
            choice_advert_user = choice(advert_user)
            choice_advert_address = choice(advert_address)
            choice_constraint_time_begin = choice(constraint_time_begin)
            choice_url_img = choice(url_img)
            # Conditions :
            id_category = int(str(choice_sub_category)[0])
            if id_category == 1:
                volu = choice(numpy.random.choice(["encombrant", "tres encombrant"], 10, replace = True, p = [0.3, 0.7]))
            elif id_category == 2 or id_category == 7 :
                volu = 'peu encombrant'           
            elif id_category == 5 :
                volu = 'tres encombrant'
            elif id_category == 6 or id_category == 8 :
                volu = choice(["peu encombrant", "encombrant"])
            elif id_category == 9 :
                volu = choice(numpy.random.choice(["encombrant", "peu encombrant"], 10, replace = True, p = [0.65, 0.35]))
            elif id_category == 4 or id_category == 3 :
                volu = choice(["peu encombrant", "encombrant", "tres encombrant"])
            
            vol = {"volume":volu}

            if vol["volume"] == 'tres encombrant' :
                poids = choice(range(5,50))
                # si un utilisateur poste une annonce d'un objet qui se trouve dans
                # ou dans un centre de collecte alors l'objet est gratuit
                if choice_type_place != "chez un particulier" :
                    choice_situation1 = choice(["a donner", "a debarrasser"])
                    list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":"", "situation":choice_situation1, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":poids, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img} 
                else :
                    # Mais si l'objet à récupérer se trouve chez un particulier,
                    # si c'est "à donner" alors l'objet est gratuit
                    if choice_situation == "a donner" :
                        list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":0, "situation":choice_situation, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":poids, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
                    else :
                        # Et si la situation de l'objet est "à vendre" 
                        # un prix est forcément attribué
                        if choice_situation == "a vendre" :
                            choice_price = choice(price)
                            list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":choice_price, "situation":choice_situation, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":poids, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
                        # Pour finir si un objet chez un particulier
                        # n'est ni à vendre ni à donner alors l'utilisateur
                        # cherche à ce qu'on le debarrasse de cet objet en échange d'une compensation ou pas
                        else :
                            prime = choice(range(0,20))
                            list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":prime, "situation":choice_situation, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":poids, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
            if vol["volume"] == 'encombrant' :
                poids = choice(range(1,10))
                # si un utilisateur poste une annonce d'un objet qui se trouve dans
                # ou dans un centre de collecte alors l'objet est gratuit
                if choice_type_place != "chez un particulier" :
                    choice_situation1 = choice(["a donner", "a debarrasser"])
                    list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":"", "situation":choice_situation1, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":poids, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
                else :
                    # Mais si l'objet à récupérer se trouve chez un particulier,
                    # si c'est "à donner" alors l'objet est gratuit
                    if choice_situation == "a donner" :
                        list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":0, "situation":choice_situation, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":poids, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
                    else :
                        # Et si la situation de l'objet est "à vendre" 
                        # un prix est forcément attribué
                        if choice_situation == "a vendre" :
                            choice_price = choice(price)
                            list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":choice_price, "situation":choice_situation, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":poids, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
                        # Pour finir si un objet chez un particulier
                        # n'est ni à vendre ni à donner alors l'utilisateur
                        # cherche à ce qu'on le debarrasse de cet objet en échange d'une compensation ou pas
                        else :
                            prime = choice(range(0,20))
                            list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":prime, "situation":choice_situation, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":poids, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
            if vol["volume"] == 'peu encombrant' :
                if choice_type_place != "chez un particulier" :
                    choice_situation1 = choice(["a donner", "a debarrasser"])
                    list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":"", "situation":choice_situation1, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":0, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
                else :
                    # Mais si l'objet à récupérer se trouve chez un particulier,
                    # si c'est "à donner" alors l'objet est gratuit
                    if choice_situation == "a donner" :
                        list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":0, "situation":choice_situation, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":0, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
                    else :
                        # Et si la situation de l'objet est "à vendre" 
                        # un prix est forcément attribué
                        if choice_situation == "a vendre" :
                            choice_price = choice(price)
                            list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":choice_price, "situation":choice_situation, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":0, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
                        # Pour finir si un objet chez un particulier
                        # n'est ni à vendre ni à donner alors l'utilisateur
                        # cherche à ce qu'on le debarrasse de cet objet en échange d'une compensation ou pas
                        else :
                            prime = choice(range(0,20))
                            list_init = {"id_advert":i, "advert_address":choice_advert_address, "price":prime, "situation":choice_situation, "advert_state":choice_advert_state, "object_state":choice_object_state, "volume":volu, "type_place":choice_type_place, "advert_date":choice_Date_list, "sub_category":choice_sub_category, "quantity":1, "buy_place":choice_buy_place, "advert_user":choice_advert_user, "title":"truc", "weight":0, "category":int(str(choice_sub_category)[0]), "constraint_time_begin":choice_constraint_time_begin.strftime('%H:%M:%S'), "constraint_time_end":(choice_constraint_time_begin + timedelta(hours=3)).strftime('%H:%M:%S'), "advert_img":choice_url_img}
                
                
            data.append(list_init)
    return data

data = advert(3000)


# Créer un fichier csv
annonce = pd.DataFrame(data)
pd.DataFrame(annonce).to_csv('advert.csv')


# Creer un fichier Annonce en JSON

jsonData = json.dumps(data)
print(jsonData)
with open ('Advert.json','w')as f:
    json.dump(jsonData,f)
