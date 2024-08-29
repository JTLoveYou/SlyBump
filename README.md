# SlyBump

**SlyBump** est un bot automatisé conçu pour envoyer des commandes `/bump` sur Discord via plusieurs comptes utilisateurs. Le bot utilise Selenium pour contrôler une session Firefox, et Tkinter pour fournir une interface utilisateur simple.

 ![Version](https://img.shields.io/badge/Version-v1.0-red)
![Python](https://img.shields.io/badge/python-100%25-red)


## Fonctionnalités

- Connexion automatique à Discord
- Navigation vers différents canaux sur plusieurs serveurs
- Envoi automatique de la commande `/bump`
- Interface graphique pour surveiller les logs et l'état du bot

## Prérequis

- **Python 3.x**
- **Firefox** installé avec un profil configuré pour garder la session ouverte
- **Selenium** installé (`pip install selenium`)
- **Geckodriver** disponible dans le PATH ou spécifié directement dans le script

## Configuration

1. **Configurer le script Python :**

   - Remplacez `votre_nom_utilisateur` par votre nom d'utilisateur Windows.
   - Remplacez `votre_profil` par le nom de votre profil Firefox.
   - Remplacez les placeholders comme `votre_email1`, `votre_mot_de_passe1`, `id_du_serveur1`, `id_du_salon1`, etc. par vos informations Discord.

2. **Exécuter le script :**
   - Utilisez la commande suivante pour exécuter le script :
     ```bash
     python SlyBump.py
     ```

3. **Modifier le mode headless (optionnel) :**
   - Pour exécuter le script sans ouvrir de fenêtre de navigateur, décommentez la ligne suivante dans la fonction `create_driver` :
     ```python
     options.add_argument("--headless")
     ```

## Avertissement

**SlyBump** est un outil d'automatisation. L'utilisation de bots sur Discord peut enfreindre les conditions d'utilisation de Discord. Utilisez cet outil à vos propres risques.

## License

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
