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
            list_infras=0
        )

for bat_id, bat_obj in batiment_dict.items():
    print(f"batiment id: {bat_obj.id_building}")

print("_" * 30)

# for infra_id, infra_obj in infra_dict.items():
#     infra_obj.get_infra_difficulty()
#     print(f"Infrastructure ID: {infra_id}, Type: {infra_obj.infra_type}, Nb House(s): {infra_obj.nb_houses}, Length: {infra_obj.length}, Difficulty: {infra_obj.infra_difficulty}")













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
