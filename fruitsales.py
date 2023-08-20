"""In this exercise we will create a Pandas Dataframe with fruit sales information and 
write the data to a CSV file. This exercise is based on the Lesson 1 exercise in the 
Kaggle Learn Pandas course.
Write a Python program that creates a Pandas Dataframe that matches the table below:

Apples	Bananas
2017 Sales	35	21
2018 Sales	41	34
Write the data to a file called fruit.csv in the project directory."""
import pandas as pd
columns = {"Apples":[35,41],"Bananas":[21,34]}
index = ['2017 Sales','2018 Sales']
df = pd.DataFrame(columns, index)
df.to_csv("fruit.csv")
print(df)





