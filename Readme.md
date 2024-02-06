# TP1 - DMB

Réalisé par Quentin LEGRAND et Bastien SAUVAT

## 💻 0. Prérequis

Pour lancer le TP, ajoutez les fichiers **"./kill_match_stats_final_0.csv" et "./agg_match_stats_0.csv"** à la racine du projet.

## 💻 1. Présentation du TP

Dans ce projet, nous effectuons une analyse de données d'un dataset sur le jeu PUBG.

Nous allons effectuer des analyses sur les meilleurs joueurs ainsi que les scores des joueurs.

Nous utilisons les librairies Spark et GraphX pour effectuer ces analyses.

## 💻 2. Préparation du jeu de données

Pour préparer le jeu de données, nous avons effectué les opérations suivantes :

- Importation des données
- Démarrage d'une session Spark
- Chargement du jeu de données
- Sélection des colonnes pertinentes

## 💻 3. Les meilleurs joueurs

Voici un échantillon de statistiques de joueurs :

```markdown
| Killer Name       | Number of Games  | Average Kills per Game |
|-------------------|------------------|------------------------|
| KrazyPortuguese   | 1.00             | 1.00                   |
| nide2Bxiaojiejie  | 1.00             | 3.00                   |
| Ascholes          | 1.00             | 2.00                   |
| Weirdo7777        | 1.00             | 1.00                   |
| Solayuki1         | 1.00             | 1.00                   |
| xuezhiqian717     | 1.00             | 3.00                   |
| pdfjkkvjk         | 1.00             | 1.00                   |
| xiaogao13         | 1.00             | 2.00                   |
| Jingchita         | 1.00             | 1.00                   |
| Alexande-999      | 1.00             | 3.00                   |
```


Voici le TOP 10 des meilleurs joueurs : (joueurs ayant la meilleure moyenne de kills par partie)

```markdown
| Killer Name       | Number of Games  | Average Kills per Game |
|-------------------|------------------|------------------------|
| #unknown          | 20.00            | 154.00                 |
| gogolnyg          | 1.00             | 62.00                  |
| 651651646         | 1.00             | 42.00                  |
| EsNmToging        | 1.00             | 36.00                  |
| MoGu1314          | 1.00             | 25.00                  | 
| s1000r-race       | 1.00             | 24.00                  |
| KouBxczG          | 1.00             | 24.00                  |
| Hidden-In-Bushes  | 2.00             | 22.00                  |
| EVEN1982          | 1.00             | 20.00                  |
| A_Dadyo_o         | 1.00             | 20.00                  |
```


## 💻 4. Score des joueurs

