DataMiningNews

#Catégorisation d'articles

##Problématique

Nous avons choisi d'utiliser un jeu de données de 100,001+ articles trouvés sur le site kaggle.com.

Notre but était de classer les articles par catégories.

##Raisonnement 

Depuis ces données nous avons décidé de déterminer des "catégories" en comparant les articles entre eux. Pour ce faire nous avons extrait de leur contenu tous les noms et y avons attaché leur fréquence d'apparition. Ensuite nous n'avons gardé que les mots qui ont une fréquence >= 2.

Puis, à partir de ces données nous les avons regroupés pour former une matrice avec pour abscisses tous les mots de tous les articles et en ordonnés tous les articles.
Cela nous a donné un nouveau fichier utilisable par le logiciel Weka au format ".arff".

Grâce a Weka nous avons pu ensuite clusteriser les articles avec un algorithme.

