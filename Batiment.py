import pandas as pd 

class Batiment:
    def __init__(self, id_building, list_infras):
        self.id_building = id_building
        self.list_infras = list_infras
        

    def get_building_difficulty(self):
        bat_difficulty = 0
        for element in self.list_infras:
            bat_difficulty += element.get_infra_difficulty()
        return bat_difficulty