# Groupe7

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

# Creation des variables du dictionnaire Annonce 

advert_state=["en ligne","expire","recupere"] # expire au bout de 30jours
object_state=["mauvais etat","etat moyen","bon etat"]
forecast_price=range(1,200)
# Il se peux que pour un debarrasement une compensation soit associée à l'annonce
# et soit renseignée dans la variable forecast_price.
#type_place=["chez un particulier","dans la rue","dans un point de collecte"]
situation=["a vendre","a donner","a debarrasser"]
volume=["peu encombrant","encombrant","tres encombrant"]
buy_place=["grande distribution","artisan","magasin specialise","indefini"]
# Generer une liste dans laquelle il y a toute les dates du 1 octobre 2016 à aujourd'hui
a=pd.date_range(datetime(2016,10,1),datetime.today(), freq='12H')
# Convertion en format liste
Date_list=pd.Series(a.format())

id_sub_category = range(1,36)
id_user = range(1,50)



# Définition de la fonction annonce qui crée un dictionnaire

def annonce(N):
    data=[] 
    z = {}
    type_place = (["chez un particulier"]*int(round((0.8*N),0)))+(["dans la rue"]*int(round((0.12*N),0)))+(["dans un point de collecte"]*int(round((0.08*N))))                                             
    for i in range(N):
            V=choice(volume)
            EA=choice(advert_state)
            EO=choice(object_state)
            TL=choice(type_place)
            S=choice(situation)
            D=choice(Date_list)
            SC=choice(id_sub_category)
            BP=choice(buy_place)
            IU=choice(id_user)
            # Conditions :
            # si un utilisateur poste une annonce d'un objet qui se trouve dans
            # ou dans un centre de collecte alors l'objet est gratuit
            if TL!="chez un particulier":
                S1=choice(["a donner","a debarrasser"])
                z = {"id_advert":i,"forecast_price":"","situation":S1,"advert_state":EA,"object_state":EO,"volume":V,"type_place":TL,"date":D,"id_sub_category":SC,"quantite":1,"buy_place":BP,"id_user":IU,"title":"truc"}
            else:
                # Mais si l'objet à récupérer se trouve chez un particulier,
                # si c'est "à donner" alors l'objet est gratuit
                if S == "a donner" :
                    z = {"id_advert":i,"forecast_price":0,"situation":S,"advert_state":EA,"object_state":EO,"volume":V,"type_place":TL,"date":D,"id_sub_category":SC,"quantite":1,"buy_place":BP,"id_user":IU,"title":"truc"}
                else:
                    # Et si la situation de l'objet est "à vendre" 
                    # un prix est forcément attribué
                    if S== "a vendre" :
                        P=choice(forecast_price)
                        z = {"id_advert":i,"forecast_price":P,"situation":S,"advert_state":EA,"object_state":EO,"volume":V,"type_place":TL,"date":D,"id_sub_category":SC,"quantite":1,"buy_place":BP,"id_user":IU,"title":"truc"}
                    # Pour finir si un objet chez un particulier
                    # n'est ni à vendre ni à donner alors l'utilisateur
                    # cherche à ce qu'on le debarrasse de cet objet en échange d'une compensation ou pas
                    else :
                        Pr=choice(range(0,20))
                        z = {"id_advert":i,"forecast_price":Pr,"situation":S,"advert_state":EA,"object_state":EO,"volume":V,"type_place":TL,"date":D,"id_sub_category":SC,"quantite":1,"buy_place":BP,"id_user":IU,"title":"truc"}
            
            data.append(z)
    return data

data=annonce(50)

# Créer un fichier csv
pd.DataFrame(data)
pd.DataFrame(data).to_csv('annonces.csv')

# Creer un fichier Annonce en JSON
jsonData=json.dumps(data)
print(jsonData)
with open ('Annonce.json','w')as f:
    json.dump(jsonData,f)
    
# Creer un fichier Annonce.xls
book=Workbook()
annonces=book.add_sheet('annonce')
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
book.save('Annonce.xls')
