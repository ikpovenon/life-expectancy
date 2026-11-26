\# WHO Life Expectancy — Analyse de l'espérance de vie (2000–2015)



\## Présentation du projet



Ce projet vise à analyser l'évolution de l'espérance de vie et les disparités entre les pays de 2000 à 2015, ainsi qu'à explorer les facteurs sanitaires et socioéconomiques qui peuvent y être associés.



Il s'appuie sur le jeu de données \*Life Expectancy (WHO)\* disponible sur Kaggle, enrichi et fiabilisé à partir de sources officielles de la Banque mondiale, de l'OMS et de l'UNICEF.



\*\*Données :\*\* 2 938 observations, 193 pays, 23 colonnes après fiabilisation.



\## Objectifs analytiques



\- Identifier les pays présentant les espérances de vie les plus élevées et les plus faibles.

\- Comparer l'espérance de vie selon le statut de développement.

\- Étudier son évolution entre 2000 et 2015.

\- Analyser les facteurs sanitaires, économiques et sociaux associés à l'espérance de vie.

\- Explorer la modélisation prédictive de cet indicateur.



\## Méthodologie



Le projet suit une démarche inspirée de \*\*CRISP-DM\*\*, avec une gestion Agile/Scrum organisée autour de User Stories et de livrables analytiques.



\*\*Outils :\*\* Python, Pandas, NumPy, SciPy, Matplotlib, Seaborn, Jupyter Notebook, Git, GitHub et Jira.



\## Travaux réalisés



\### Préparation et fiabilisation des données

\- Diagnostic des valeurs manquantes, des doublons et des incohérences.

\- Intégration de données officielles et reconstruction de plusieurs variables.

\- Remplacement intégral de `life\_expectancy` par les estimations de la Banque mondiale.

\- Harmonisation des noms de colonnes et des codes pays ISO3.

\- Actualisation du dictionnaire des variables et exportation du jeu fiabilisé.



\### Analyses exploratoires et statistiques



| User Story | Principaux résultats |

|---|---|

| \*\*LEP-14 — Classement des pays\*\* | Identification des 10 pays aux valeurs les plus élevées et les plus faibles ; forte stabilité des classements (Spearman : ρ = 0,9627). |

| \*\*LEP-15 — Statut de développement\*\* | Écart moyen de 11,60 ans en faveur des pays développés ; différence statistiquement significative. |

| \*\*LEP-16 — Évolution temporelle\*\* | Progression moyenne de 4,80 ans entre 2000 et 2015 ; 181 pays en progression sur 183 étudiés. |



\## Structure du projet



```text

life-expectancy/

├── data/

│   ├── raw/

│   ├── external/

│   └── processed/

├── notebooks/

│   ├── 01\_diagnostic\_initial\_qualite\_des\_donnees.ipynb

│   ├── 02\_preparation\_fiabilisation\_des\_donnees.ipynb

│   ├── 03\_LEP\_14\_classement\_pays.ipynb

│   ├── 04\_LEP\_15\_statut\_developpement.ipynb

│   └── LEP\_16\_evolution\_temporelle.ipynb

├── reports/

│   └── rapport\_WHO\_Sprint 2 et 3.docx

└── README.md

```



\## État d'avancement



\*\*Sprints 2 et 3 : réalisés.\*\*



Prochaines étapes : analyse des facteurs sanitaires et socioéconomiques, sélection des caractéristiques et développement d'un modèle prédictif.



\## Équipe — Groupe 8



\- Ista Kpovenon

\- Sylvain Effohi

\- Émile Nibasumba

\- Rosnys



\## Sources principales



\- \[Life Expectancy (WHO) — Kaggle](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)

\- \[Banque mondiale — World Development Indicators](https://databank.worldbank.org/source/world-development-indicators)

\- \[OMS / UNICEF — Estimations de couverture vaccinale](https://immunizationdata.who.int/)

