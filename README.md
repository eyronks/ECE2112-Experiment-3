# ECE2112 Programming Problems

This repository houses a set of Python scripts designed to solve a variety of programming problems for the ECE2112 course, with a particular focus on utilizing the Python Data Analysis library. These scripts provide practical solutions for performing efficient data analysis and manipulation. Below, you will find detailed descriptions of each script and its functionality within the context of data-driven problem solving.

<br> 

## Intended Learning Outcomes 

  1. To identify the codes and functions incorporated in the Pandas library.
  
  2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library.

<br> 

## Problem 1 

Using knowledge obtained from the experiment and demonstrations:

  * Load the corresponding .csv file into a data frame named cars using pandas
  * Display the first five and last five rows of the resulting cars.

<br>

## Step by Step Solution:

**Step 1: Import the necessary library for this problem:**

```python
# Declare panda data analysis library
import pandas as pd
```

<br>

**Step 2: Load the corresponding .csv file into a data frame named cars using pandas:**

 ```python
# Load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('cars.csv')
```

> We use the read_csv function from pandas to load the cars.csv file into a data frame named cars.

<br>

**Step 3: Display the first five rows of the resulting cars:**

```python
# Display the first five rows of the resulting cars
print("First five rows of the cars data frame:")
print(cars.head())
```

**Output:**

![Screenshot 2024-09-15 221243](https://github.com/user-attachments/assets/be513cb6-f3ca-46c7-9845-3b2e78e5b8d5)

> We use the head method to display the first five rows of the cars data frame.

<br>

**Step 4: Display the last five rows of the resulting cars:**

```python
# Display the last five rows of the resulting cars
print("\nLast five rows of the cars data frame:")
print(cars.tail())
```

**Output:**

![image](https://github.com/user-attachments/assets/2f47ad96-38e7-46e0-a711-2802f4611992)

> We use the tail method to display the last five rows of the cars data frame.

<br> 

## Discussion 

**Approach:** The approach used to solve the problem involves three key steps. Firstly, the necessary library, pandas, is imported to enable working with CSV files and data frames. Secondly, the read_csv function is utilized to load the cars.csv file into a data frame named cars. Finally, the head and tail methods are employed to display the first five and last five rows of the cars data frame, respectively.

<br>

**Functionality:** The approach is useful because it efficiently loads data into a flexible data structure, allows for quick data inspection, and sets the stage for further analysis and manipulation.

<br> 

## Problem 2

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
  * Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
  * Display the row that contains the ‘Model’ of ‘Mazda RX4’.
  * How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
  * Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

<br> 

## Step by Step Solution

**Step 1: Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.**

```python
print(cars.iloc[:, 1::2].head(5))
```

**Output:**

![image](https://github.com/user-attachments/assets/8a2aa883-beee-461b-b2c3-29b7ce8842a1)

> To achieve this, we can use slicing and indexing operations. Assuming the column indices start from 0, we can select the odd-numbered columns using iloc and then select the first five rows using slicing.

<br>

**Step 2: Display the row that contains the ‘Model’ of ‘Mazda RX4’**

```python
print(cars[cars['Model'] == 'Mazda RX4'])
```

<br>

**Output:**

![image](https://github.com/user-attachments/assets/ae6ecb53-4e49-47b5-b616-9d5ee85af916)

> We can use boolean indexing to select the row where the 'Model' column is 'Mazda RX4'.

<br>

**Step 3: Display the amount of cylinders (‘cyl’) the car model ‘Camaro Z28’ have**

```python
print(cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0])
```

**Output:** 

8

> Similar to the previous question, we can use boolean indexing to select the row where the 'Model' column is 'Camaro Z28' and then access the 'cyl' column.

<br>

**Step 4: Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.**

```python
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(models), ['cyl', 'gear']])
```

**Output:**

![image](https://github.com/user-attachments/assets/2ac0e749-794f-40c7-8469-5954fc534c80)

> We can use boolean indexing to select the rows where the 'Model' column is in the list of desired models, and then access the 'cyl' and 'gear' columns.

<br/>

## Discussion

**Approach:** To extract specific data from a Pandas dataframe, one can employ various subsetting, slicing, and indexing operations. Slicing allows one to select specific rows and columns using iloc or loc. Boolean indexing enables one to filter rows based on conditions, and the isin method allows one to select rows where a column is in a list of desired values. These operations can be combined to efficiently extract the required information from the dataframe.

<br>

**Functionality:** This approach is useful because it allows for efficient and flexible data extraction from Pandas dataframes. By combining subsetting, slicing, and indexing operations, users can quickly and precisely retrieve specific data, filter out unwanted information, and manipulate their data to meet their analysis needs

<br>

##

**Author:** Aaron Chastine V. Villajin

**Submitted to:** Engr. Ma. Madecheen S. Pangaliman, M.Sc.











