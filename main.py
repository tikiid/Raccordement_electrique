import pandas as pd

from Batiment import *
from Infrastructure import *

print('__|__' * 22)

network_df = pd.read_csv('./reseau_file/dataset/reseau_en_arbre.csv')
# print(network_df.head())

def remove_element_from_dict_with_keys(dict, list_of_key):
    for key in list_of_key:
        batiment_dict.pop(key, None)
    return dict

# Create list and dictionnary

infra_dict = {}
batiment_dict = {}
no_impact_batiment_list = []
impact_batiment_list = []
keys_to_remove = []


# Create infrastructures object

for index, row in network_df.iterrows():
    infra_id = row['infra_id']
    
    if infra_id not in infra_dict:
        infra_dict[infra_id] = Infra(
            infra_id=row['infra_id'],
            infra_length=row['longueur'],
            infra_type=row['infra_type'],
            nb_houses=row['nb_maisons']
        )
    
# Add infrastructures obj to corresponding batiment obj 

for index, row in network_df.iterrows():
    batiment_id = row['id_batiment']
        
    if batiment_id not in batiment_dict:
        batiment_dict[batiment_id] = Batiment(
            id_building=row['id_batiment'],
            list_infras=[]
        )
        
    infra_id = row['infra_id']
    batiment_dict[batiment_id].list_infras.append(infra_dict[infra_id])

# no_impact = all(infrastructure == 'infra_intacte' for infrastructure in )

# size of batiment dict
print(len(batiment_dict))

# Add not impacted batiment to a list

for bat_id, bat_obj in batiment_dict.items():
    flag = True
    for infra_object in bat_obj.list_infras:
        if not(infra_object.infra_type == 'infra_intacte'):
            flag = False
    if flag:
        no_impact_batiment_list.append(bat_obj)
        # del batiment_dict[bat_id] not working : dict change size
        keys_to_remove.append(bat_id)

# Remove not impacted batiment from batiment_dict

# for key in keys_to_remove:
#     batiment_dict.pop(key, None)

batiment_dict = remove_element_from_dict_with_keys(batiment_dict, keys_to_remove)

keys_to_remove.clear()
# size of batiment dict with impacted batiement

print(len(batiment_dict))


# checking impacted batiment
while len(impact_batiment_list) != len(batiment_dict):
    id_bat_to_add = None
    min_difficulty = 1_000_000_000_000_000_000
    for bat_id, bat_obj in batiment_dict.items():
        if min_difficulty > bat_obj.get_building_difficulty():
            min_difficulty = bat_obj.get_building_difficulty()
            id_bat_to_add = bat_id
    if id_bat_to_add == None:
        break

    # print(id_bat_to_add)
    # print(min_difficulty)
    impact_batiment_list.append((batiment_dict[id_bat_to_add], min_difficulty))
    # remove element from dictionary
    batiment_dict.pop(id_bat_to_add, None)

'''
# checking impacted batiment
while len(impact_batiment_list) != len(batiment_dict):
    id_bat_to_add = None
    min_difficulty = 1000000000000000000
    for bat_id, bat_obj in batiment_dict.items():
        if min_difficulty > bat_obj.get_building_difficulty():
            min_difficulty = bat_obj.get_building_difficulty()
            id_bat_to_add = bat_id

    print(bat_id)
    print(min_difficulty)
    impact_batiment_list.append(bat_obj)
    # remove element from dictionnary
    batiment_dict.pop(bat_id, None)

'''

# afficher les batiments à raccorder dans l'ordre
for element in impact_batiment_list:
    print(f"Id building: {element[0].id_building} - Difficulty: {element[1]}")
