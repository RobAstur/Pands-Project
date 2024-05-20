# Iris data set analysis

***

## Introduction

Iris is a genus of flowers with more than 300 species.  The iris data set was made famous by British statistician and biologist Ronald Fisher. It contains 3 different types of iris flowers (Iris setosa, Iris virginica and Iris versicolor). It is one of the most popular datasets for data analytics. The aim of this project is to provide simple analysis with extensive research. 

SETOSA

![Setosa_flower](https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg)

VIRGINICA

![Virginica_flower](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1200px-Iris_virginica_2.jpg)

VERSICOLOR

![Versicolor_flower](https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg)



Data is available on [GITHUB](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv)
Originally published [ICS.UCI](https://archive.ics.uci.edu/dataset/53/iris)

This section was created using **references 1** and **reference 2**

## Research

For this research a different set of histograms, scatter plots, bar charts were created. The aim is to extract the key insights of the data set and get a better understanding of the iris flowers. Moreover, external sources will be used to validate and confirm the key findings.

![Versicolor_flower](https://editor.analyticsvidhya.com/uploads/51518iris%20img1.png)

First thing to highlight is that According to **Reference 15**  the 3 species of iris flowers are not directly comparable because of their different sources. However it is still a good set of info for data analytics. Setosa flowers were found in Alaska, Versicolor in northeastern Ohio and Virginica outhward along the Atlantic Coast. **Reference 15**

![Where_the_flowers_are](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/jrssig/18/6/10.1111_1740-9713.01589/1/m_sign_18_6_26_fig-2.jpeg?Expires=1718732637&Signature=PhfRbUxedr7JCJwotC34t5gVX1RUNYEvgnEwdMwl-ecTZ0haSxwV77nkcDxmWQPMEcBasdfit4veQhtsqtMM9iRzko7Bi8C3ym3I1T~DIZvyu2W196Br10aLeWhFelxSX7rsiRT20SHiRCzIOLT53b9CylMIkN7tmY92VzTobPHs1GDViQ28K-N4DcBiUBcq7YH4TPtR35fVzvBtEV2WR6aD0Bnkhvf4acShucMPyPEuIf6oj2yIYcTHc1pwzWB5~iIrarOOnEmdEd7EvXLHolnFcPW4-tCSjrojC6lz9Y6YbSk16YQFcZ9ntx3L0DWHniL0GzoA2OT~bBLdJqwIFw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Before starting the analysis it is important to see the composition of the data set. We can see that the number of subjects per specie is the same with 50 flowers each.

![Bar_chart_number of species](https://github.com/RobAstur/Pands-Project/blob/main/Bar%20chart%20Number_of_flowers_in_dataset_per_species.png)
![Pie_chart](https://github.com/RobAstur/Pands-Project/blob/main/Pie_charts_number%20of%20species.png)


### Information from Histograms 

To better understand the analysis it is important to open the different histograms while reading the analysis.
Website atlassian **Reference 5**, defined histogram as " chart that plots the distribution of a numeric variable’s values as a series of bars. Each bar typically covers a range of numeric values called a bin or class; a bar’s height indicates the frequency of data points with a value within the corresponding bin."

The histograms of each of the flowers features shows different frecuencies for each of them. The key points are listed below.

* The petal lenght feature have the highest frecuency  between 1.0 and 2.0 cms. Aproximate 50 subjects falls in this category.
* The petal width feature shows the highest frequency in between 0.0 and 0.5 cms. Around 40 subjects falls in this category.
* The sepal lenghts feature have the highest frecuency in between 5.5 and 6.0. Between 40 and 45 subjects falls into this category
* The sepal width have highest frequency in between 3.0 and 3.5. Aproximate  65 subjects falls into this category

Above data is confirmed by **reference 4**

According to **reference 9** and **reference14** and the information provided by the histograms, by using the feature Petal length we can separate setosa flowers from the group. If a flower has a petal lenght of 1.5 cm we can conclude it is a setosa flower but if it has a 5 cm petal lenght we couldn't say it is versicolor or virginica **Reference 17**. 

It is not possible to do the same with sepal length and sepal width, as separation is not so clear. Moreover, petal width is not well defined. Thus, we can conclude that petal length is the ***key feature*** to distinguise setosa flowers from the rest of the group.**Reference 9** 


### Information from Scatterplot

To better understand the anylisis it is important to open the different scatterplots while reading the analysis.

Website atlassian **reference 6** defined scatter plot  as "A scatter plot (aka scatter chart, scatter graph) uses dots to represent values for two different numeric variables. The position of each dot on the horizontal and vertical axis indicates values for an individual data point. Scatter plots are used to observe relationships between variables."

The scatter charts provide very interesting information that can be see in below key points.

* Petals Length and Petal Width
    * According to **reference 6** **reference 14** and **reference 7** there is correlation between petal length and width, flowers with longer petals tend to have wider widths. **reference 12** suggest that petal length  is the key feture to identify the flowers.
    * In the charts we can see that setosa flowers Petal length and petal width are the smaller and the virginica are the largest. Versicolor has average values. 
    * We can see that setosa flowers can be easily separated and identified by petals. **Reference 10** **reference 12** **reference 15**
    * **Reference 14** suggest that petal width can be used alone to separate setosa flowers from rest of the subjects.

* Sepal Length and Sepal Width
    * Setosa flowers have the highest sepal width and it is combined with a low sepal length. Versicolor flowers has average values and Virginica are the opposite of setosa with low sepal with and high sepal length.
    * Setosa flowers can also be separated from the rest of the flowers in the dataset using sepal measurements. **reference 11** **reference 15**
    * Although virginica is larger than Versicolor, they have many points overlapping **Reference 10**. Thus, it would be difficult to identify flowers using  Sepal Length and width alone. **Reference 13**. **Reference 16** argue that it is not possible to separate flowers using only sepal length.
    * According to **Reference 16** there is weak correlation bewteen sepal lenght and sepal width. **Reference 14** see a moderate negative correlation between sepal length and sepal width. This statement imply that flowers that havee longer sepals tend to have narrower widths.

### Combination of bar charts and scatter plot

This section shows 4 different bar charts combined with scatter plots. It combine one of the principel features (petal and sepal sizes) and species. Bar chart calculates the mean and scatter plot add the range of sizes. It provides a very interesting information for analysis. It helps to confirm and understand the information provided by the previous section

* Petal Length by species - As we have learnt the setosa flowers has smaller petal length and can be easily separated. However in this chart if we analized the scatter plot range we can see an overlaping between versicolor and virginica in values around 5.5 to 7.0 cms range.

![Petal_Length](https://github.com/RobAstur/Pands-Project/blob/main/Average%20Sepal%20Length%20by%20species%20%2B%20scatter%20plot.png)

* Petal width by species - We have the same situation. Setosa flowers can be completely separated from Versicolor and Virginica. For this 2 values the scatter plot range shows clear overlaping between values 1.5 cm to almost 2 cm for versicolor and virginica.

![Petal_Width](https://github.com/RobAstur/Pands-Project/blob/main/Average%20petal%20width%20by%20species%20%2B%20scatterplot.png)

* Sepal Length by species - in this case there are overlaping between the 3 species. We could potentially separate small small values of setosa flower and highest values of Virginica. Rest of the values are overlaping and it would make impossible to separate the different types of flower

![Sepal_lenght](https://github.com/RobAstur/Pands-Project/blob/main/Average%20Sepal%20Length%20by%20species%20%2B%20scatter%20plot.png)

*  Sepal width by species - badsed on the sepal width we can see that most the range of values overlapse for the the 3 flowers. Only setosa flowers with sepal width over 4 cms could be easily identify.

![Sepal_Width](https://github.com/RobAstur/Pands-Project/blob/main/Average%20Sepal%20Width%20by%20species%20%2B%20scatter%20plot.png)

###  Other type of charts using referenced work 



This section is created using images form references. They are great for visualization and it provide clear views and analysis of teh dataset.

One of the most popular charts to analyse the iris dataset is the pair charts. It is a combination of the charts that I created individually (histograms, scatter plots). It includes different colores which is great in terms of visualization. 


![PAIR_CHART](https://miro.medium.com/v2/resize:fit:720/format:webp/1*EC0wwBEYyc6nHbKfkdvn9g.png) **Reference 9**


The box chart is offers good visualization of the distribution. This chart confirms the points previosly highlighted. Sepal length can be used to separate setosa flowers from the rest of the subjects. However, there are overlaping between versicolor and virginica. in terms of the sepal Width the plot confirm the same data. There are some differences but are not very pronounce **Reference 14**


![SEPAL_L_BOX](https://miro.medium.com/v2/resize:fit:640/format:webp/1*bGDLQW129SZqhiE_wy8h4w.png) **Reference 14**
![Sepal_W_bBOX](https://miro.medium.com/v2/resize:fit:640/format:webp/1*qDBKrz-BPYvymnyQe1dOhw.png) **Reference 14**



### References

* 1  [WIKIPEDIA](https://en.wikipedia.org/wiki/Iris_(plant))
* 2  [WIKIPEDIA](https://en.wikipedia.org/wiki/Iris_flower_data_set)
* 3  [MEDIUM_OYIN](https://medium.com/@OyinWoyin/insights-from-the-iris-data-set-e149f0b6941f)
* 4  [GEEKFORGEEK](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)
* 5  [ATLASSIAN_HI](https://www.atlassian.com/data/charts/histogram-complete-guide#:~:text=What%20is%20a%20histogram%3F,value%20within%20the%20corresponding%20bin.)
* 6  [ATLASSIAN_SCAT](https://www.atlassian.com/data/charts/what-is-a-scatter-plot)
* 6  [gexijin.github](https://gexijin.github.io/learnR/step-into-r-programmingthe-iris-flower-dataset.html)
* 7  [MEDIUM_EMINE](https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c)
* 8  [XIAOIRUI](https://xiaorui.site/Data-Mining-R/lecture/2.B_EDA_Vis.html)
* 9  [MEDIUM_NIRAJAN](https://medium.com/@nirajan.acharya666/exploratory-data-analysis-of-iris-dataset-9c0df76771df)
* 10 [GITHUB_ABHI](https://github.com/abhikumar22/Exploratory-Data-Analysis-on-IRIS-Dataset/blob/master/EDA_Flower.ipynb)
* 11 [SCIKIT](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html#:~:text=Scatter%20Plot%20of%20the%20Iris%20dataset,-import%20matplotlib.pyplot&text=You%20can%20already%20see%20a,the%20Versicolor%20and%20Virginica%20types.)
* 12 [MEDIUM_VID](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-32d09a52f322)
* 13 [WARWICK](https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/r/iris_plots/)
* 14 [MEDIUM_LEVELUP](https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d)
* 15 [ACADEMIC](https://academic.oup.com/jrssig/article/18/6/26/7038520?login=false)
* 16 [GITRABIUL](https://gist.github.com/rabiulcste/33d985ab55820353181f9727a9496a81)
* 17 [SCIENCE_DIRECT](https://www.sciencedirect.com/topics/computer-science/iris-virginica)