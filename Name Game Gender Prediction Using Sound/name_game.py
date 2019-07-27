import fuzzy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

first_name =[]

#reading data from the dataset and 
# extracting first names of the authors

author_df = pd.read_csv('datasets/nytkids_yearly.csv',delimiter=';')
for name in author_df['Author']:
    lst = name.split(' ')
    first_name.append(lst[0])

# adding a new column to the dataset
author_df["first_name"] = first_name
author_df.head()

# Looping through author's first names to create the nysiis (fuzzy) equivalent
nysiis_name = []
for i in (first_name):
    nysiis_name.append(fuzzy.nysiis(i))
    
author_df["nysiis_name"] = nysiis_name
unique_fn = len(np.unique(author_df['first_name']))
unique_nys = len(np.unique(author_df['nysiis_name']))
print(unique_fn - unique_nys)

babies_df = pd.read_csv('datasets/babynames_nysiis.csv',delimiter=';')
#print(babies_df.head())
gender = []
for index, row in babies_df.iterrows():
    if row[1]> row[2]:
        gender.append('F')
    elif row[1] < row[2]:
        gender.append('M')
    else:
        gender.append('N')
  
babies_df['gender'] = gender
babies_df.head()

# This function returns the location of an element in a_list.
# Where an item does not exist, it returns -1.
def locate_in_list(a_list, element):
    loc_of_name = a_list.index(element) if element in a_list else -1
    return(loc_of_name)

# Looping through author_df['nysiis_name'] and appending the gender of each
# author to author_gender.
author_gender = []
for name in author_df['nysiis_name']:
    lst = list(babies_df['babynysiis'])
    index = locate_in_list(lst, name)
    if index > -1:
        author_gender.append(list(babies_df['gender'])[index])
    else:
        author_gender.append('Unknown')

# Adding author_gender to the author_df
author_df['author_gender'] = author_gender

# Counting the author's genders
author_df['author_gender'].value_counts()

# Creating a list of unique years, sorted in ascending order.
years = sorted(author_df["Year"].unique())

# Initializing lists
males_by_yr = []
females_by_yr = []
unknown_by_yr = []

# Looping through years to find the number of male, female and unknown authors per yea

for year in years:
    df = author_df[author_df['Year'] == year]
    males_by_yr.append(len( df[ df['author_gender'] == 'M' ]))
    females_by_yr.append(len( df[ df['author_gender'] =='F' ]))
    unknown_by_yr.append(len( df[ df['author_gender'] =='Unknown' ]))
        

# Printing out yearly values to examine changes over time
print(males_by_yr, females_by_yr, unknown_by_yr)

# This makes plots appear in the notebook
%matplotlib inline

# Plotting the bar chart
plt.bar(years, unknown_by_yr, color = "green")
plt.title("Unidentified Genders of Authors Per Year")
plt.xlabel("Year")
plt.ylabel("Unknown Genders")

# Creating a new list, where 0.25 is added to each year
ys = []
for i in (years):
    new = i + 0.25
    ys.append(new)
years_shifted = ys

#Plotting males_by_yr by year
#plt.bar(x = years, height = males_by_yr, width = 0.5, color='yellow')

# Plotting females_by_yr by years_shifted
#plt.bar(x = years_shifted, height=females_by_yr, width = 0.5, color='pink')

#plt.title("Male & Female Authors Per Year")
#plt.xlabel("Year")
#plt.ylabel("Distribution")"""
