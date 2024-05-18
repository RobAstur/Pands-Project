#data Frame
import pandas as pd
#Plotting
import matplotlib.pyplot as plt
#numerical arrays
import numpy as np

# More comments in the jupyter notebook

# Loading the file into python. The reason I used below website is that all the columnns are correctly build with names.

iris_dataset = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#Adding the print to see a picture of the dataset
print(iris_dataset)

# Section 1. More info under this topic on the jupyter notebook called Iris_project. Below function will create/open a text file called summary each time it is run. It will contain a short summary of all the variables. 


filename = "summary.txt"

with open(filename, 'w') as f:
    df_string = iris_dataset.describe().to_string()
    f.write(df_string)


# Summary of the data in the dataset
iris_dataset.info()


# Section 2. Create arrays to prepare data for plotting with Numpy 

seplen = iris_dataset["sepal_length"]
seplen = seplen.to_numpy()


# Creating histograms
plt.hist(seplen, color="darkgreen",edgecolor="black",  linestyle='--', alpha=0.5)
plt.title("Sepal Length in cm")
plt.xlabel('Sepal_Length_cm') 
plt.ylabel('Count') 
plt.show() 


sewidt = iris_dataset["sepal_width"]
sewidt = sewidt.to_numpy()

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


# Creating scatter plots
plt.scatter(seplen, sewidt , marker='8', s=50,  color = "cornflowerblue", edgecolor="black")
plt.title("Sepal Length Vs Sepal Width")
plt.xlabel('Sepal_Length_cm') 
plt.ylabel('Sepal_width_cm') 

plt.show() 



plt.scatter(seplen, peleng , marker='8', s=50,  color = "green", edgecolor="black")
plt.title("Sepal Length Vs Petal_Length_cm")
plt.xlabel('Petal_Length_cm') 
plt.ylabel('Petal_Length_cm') 

plt.show() 


plt.scatter(seplen, pewidt , marker='8', s=50,  color = "Blue", edgecolor="black")
plt.title("Sepal Length Vs Petal_Width_cm")
plt.xlabel('Petal_Length_cm') 
plt.ylabel('Petal_Width_cm') 

plt.show() 




plt.scatter(pewidt, peleng , marker='x', s=40,  color = "orange", edgecolor="black")
plt.title("Sepal_Width Vs Petal_Length_cm")
plt.xlabel('Sepal_width_cm') 
plt.ylabel('Petal_Length_cm') 

plt.show() 



plt.scatter(peleng, pewidt, marker='x', s=40,  color = "red", edgecolor="black")
plt.title("Petal_length Vs Petal_width_cm")
plt.xlabel('Petal_length_cm') 
plt.ylabel('Petal_Width_cm') 

plt.show() 



# Aditonal analysis - 

number_of_flowers =iris_dataset["species"].value_counts().plot.bar(color="darkgreen",edgecolor="limegreen")
number_of_flowers.set_facecolor("snow")
plt.title("Number of flowers per Specie")

plt.show()



iris_dataset["species"].value_counts().plot.pie(autopct='%1.1f%%')
plt.legend(loc="upper left")
plt.title("Percentage of flowers per specie")

plt.show()



flowers_grouped = iris_dataset[['species', 'petal_length']].groupby('species').mean().reset_index()

plt.bar(flowers_grouped["species"], flowers_grouped["petal_length"], color="powderblue",edgecolor="black")
plt.title('Average petal lenght by species')

# Adding the scatter plot shows us the range of Petal Length of each of the species. 
plt.scatter(iris_dataset ["species"], iris_dataset[ "petal_length"], color = "seagreen")

plt.show()

flowers_grouped = iris_dataset[['species', 'petal_width']].groupby('species').mean().reset_index()

plt.bar(flowers_grouped["species"], flowers_grouped["petal_width"], color="powderblue",edgecolor="black")
plt.title('Average petal width by species')

# Adding the scatter plot shows us the range of petal width of each of the species. 
plt.scatter(iris_dataset ["species"], iris_dataset[ "petal_width"], color = "seagreen")

plt.show()



flowers_grouped = iris_dataset[['species', 'sepal_length']].groupby('species').mean().reset_index()

plt.bar(flowers_grouped["species"], flowers_grouped["sepal_length"], color="powderblue",edgecolor="black")
plt.title('Average sepal Length by species')

# Adding the scatter plot shows us the range of sepal length of each of the species. 
plt.scatter(iris_dataset ["species"], iris_dataset[ "sepal_length"], color = "seagreen")

plt.show()



flowers_grouped = iris_dataset[['species', 'sepal_width']].groupby('species').mean().reset_index()

plt.bar(flowers_grouped["species"], flowers_grouped["sepal_width"], color="powderblue",edgecolor="black")
plt.title('Average sepal width by species')

# Adding the scatter plot shows us the range of sepal width of each of the species. 
plt.scatter(iris_dataset ["species"], iris_dataset[ "sepal_width"], color = "seagreen")

plt.show()

