# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 21:14:30 2024

@author: Elelwani
"""

import pandas as pd

df= pd.read_csv(".spyproject/movie_dataset.csv")
#print(df.info())


x= df["Revenue"].mean()
y= df['Metascore'].mean()

df["Revenue"].fillna(x,inplace= True)
df["Metascore"].fillna(y,inplace= True)
df.columns = df.columns.str.replace(' ', '_')
print(df)

print(df.describe())

##question1
Highest_rating= df.groupby("Rating")["Title"].max()
print(Highest_rating)
##answer1 (the dark knight)


##Question2
# Calculate the average of a specific column (e.g., 'Column1')
average_Revenue = df['Revenue'].mean()
print(average_Revenue)
##answer2(between 70-100 million )

#QUESTION3
avg2015_2017= df[(df["Year"]>=2015) &(df["Year"]<=2017)]["Revenue"].mean()
print(avg2015_2017)
#ANSWER3 (between 50 to 80 million)

##question4
data= df.groupby("Year")["Title"].count()
print(data)
##answer (297)

##question5
movie_director= df.groupby("Director")["Title"].count()
print(movie_director)
##answer (5)

##Question 6
rating_of_8= df[df["Rating"]>=8.0]["Title"]
print(rating_of_8)
#ANSWER FOR 6 IS EQUAL TO 78

#question 7
nolan_movie= df[df["Director"]=="Christopher Nolan"]
median_rating= nolan_movie["Rating"].median()
print(median_rating)
#answer 8.6

#question 8
avrg_rating_year= df.groupby("Year")["Rating"].mean()
year_highest_avg_rating= avrg_rating_year.max()
print(year_highest_avg_rating)
#answer=2007

#question 9
movie_made_2006=df[df["Year"]==2006].count()
movie_made_2016=df[df["Year"]==2016].count()
percentage_increase= ((movie_made_2016-movie_made_2006)/ movie_made_2006)*100
print(percentage_increase)

#answer i got 575

#question 10
all_actors = df['Actors'].str.split(', ', expand=True).stack().reset_index(drop=True)
most_common_actor = all_actors.mode()[0]
print(most_common_actor)
#ANSWER:Mark Wahlberg

#QUESTION11
genres = df['Genre'].str.split(', ', expand=True).stack().unique()
number_of_unique_genres = len(genres)
print(number_of_unique_genres)
##ANSWER 207

##QUESTION 12
cor_matric = df.corr()
print(cor_matric)


