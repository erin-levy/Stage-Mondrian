# Stage-Mondrian

**Stage-Mondrian** est un projet Python développé dans le cadre d'un stage, visant à générer des compositions artistiques inspirées du style de Piet Mondrian. Le projet explore la création algorithmique de grilles colorées en utilisant différentes approches de quadrillage, de gestion des couleurs et de placement des formes.

## 📁 Structure du projet

Le dépôt contient plusieurs scripts Python, chacun correspondant à une étape ou une fonctionnalité spécifique du projet :

- `mondrian.py` : Script principal pour générer une composition Mondrian.
- `grille4.py`, `quadrillage_1.py`, `quadrillage_2.py`, etc. : Scripts pour la création et la gestion des grilles.
- `couleurs1.py` à `couleurs4.py` : Scripts explorant différentes palettes et méthodes d'application des couleurs.
- `défaussage.py`, `fail_prolongement.py` : Scripts traitant des cas particuliers ou des erreurs dans la génération.
- `fonctions_init.py`, `fonctions_couleurs4.py`, `fonctions_quadrillage4.py` : Fonctions utilitaires utilisées dans les scripts principaux.
- `stockage.py` : Script pour la sauvegarde ou le chargement des données.
- `historique.json`, `zoom.json` : Fichiers JSON contenant des données de configuration ou d'historique.
- `impossible.odg`, `Mondrian 13.06.zip`, `Mondrian 26.06.zip` : Fichiers liés à la documentation ou aux versions archivées du projet.

## 🚀 Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/erin-levy/Stage-Mondrian.git
   cd Stage-Mondrian
   ```

2. **Créer un environnement virtuel (optionnel mais recommandé) :**

   ```bash
   python3 -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

3. **Installer les dépendances :**

   Le projet utilise uniquement des bibliothèques standard de Python. Cependant, si des bibliothèques externes sont nécessaires, elles devraient être listées dans un fichier `requirements.txt`. Assurez-vous de l'installer si présent :

   ```bash
   pip install -r requirements.txt
   ```

## 🖼️ Utilisation

Exécutez le script principal pour générer une composition :

```bash
python mondrian.py
```

Les autres scripts peuvent être exécutés individuellement pour explorer différentes fonctionnalités ou approches du projet.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📫 Contact

Pour toute question ou suggestion, veuillez contacter [erin-levy](https://github.com/erin-levy).
