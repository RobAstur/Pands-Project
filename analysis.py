
import pandas as pd
#Plotting
import matplotlib.pyplot as plt
#numerical arrays
import numpy as np


# Loading the file into python

iris_dataset = 'iris.data'

iris_dataset = pd.read_csv("iris.data")


# Summary of the data set

print(iris_dataset)

'''
# We use this function to get information about the data types

print(iris_dataset.dtypes)

# Summary of the data 

print (iris_dataset.describe())


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

