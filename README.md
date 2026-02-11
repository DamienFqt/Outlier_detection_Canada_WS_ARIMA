# A propos

__Detecting Outliers in Time Series Using Window-Sliding ARIMA: A Case Study on Montreal’s Daily Temperatures__

Ce projet présente une méthode de détection d’outliers appliquée aux températures quotidiennes au Canada - un ARIMA avec fenêtre glissantes. 

Réalisé dans le cadre de la 3ème année du Magistère "Economiste-Statisticien" et de l'année du Master 2 "Econométrie et Statistique".

Il a été soumis (en anglais) au journal __International Journal of Climatology__. 

# Contenu du repo
### Dossier `rendus`
- L'[article.pdf](docs/Article%20-%20Detecting%20Outliers%20in%20Time%20Series%20Using%20Window-Sliding.pdf) soumis au journal 
- Le [graphique.png](rendus/outliers.png) illustrant la comparaison entre un ARIMA global et la méthode par fenêtres glissantes
### Dossier `src`
- Le code `preprocessing.py` permettant de télécharger les données depuis `Kaggle` et les traiter
- Le code `outlier_detection.py` permettant de générer une détection d'outliers en indiquant des paramètres sur les fenêtres glissantes et le seuil de décision (outlier ou non)
- Le code `main.py`  permettant de les orchestrer
### Dossier `notebooks`
Un dossier exploratoire fournissant des résumés numériques, graphiques et autres insights. 


# Abstract 
This article describes and implements a method for outlier detection in the specific context
of time series, drawing on the taxonomy proposed by Blazquez-Garcia et al. (2021). First,
the study briefly presents the aforementioned taxonomy, then focuses on anomaly detection
in daily temperature data from Montreal, Canada. The aim is both to implement a modern
outlier detection technique and to carry out this analysis on data with high-stakes implica-
tions: those related to climate change. For this, we use a historical dataset on Canadian
climate. This database contains daily information on average temperatures and precipitation
for 13 Canadian weather stations from 1940 to 2019. The detection method is carried out
using an AutoRegressive Integrated Moving Average (ARIMA) model with a sliding window.
It detects an increasing number of outliers over time, which suggests, to some extent, the
existence of climate warming. This article is the first to combine a little-used method with
climate data from Montreal


# Résumé 
Cet article décrit et met en œuvre une méthode pour la détection d’outliers dans le contexte spécifique des séries temporelles, en s’appuyant sur la taxonomie proposée par Blazquez-Garcia et al. (2021). D’abord, l’étude présente brièvement la taxonomie mentionnée, puis se concentre sur la détection d’anomalies dans les données de température quotidienne à Montréal, Canada. L’objectif est à la fois d’implémenter une technique moderne de détection d’outliers et de réaliser cette analyse sur des données avec des implications importantes : celles liées au changement climatique. Pour cela, nous utilisons un jeu de données historique sur le climat canadien. Cette base de données contient des informations quotidiennes sur les températures moyennes et les précipitations pour 13 stations météorologiques canadiennes de 1940 à 2019. La méthode de détection est réalisée en utilisant un modèle AutoRegressive Integrated Moving Average (ARIMA) avec une fenêtre glissante. Elle détecte un nombre croissant d’outliers au fil du temps, ce qui suggère, dans une certaine mesure, l’existence d’un réchauffement climatique. Cet article est le premier à combiner une méthode peu utilisée avec des données climatiques de Montréal.