
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
'''

# Below function will create/open a text file called summary each time it is run. It will contain a short summary of all the variables. More info in the jupyter notebook. Seccion 1


filename = "summary.txt"

with open(filename, 'w') as f:
    df_string = iris_dataset.describe().to_string()
    f.write(df_string)


# We use this function to get information about the data types
'''
print(iris_dataset.dtypes)

'''

'''
# Create arrays to prepare data for plotting 

seplen = iris_dataset["sepal_length"]
seplen = seplen.to_numpy()

sewidt = iris_dataset["sepal_width"]
sewidt = sewidt.to_numpy()
print(sewidt)

peleng = iris_dataset["petal_length"]
peleng = peleng.to_numpy()
print(peleng)

pewidt = iris_dataset["petal_width"]
pewidt = pewidt.to_numpy()
print(pewidt)
'''

