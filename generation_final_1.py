"""
Groupe7
v1.0.1
"""
import pandas as pd
import json


# Ouverture de fichiers csv

advert = pd.read_csv('adverts.csv')
#supprimer la première colonne
advert = advert.drop(advert.columns[[0]], axis=1) 


# Jointure advert-sub_category

sub_categ = pd.read_csv('sub_category.csv')

result = pd.merge(advert, sub_categ, how='left', on='sub_category')
# supprimer id_sub_category
result = result.drop(result.columns[[14]], axis=1)
# modifier le nom de la colonne 'name_sub_category' en 'sub_category'
result = result.rename(columns = { 'name_sub_category' : 'sub_category'})

# Jointure advert-category

category = pd.read_csv('category.csv')

result1 = pd.merge(result, category, how='left', on='category')
result1 = result1.drop(result1.columns[[6]], axis=1)

#### Jointure advert-address (avec id_district et ajouter la colonne city)

# Import des donnees au format json
with open('adresse.json') as data_file:    
    data1 = json.load(data_file)

# Transformation des donnees en dataframe
address = pd.read_json(data1)
# renomer la colonne id_adress
address = address.rename(columns = { 'id_adress' : 'advert_address'})
address ["city_name"] = 'TOULOUSE'
address = address.drop(address.columns[[0,]], axis=1)

result2 = pd.merge(result1, address, how='left', on='advert_address')
result2 = result2.drop(result2.columns[[0]], axis=1)


#### Jointure advert-district

# Import des donnees au format json
with open('District.json') as data_file:    
    data2 = json.load(data_file)

# Transformation des donnees en dataframe
district = pd.read_json(data2)
district = district.drop(district.columns[[0]], axis=1)

# importation fichier json district

result3 = pd.merge(result2, district, how='left', left_on='district', right_on='id_district')
# supprimer id_district
result3 = result3.drop(result3.columns[[25]], axis=1)

# Jointure advert-user

# Import des donnees au format json
with open('mail1.json') as data_file:    
    data3 = json.load(data_file)

# Transformation des donnees en dataframe
mail = pd.read_json(data3)

result4 = pd.merge(result3, mail, how='left', left_on='advert_user', right_on='id_U')
# supprimer advert_user, id_U
result4 = result4.drop(result4.columns[[3, 28]], axis=1)

# Changer le nom de certaine colonne
result4 = result4.rename(columns = { 'name_district' : 'district_name'})
result4 ["complement"] = ''
result4 ["description"] = ''





# Créer un fichier csv
pd.DataFrame(result4).to_csv('advert_final.csv')
pd.json(result4)

# Creer un fichier Annonce en JSON

    