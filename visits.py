# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:20:03 2017

@author: Groupe_7
"""
"""
importation des modules
"""
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
from random import *
# Generer une liste dans laquelle il y a toute les dates du 1 octobre 2016 à aujourd'hui
gen_date = pd.date_range(datetime(2016,10,1),datetime.today(), freq = '12H')
# Convertion en format liste
date_list = pd.Series(gen_date.format())
id_like = range(1,10000)
id_user_visit = range(1,10000)
id_advert_visit = range(1,10000)

"""
Entrées : le nombre de lignes a générer
Sortie : la table visites avec toutes les attributs
fonction : elle permet de générer la table visite en fonction du nombre de
lignes souhaités
"""

def visits(N):
    data = [] 
    z = {}                                                  
    for i in range(N):
            choice_id_like = choice(id_like)
            choice_id_user = choice(id_user_visit)
            choice_id_advert = choice(id_advert_visit)
            choice_date = choice(date_list)
            z = {"id_visit":choice_id_like,"user_visit":choice_id_user,
            "advert_visit":choice_id_advert,"visit_datetime":choice_date}
            data.append(z)
    return data
    
"""
création du fichier .json
"""
data = visits(100)
jsonData2 = json.dumps(data)
print(jsonData2)
with open ('visits.json','w') as f:
    json.dump(jsonData2,f)
    
"""
création du fichier excel pour st
"""
book = Workbook()   
users = book.add_sheet('users')
users.write(0,0,"id_visit")
users.write(0,1,"user_visit")
users.write(0,2,"advert_visit")
users.write(0,3,"visit_datetime")
for i in range(1,len(data)):
        users.write(i,0,data[i]["id_visit"])
        users.write(i,1,data[i]["user_visit"])
        users.write(i,2,data[i]["advert_visit"])
        users.write(i,3,data[i]["visit_datetime"])
book.save('visits.xls') #Enregistrement fichier EXCEL