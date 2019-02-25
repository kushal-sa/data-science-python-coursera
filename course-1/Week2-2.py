####### DataFrame #########

# 2-dimensional datastructure
# Can be though of as a table with indexed-rows ( indexes can be either integers or strings like in series )
# Can also be thought of as a 2-axis labelled array

import pandas as pd

purchase_1 = pd.Series({
		'Name': 'Kushal',
		'Purchase': 'iPad'
	})

purchase_2 = pd.Series({
		'Name': 'Samiksa',
		'Purchase': 'Tablet'
	})

purchase_3 = pd.Series({
		'Name': 'Thamtham',
		'Purchase': 'Mouse'
	})

s = pd.DataFrame([purchase_1,purchase_2,purchase_3], index = ['store1', 'store1', 'store3'])

print(type(s.iloc[1])) # pd.Series type
print(type(s['Name'])) # pd.Series type
print(type(s.loc['store1'])) # pd.DataFrame type because multiple entries exist with that indexing

# Selecting columns and rows
print(s.loc['store3', ['Purchase']])

# Note: iloc and loc are reserved for row selection

# Transpose the dataframe
s.T

# Note: Chaining is slow as it creates a copy of the selected part. AVOID
# Dropping a row or column, inplace and 

s.drop('store1') # returns a copy with the rows dropped

# ADding new columns is easy
s['New Column'] = None # sets all rows with this default value
print(s)

# Updating a column
s['New Column'] = pd.Series(['A1','A2','A3'], index = ['store1','store1','store3'])
print(s)

####### Dataframe Indexing and Loading ##########

# NOTE: Ambiguity around when we have references and when we have copy, when dataframes are being manipulated

# Pandas dataframes provide us the ability to directly read csv in the format we want to

s.rename(columns={'New Column':'Grade'}, inplace = True)
print(s)