# Communication Client-Serveur en Python

Ce projet implémente une application de communication entre un serveur et un client en Python. Il constitue une base solide pour des applications nécessitant un échange de données entre plusieurs systèmes via des sockets.

## Fonctionnalités

- **Communication en temps réel** entre le client et le serveur.
- **Gestion des connexions multiples** (si applicable).
- **Implémentation simple et efficace** en utilisant les sockets Python.

## Prérequis

- Python 3.6 ou une version ultérieure.
- Une machine ou un réseau permettant la communication entre le client et le serveur.

## Installation

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/adamchehade/Application-communicante.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd Application-communicante
   ```
3. Installez les dépendances requises (s'il y en a) :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Lancement du serveur

1. Exécutez le script du serveur :
   ```bash
   python server.py
   ```
2. Le serveur sera en attente de connexions des clients.

### Lancement du client

1. Exécutez le script du client :
   ```bash
   python client.py
   ```
2. Entrez les messages que vous souhaitez envoyer au serveur. Les réponses du serveur seront affichées en temps réel.

### Exemple de session

1. Démarrez le serveur :
   ```bash
   python server.py
   ```
   Output attendu :
   ```
   Serveur en attente de connexions sur le port 5000...
   ```

2. Démarrez le client :
   ```bash
   python client.py
   ```
   Output attendu :
   ```
   Connecté au serveur sur 127.0.0.1:5000
   Entrez votre message :
   ```

3. Envoyez un message depuis le client et voyez la réponse sur les deux terminaux.

## Configuration

- Par défaut, le serveur écoute sur `127.0.0.1` et le port `5000`.
- Vous pouvez modifier ces paramètres dans les fichiers `server.py` et `client.py`.

## Structure du projet

```
<nom-du-depot>/
├── client.py       # Script pour le client
├── server.py       # Script pour le serveur
├── requirements.txt # Dépendances Python (facultatif)
└── README.md       # Documentation du projet
```

## Contributions

Les contributions sont les bienvenues ! Veuillez suivre les étapes ci-dessous :

1. Forkez le dépôt.
2. Créez une nouvelle branche : `git checkout -b feature/ma-nouvelle-fonctionnalite`.
3. Effectuez vos modifications et validez-les : `git commit -m 'Ajout d'une nouvelle fonctionnalité'`.
4. Poussez vers votre branche : `git push origin feature/ma-nouvelle-fonctionnalite`.
5. Créez une Pull Request.

## Licence

Ce projet est sous licence adamch. Vous êtes libre de l'utiliser, de le modifier et de le distribuer avec mention de l'auteur original.

## Auteur

Projet créé par Adam chehade

