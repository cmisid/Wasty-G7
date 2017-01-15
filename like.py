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

# Creation des variables

gen_date = pd.date_range(datetime(2016,10,1),datetime.today(), freq = '2H')
# Convertion en format liste
like_datetime = pd.Series(gen_date.format())
user = range(1,1000)
advert_like=range(1,2000)

"""
Entrées : le nombre de lignes a générer
Sortie : la table like avec toutes les attributs
fonction :générer la table like
"""
def like(N):
    data=[] 
    z = {}                                                  
    for i in range(N):
            V=choice(advert_like)
            id_u=choice(user)
            D=choice(like_datetime)
           
            z = {"id_like":i,"advert_like":V,"like_datetime":D,"user_like":id_u}
            data.append(z)
    return data

data=like(50)

# Creer un fichier like en JSON
jsonData=json.dumps(data)
print(jsonData)
with open ('like.json','w')as f:
    json.dump(jsonData,f)
    
# Creer un fichier Annonce.xls
book=Workbook()
like=book.add_sheet('likes')
like.write(0,0,"id_like")
like.write(0,1,"advert_like")
like.write(0,2,"like_datetime")
like.write(0,3,"user_like")

for i in range(1,len(data)):
        like.write(i,0,data[i]["id_like"])
        like.write(i,1,data[i]["advert_like"])
        like.write(i,2,data[i]["like_datetime"])
        like.write(i,3,data[i]["user_like"])
         
book.save('like.xls')
