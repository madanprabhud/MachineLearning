# importing pandas package 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("day.csv") 

# generating one row 
row1 = data.sample(n = 1) 

# display 
print(row1) 

# generating another row 
row2 = data.sample(n = 1) 

# display 
print(row2) 
