import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# Checking pandas version
print(pd.__version__)

# Pandas Series
a = [1, 7, 2]

aSeries = pd.Series(a)
print(aSeries)
print(aSeries[0])

# Creating Labels

bSeries = pd.Series(a, index=['x', 'y', 'z'])
print(bSeries)

print(bSeries['x'])


# Key/Value Objects as Series

calories = {"day1": 420, "day2": 380, "day3": 390}

aKey = pd.Series(calories)

print(aKey)

# Create a Series using only data from "day1" and "day2"

bKey = pd.Series(calories, index=['day1', 'day2'])
print(bKey)

# DataFrames

data = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}

aDataFrame = pd.DataFrame(data)

print(aDataFrame)

# Locate Row

print(aDataFrame.loc[0])
print(aDataFrame.loc[[0, 1]])


# Named Indexes

bDataFrame = pd.DataFrame(data, index=['day1', 'day2', 'day3'])

print(bDataFrame)

# Locate Named Index

print(bDataFrame.loc['day2'])

# Load Files into DataFrame

aLoad = pd.read_csv('data.csv')

print(aLoad)

# Print the entire data set
print(aLoad.to_string())

# Max_rows

print(pd.options.display.max_rows)

# Set Max Rows

pd.options.display.max_rows = 9999

bLoad = pd.read_csv('data.csv')

print(bLoad)


# Read JSON

aJson = pd.read_json('data.json')

print(aJson.to_string())

# Dictionary as JSON

dataJson = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60,
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102,
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127,
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 289,
        "4": 401,
        "5": 388,
    }
}

bJson = pd.DataFrame(dataJson)

print(bJson.to_string())

# Pandas - Analyzing DataFrames

# head method
# Prints the first 5 rows of the DataFrame

print(aLoad.head())

# tail method
# Prints the last 5 rows of the DataFrame

print(aLoad.tail())

# info method
# Prints information about the DataFrame

print(aLoad.info())


# Pandas - Cleaning Empty Cells

df = pd.read_csv('newdata.csv')

new_df = df.dropna()

print(new_df.to_string())

df2 = pd.read_csv('newdata.csv')

df2.dropna(inplace=True)

print(df2.to_string())

# Replace Empty Values

df3 = pd.read_csv('newdata.csv')

df3.fillna(130, inplace=True)

print(df3.to_string())


# Replace only for a specific column

df4 = pd.read_csv('newdata.csv')

df4.fillna({'Calories': 130}, inplace=True)

print(df4.to_string())


# remove duplicates

print(df.duplicated())


# Pandas - Plotting

import matplotlib.pyplot as plt

dfPlot = pd.read_csv('data.csv')

dfPlot.plot()

plt.show()


# Scatter Plot

dfPlot.plot(kind='scatter', x='Duration', y='Calories')

plt.show()

# Histogram

dfPlot['Duration'].plot(kind= 'hist')

plt.show()




