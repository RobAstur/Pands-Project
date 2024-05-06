
import pandas as pd
#Plotting
import matplotlib.pyplot as plt
#numerical arrays
import numpy as np


# Loading the file into python. The reason I used below website is that all the columnns are correctly build with names.

iris_dataset = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

'''
# Summary of the data set

print(iris_dataset)


# Below function will create/open a text file called summary each time it is run. It will contain a short summary of all the variables. More info in the jupyter notebook. Seccion 1



filename = "summary.txt"

with open(filename, 'w') as f:
    df_string = iris_dataset.describe().to_string()
    f.write(df_string)


# We use this function to get information about the data types

print(iris_dataset.dtypes)

'''


# Create arrays to prepare data for plotting 

seplen = iris_dataset["sepal_length"]
seplen = seplen.to_numpy()

'''
plt.hist(seplen, color="darkgreen",edgecolor="black",  linestyle='--', alpha=0.5)
plt.title("Sepal Length in cm")
plt.xlabel('Sepal_Length_cm') 
plt.ylabel('Count') 
plt.show() 
'''

sewidt = iris_dataset["sepal_width"]
sewidt = sewidt.to_numpy()
'''
plt.hist(sewidt, color="cornflowerblue",edgecolor="black",  linestyle='--', alpha=0.5)
plt.title("Sepal Width in cm")
plt.xlabel('Sepal_Width_cm') 
plt.ylabel('Count') 
plt.show() 



peleng = iris_dataset["petal_length"]
peleng = peleng.to_numpy()


plt.hist(peleng, color="khaki",edgecolor="darkgreen",  linestyle='--', alpha=0.5)
plt.title("Petal Length in cm")
plt.xlabel('Petal_Length_cm') 
plt.ylabel('Count') 
plt.show() 



pewidt = iris_dataset["petal_width"]
pewidt = pewidt.to_numpy()


plt.hist(pewidt, color="plum",edgecolor="magenta",  linestyle='--', alpha=0.5)
plt.title("Petal Width in cm")
plt.xlabel('Petal_Width_cm') 
plt.ylabel('Count') 
plt.show() 

'''

plt.scatter(seplen, sewidt , marker='8', s=50,  color = "cornflowerblue", edgecolor="black")
plt.title("Sepal Length Vs Sepal Width")
plt.xlabel('Sepal_Length_cm') 
plt.ylabel('Sepal_width_cm') 

plt.show() 
