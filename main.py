import pandas as pd

from Batiment import *
from Infrastructure import *

print('__|__' * 22)

network_df = pd.read_csv('./reseau_file/dataset/reseau_en_arbre.csv')
# print(network_df.head())

infra_dict = {}
batiment_dict = {}



for index, row in network_df.iterrows():
    infra_id = row['infra_id']
    
    if infra_id not in infra_dict:
        infra_dict[infra_id] = Infra(
            infra_id=row['infra_id'],
            infra_length=row['longueur'],
            infra_type=row['infra_type'],
            nb_houses=row['nb_maisons']
        )
    

for index, row in network_df.iterrows():
    batiment_id = row['id_batiment']
        
    if batiment_id not in batiment_dict:
        batiment_dict[batiment_id] = Batiment(
            id_building=row['id_batiment'],
            list_infras=[]
        )
        
    infra_id = row['infra_id']
    batiment_dict[batiment_id].list_infras.append(infra_dict[infra_id])




# for infra_index, infra_element in infra_dict.items():
    


# for bat_id, bat_obj in batiment_dict.items():
    
# for batiment_id, batiment_obj in batiment_dict.items():
#     print(f"Batiment ID: {batiment_id}, Number of Infras: {len(batiment_obj.list_infras)}")
#     for infra_obj in batiment_obj.list_infras:
#         print(f"  Infrastructure ID: {infra_obj.infra_id}, Type: {infra_obj.infra_type}, Length: {infra_obj.length}")














'''
# faire une table croisée dynamique

# batiment_subdfs = network_df.groupby(by="id_batiment")
# for id_batiment, batiment_subdf in batiment_subdfs:
#     print(id_batiment)
#     print(batiment_subdf)
#     print("_" * 30)

# infra_subdfs = network_df.groupby(by="infra_id")
# for id_infra, infra_subdf in infra_subdfs:
#     print(id_infra)
#     print(infra_subdf)
#     print("_" * 30)

'''
