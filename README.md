# BIGDATA

#  1.Lancement du docker 
### Pour lancer docker 

```
docker compose up 
```

# 2.Configuration du Namenode

### Pour se rendre sur le namenode 

```
docker compose -it namenode bash
```
## On créer un dossier dans le namenode pour stocker les CSV 

```
mkdir nom_du_dossier 
```
## On copie les fichier CSV pour les mettre dans le Namenode

```
docker cp covid.csv f0ee2a0d4686:/root/nom_du_dossier
```

```
docker cp frequentation-gares.csv f0ee2a0d4686:/root/csv
```

# Configuration du HDFS
 ## Création du dossier dans le HDFS 
 
 ```
 hdfs dfs -mkdir nom_du_dossier
 ```
 ## On va chercher les fichier du namenode pour les mettre dans le HDFS

 ```
 hdfs dfs -put /root/csv/frequentation-gares.csv /nom_du_dossier
 ```

 ```
 hdfs dfs -put /root/csv/covid.csv /nom_du_dossier
 ```
## Lancement programme 

### se rendre sur Jupyter pour executer notre solution


```
localhost:8888
```
