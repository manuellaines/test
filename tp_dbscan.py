import pandas as pd
# Substitute the path_to_file content by the path to your csv file 
path_to_file = 'data.csv'
customer_data = pd.read_csv(path_to_file)
# customer.head() : affiche les 5 premieres ligne du fichier
# customer.info() : permet de verifier s'il ya les donnees manquantes
#customer_data.shape: retourne le couple (nombre de ligne,nombre de colones)
#customer_data.columns retourne le nom des colones
#customer_data['Spending Score (1-100)'].hist(): construit l'histogramme des client en fonction de leurs depenses
#customer_data.describe().transpose() :Cela nous donnera un tableau à partir duquel nous pourrons lire les distributions d'autres valeurs de notre ensemble de données
#customer_data['Genre'].unique(): retourne les valeurs possible pour le type genre
#customer_data['Genre'].value_counts(normalize=True): affiche la proportion entre les valeurs de la donnee genre
print(customer_data['Spending Score (1-100)'].hist())
# https://stackabuse.com/feature-scaling-data-with-scikit-learn-for-machine-learning-in-python/
#https://stackabuse.com/dimensionality-reduction-in-python-with-scikit-learn/
#https://stackabuse.com/k-means-clustering-with-scikit-learn/
#https://machinelearningmastery.com/using-singular-value-decomposition-to-build-a-recommender-system/
#https://towardsdatascience.com/beginners-guide-to-creating-an-svd-recommender-system-1fd7326d1f65
#https://jaketae.github.io/study/svd/
#https://realpython.com/gradient-descent-algorithm-python/
# german_data=pd.read_csv('german.data',delimiter='\s+')
# tracer les fonction avec python
#https://poe.com/chat/2pbqdzgf0a364ac37xw
# https://www.kaggle.com/code/hassanashfaq2001/denclue-clustering-algorithm