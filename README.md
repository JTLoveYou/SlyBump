# Discord Auto Bump Script

**Discord Auto Bump Script** est un bot automatisé conçu pour envoyer des commandes `/bump` sur Discord via plusieurs comptes utilisateurs. Le bot utilise **Selenium** pour contrôler une session **Firefox** et **Tkinter** pour fournir une interface utilisateur simple.

 ![Version](https://img.shields.io/badge/Version-v3.0-red)
![Python](https://img.shields.io/badge/python-100%25-red)


███████╗██╗  ██╗   ██╗██████╗ ██╗   ██╗███╗   ███╗██████╗ 
██╔════╝██║  ╚██╗ ██╔╝██╔══██╗██║   ██║████╗ ████║██╔══██╗
███████╗██║   ╚████╔╝ ██████╔╝██║   ██║██╔████╔██║██████╔╝
╚════██║██║    ╚██╔╝  ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝ 
███████║███████╗██║   ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║     
╚══════╝╚══════╝╚═╝   ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     

## Fonctionnalités

- Connexion automatique à Discord
- Navigation vers différents canaux sur plusieurs serveurs
- Envoi automatique de la commande `/bump`
- Interface graphique pour surveiller les logs et l'état du bot
- Captures d'écran en cas d'erreur

## Prérequis

- **Python 3.x** : [Télécharger Python](https://www.python.org/downloads/)
- **Firefox** : [Télécharger Firefox](https://www.mozilla.org/en-US/firefox/new/)
- **Geckodriver** : [Télécharger GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- **Selenium** installé :  
  ```bash
  pip install selenium
Tkinter installé (inclus avec la plupart des distributions Python)

##Configuration
Configurer le script Python :
Dans le fichier main.py, remplacez les placeholders comme votre_email1, votre_mot_de_passe1, id_du_serveur1, id_du_salon1 par vos informations Discord.

Exemple de configuration dans le script :
 ```bash
accounts = [
    {
        'email': 'votre_email1@example.com',
        'password': 'votre_mot_de_passe1',
        'servers_and_channels': [
            ("id_du_serveur1", "id_du_salon1"),
            ("id_du_serveur2", "id_du_salon2")
        ]
    },
    {
        'email': 'votre_email2@example.com',
        'password': 'votre_mot_de_passe2',
        'servers_and_channels': [
            ("id_du_serveur3", "id_du_salon3"),
            ("id_du_serveur4", "id_du_salon4")
        ]
    }
]
 ```

##Exécuter le script :
Utilisez la commande suivante pour exécuter le script :

 ```bash
python main.py

 ```

##Modifier le mode headless (optionnel) :
Pour exécuter le script sans ouvrir de fenêtre de navigateur, décommentez la ligne suivante dans la fonction create_driver :

 ```bash
options.add_argument("--headless")

 ```


Cela inclut **tout le contenu** du **README.md** dans un bloc de code **bash** comme demandé.
