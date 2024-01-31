#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:39:49 2024

@author: andisiwematu
"""

# DAY 2 OF THE SUMMER SCHOOL

import pandas as pd

file1 = pd.read_csv("Users/andisiwematu/ccs2024_project/ccs2024_day2/data_02/iris.csv")


file1 = pd.read_csv("data_02/iris.csv")

"""Python Quiz 2 - Variables"""

x ="5"
y= 5
print(y+x)


x = [1,2,3]
y = x
y[0] = 4
print(x)


x="12.2"
print("x")


x=23
y=10
print(z)


val = 2+3*(36/9+1)**2-1
print(val)

"""Extract, Transform, Load"""

file = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

print(file)


file = pd.read_excel("data_02/residentdoctors.xlsx")

print(file)

file = pd.read_json("data_02/student_data.json")

print(file)


url= "https://https://raw.githubusercontent.com/Asabele240701/css4_day02/blob/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

df = pd.read_csv(url)



df = pd.read_csv("Accelerometer_data.csv", names =["date_time", "x", "y", "z"])

print(df)

"""Transform"""

df = pd.read_csv("data_02/country_data_index.csv")
df = pd.read_csv("data_02/country_data_index.csv",index_col=0)
print(df)


file = pd.read_excel("data_02/residentdoctors.xlsx")
 

#extracting the lower range in the agedist column
print(file.info())



"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 161 entries, 0 to 160
Data columns (total 9 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object  #should be numeric but there is text in some cells
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
dtypes: float64(5), int64(2), object(2)
memory usage: 11.4+ KB
None"""

file["LOWER_AGE"] = file["AGEDIST"].str.extract('(\d+)-')

file["UPPER_AGE"] = file["AGEDIST"].str.extract('-(\d+)')

file["LOWER_AGE"] = file["LOWER_AGE"].astype(int)

"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 161 entries, 0 to 160
Data columns (total 10 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 9   LOWER_AGE            161 non-null    int64  
dtypes: float64(5), int64(3), object(2)
memory usage: 12.7+ KB
None
"""

print(file)

print(file.info())


#quiz 3

x = [1,2,3]
y = x[1:]
print(y)

x = {'a': 1, 'b': 2}
x.update({'c': 3})
print(x)


x = {'a': 1, 'b': 2}
del x['a']
print(x)

"""Working with Dates

30-01-2024 British standard

01-30-2024 American

"""

df = pd.read_csv("data_02/time_series_data.csv", index_col=(0))


print(df.info())

# Convert the 'Date' column to datetime

df['Date'] = pd.to_datetime(df['Date'])

# Specify the format

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

print(df)

"""Split the 'Date' column into separate 
columns for year, month, and day
"""

df['Year'] =df['Date'].dt.year
df['Month'] =df['Date'].dt.month
df['Day'] =df['Date'].dt.day
print(df)


""".str
.estract
.astype
"""

df = pd.read_csv('data_02/patient_data_dates.csv',index_col=(0))


df['Date'] = pd.to_datetime(df['Date'])



#Remove the columns

df.drop(index=26, inplace=True)


#to remove the entire rows with a  NA observation


df.dropna(inplace=True)
print(df.info())

avg_cal = df['Calories'].mean()

df["Calories"].fillna(avg_cal,inplace = True)



#One way to fix wrong values is to

df.loc[7, 'Duration'] = 45

df['Duration'] = df['Duration'].replace([450],45)

df.reset_index()

pd.set_option('display.max_rows',None)


"""Applying Data Transformations


"""

df = pd.read_csv("data_02/iris.csv")

print(df.columns)


df["class"] = df["class"].str.replace("Iris-", "")

col_names=df.columns.tolist()

print(col_names)

df['sepal_length_sq'] = df['sepal_length']**2

df['sepal_length_sq'] = df['sepal_length'].apply(lambda x: x**2)

grouped = df.groupby('class')


mean_squared_values = grouped['sepal_length_sq'].mean()

print(mean_squared_values)

"""class
Iris-setosa        25.1818
Iris-versicolor    35.4972
Iris-virginica     43.7980
Name: sepal_length_sq, dtype: float64
"""

# Read the CSV files into dataframes
df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")


# Concatenate the dataframes
df = pd.concat([df1, df2], ignore_index=True)

###two tables with different column names but are related

df1 = pd.read_csv('data_02/person_education.csv')
df2 = pd.read_csv('data_02/person_work.csv')


## inner join
df_merge_ = pd.merge(df1,df2,on='id')


print(df_merge)

df_merge = pd.merge(df1, df2, on='id', how='outer')


"""Filtering"""


df = df[df['sepal_length'] > 5]

df = df[df['class'] == "virginica"]


"""LOAD"""


df.to_csv("output/pulsa.csv")
























