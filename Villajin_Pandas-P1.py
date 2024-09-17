# Problem 1

# Declare panda data analysis library
import pandas as pd

# Load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('cars.csv')

# Display the first five rows of the resulting cars
print("First five rows of the cars data frame:")
print(cars.head())

# Display the last five rows of the resulting cars
print("\nLast five rows of the cars data frame:")
print(cars.tail())