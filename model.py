#Basic stuff and data-preprocessing
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
#Splitting two piece 
from sklearn.model_selection import train_test_split

#Importing model
from sklearn.neighbors import KNeighborsClassifier

#Accuracy score
from sklearn.metrics import accuracy_score
#Save model
import pickle

#Load data
df=load_iris()
x_train,x_test,y_train,y_test=train_test_split(df.data,df.target)

#Create Model
knn=KNeighborsClassifier(n_neighbors=5)

#Fit model
model=knn.fit(x_train,y_train)

pred=knn.predict(x_test)

print(f"accuracy score {accuracy_score(pred,y_test)}")
filename="file.pkl"
pickle.dump(model,open(filename,"wb"))