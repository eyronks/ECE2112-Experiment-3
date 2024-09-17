# Problem 2

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

# Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
print(cars.iloc[:, 1::2].head(5))

# Display the row that contains the ‘Model’ of ‘Mazda RX4’
print(cars[cars['Model'] == 'Mazda RX4'])

# Display the amount of cylinders (‘cyl’) the car model ‘Camaro Z28’ have.
print(cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0])

# Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(models), ['cyl', 'gear']])