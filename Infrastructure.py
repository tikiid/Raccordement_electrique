import pandas as pd 

class Infra:
    def __init__(self, infra_id, infra_length, infra_type, nb_houses):
        self.infra_id = infra_id
        self.length = infra_length
        self.infra_type = infra_type
        self.nb_houses =  nb_houses
        
        
    def repair_infra(self):
        if self.infra_type == "a_remplacer": 
            self.infra_type = "infra_intacte"
    
    def get_infra_difficulty(self):
        if self.infra_type == "infra_intacte":
            return 0
        return self.length / self.nb_houses
