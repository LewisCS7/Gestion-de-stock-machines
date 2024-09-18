<!-- Structure de départ du projet -->

stock_machines--projet_flask/
│
├── app/
│   ├── templates/                # Répertoire pour les templates HTML
│   │   ├── base.html             # Template de base utilisé pour les autres templates
│   │   ├── machines.html         # Page d'accueil de l'application affichant la liste des machines
│   │   └── upload_form.html      # Page d'importation des données par fichier Excel
│   │
│   ├── __init__.py               # Initialisation de l'application Flask
│   ├── models.py                 # Modèles de données (si nécessaire)
│   └── routes.py                 # Définition des routes Flask
│
├── README.md                     # Documentation du projet
├── requirements.txt              # Liste des dépendances Python requises pour l'application
└── run.py                        # Fichier pour démarrer l'application Flask

<!-- Etapes à suivre pour commencer -->
Pour commencer, exécuter les commandes suivantes :
flask db init       # Initialisation du répertoire de migration 
flask db migrate    # Création d'une migration initiale
flask db upgrate    # Mise à jour de la base de données avec la migration
python run.py       # Lancement de l'application Flask


<!-- Quelques fonctionnalités essentielles et nécessaires -->

1.Gestion des utilisateurs : Permettre la création de comptes utilisateurs avec différents niveaux d'accès (administrateur, utilisateur standard, etc.) pour gérer l'authentification et l'autorisation.

2.Ajout, modification et suppression des machines : Permettre aux utilisateurs d'ajouter de nouvelles machines à la base de données, de modifier les informations des machines existantes et de supprimer des machines obsolètes.

3.Affichage de l'inventaire des machines : 
Afficher une liste de toutes les machines en stock avec des détails tels que le fabricant, le modèle, le numéro de série, l'état, l'emplacement, etc.

4.Recherche et filtrage des machines : 
Permettre aux utilisateurs de rechercher des machines spécifiques dans l'inventaire en fonction de différents critères tels que le fabricant, le modèle, le numéro de série, etc.

5.Importation/exportation de données : 
Permettre aux utilisateurs d'importer/exporter des données à partir/de fichiers Excel ou d'autres formats de fichier pour faciliter la gestion des données en masse.

6.Gestion des transactions : Suivre les mouvements de stock des machines, y compris les entrées, les sorties et les transferts entre différents emplacements.

7.Notifications et alertes : Envoyer des notifications automatiques par e-mail ou SMS pour informer les utilisateurs des niveaux de stock bas, des machines en panne nécessitant une réparation, etc.

8.Suivi de l'historique des modifications : Garder une trace de toutes les modifications apportées à la base de données, y compris les ajouts, les modifications et les suppressions, avec des horodatages et des informations sur l'utilisateur qui a effectué la modification.

9.Génération de rapports : Générer des rapports personnalisés sur l'état des stocks, les mouvements de stock, les tendances, etc., pour aider à prendre des décisions éclairées sur la gestion des stocks.

10.Intégrations avec d'autres systèmes : Intégrer le système de gestion des stocks avec d'autres systèmes d'entreprise tels que les systèmes de comptabilité, les systèmes de gestion des ressources humaines, etc., pour assurer une synchronisation et une cohérence des données.
