# Planification du raccordement électrique de bâtiments

Ce code en Python réalise une planification du raccordement électrique de bâtiments en fonction d'un réseau électrique donné. Il utilise des objets "Batiment" et "Infrastructure" pour modéliser les bâtiments et les infrastructures du réseau, respectivement. Le processus de planification comprend la création d'objets pour les infrastructures et les bâtiments, l'association des infrastructures aux bâtiments, et enfin la sélection des bâtiments impactés en fonction de leur difficulté de raccordement.

## Utilisation
Assurez-vous d'avoir les fichiers nécessaires dans le dossier spécifié (par exemple, './dataset/reseau_en_arbre.csv'). Le programme commence par lire un fichier CSV contenant les informations sur le réseau électrique.

network_df = pd.read_csv('./dataset/reseau_en_arbre.csv')
Ensuite, le code crée des objets "Infrastructure" et "Batiment" à partir des données du réseau.

## Processus de Planification
Le code suit les étapes suivantes pour planifier le raccordement électrique :

- Création d'objets "Infrastructure" à partir des données du réseau.
- Association des infrastructures aux bâtiments correspondants.
- Identification des bâtiments non impactés et suppression de ceux-ci du dictionnaire des bâtiments.
- Sélection des bâtiments impactés en fonction de leur difficulté de raccordement.
- Affichage des Résultats (les bâtiments impactés avec leur niveau de difficulté).

## Collaborateurs
Thibaut Schweitzer

Théau Naudin
