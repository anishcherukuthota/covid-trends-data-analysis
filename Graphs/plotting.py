import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def graph(formula, x_range, str):
    x = np.array(x_range)
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)
    plt.xlabel("Age (Years)")
    plt.ylabel("Income (Millions of Dollars)")
    plt.title("Age vs Projected Annual Income" + str)
    plt.xticks(np.arange(0, 100, 20))
    plt.show()

# Create pandas dataframe from data file and split it into independent variable (age) and dependent variable (income)
df = pd.read_csv("/home/anish/PycharmProjects/asdrp/Data/final_data.csv", low_memory=False)
x = df['Age']
y = df['Income']

# Plot age vs income for all individuals
plt.scatter(x, y, s=4)
plt.xlabel("Age (Years)")
plt.ylabel("Income (Millions of Dollars)")
plt.title("Age vs Annual Income")
plt.xticks(np.arange(0, 100, 20))
plt.show()
coeff = np.polyfit(x, y, 2)
graph(lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2], np.arange(0, 100.1, 0.1), "")

#####################################################################################################################

# Create lists for age data and income data of individuals by ethnicity
white_age = []
white_income = []
black_age = []
black_income = []
asian_age = []
asian_income = []
hispanic_age = []
hispanic_income = []
na_age = []
na_income = []
mixed_age = []
mixed_income = []

# Open data file and go through each line of data, storing the age and income data in the corresponding lists
with open("/home/anish/PycharmProjects/asdrp/Data/final_data.csv") as file:
    next(file)
    for line in file:
        line = line.strip()
        data = line.split(",")
        if int(data[2]) == 0:
            white_age.append(int(data[1]))
            white_income.append(float(data[4]))
        elif int(data[2]) == 1:
            black_age.append(int(data[1]))
            black_income.append(float(data[4]))
        elif int(data[2]) == 2:
            asian_age.append(int(data[1]))
            asian_income.append(float(data[4]))
        elif int(data[2]) == 3:
            hispanic_age.append(int(data[1]))
            hispanic_income.append(float(data[4]))
        elif int(data[2]) == 4:
            na_age.append(int(data[1]))
            na_income.append(float(data[4]))
        elif int(data[2]) == 5:
            mixed_age.append(int(data[1]))
            mixed_income.append(float(data[4]))

# Plot age vs income for all individuals by ethnicity
x = np.array(white_age)
y = np.array(white_income)
plt.scatter(x, y, s=4)
plt.xlabel("Age (Years)")
plt.ylabel("Income (Millions of Dollars)")
plt.title("Age vs Annual Income of White Individuals")
plt.xticks(np.arange(0, 100, 20))
plt.show()
coeff = np.polyfit(x, y, 2)
graph(lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2], np.arange(0, 100.1, 0.1), " of White Individuals")

x = np.array(black_age)
y = np.array(black_income)
plt.scatter(x, y, s=4)
plt.xlabel("Age (Years)")
plt.ylabel("Income (Millions of Dollars)")
plt.title("Age vs Annual Income of Black Individuals")
plt.xticks(np.arange(0, 100, 20))
plt.show()
coeff = np.polyfit(x, y, 2)
graph(lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2], np.arange(0, 100.1, 0.1), " of Black Individuals")

x = np.array(asian_age)
y = np.array(asian_income)
plt.scatter(x, y, s=4)
plt.xlabel("Age (Years)")
plt.ylabel("Income (Millions of Dollars)")
plt.title("Age vs Annual Income of Asian Individuals")
plt.xticks(np.arange(0, 100, 20))
plt.show()
coeff = np.polyfit(x, y, 2)
graph(lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2], np.arange(0, 100.1, 0.1), " of Asian Individuals")

x = np.array(hispanic_age)
y = np.array(hispanic_income)
plt.scatter(x, y, s=4)
plt.xlabel("Age (Years)")
plt.ylabel("Income (Millions of Dollars)")
plt.title("Age vs Annual Income of Hispanic Individuals")
plt.xticks(np.arange(0, 100, 20))
plt.show()
coeff = np.polyfit(x, y, 2)
graph(lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2], np.arange(0, 100.1, 0.1), " of Hispanic Individuals")

x = np.array(na_age)
y = np.array(na_income)
plt.scatter(x, y, s=4)
plt.xlabel("Age (Years)")
plt.ylabel("Income (Millions of Dollars)")
plt.title("Age vs Annual Income of Native American Individuals")
plt.xticks(np.arange(0, 100, 20))
plt.show()
coeff = np.polyfit(x, y, 2)
graph(lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2], np.arange(0, 100.1, 0.1), " of Native American Individuals")

x = np.array(mixed_age)
y = np.array(mixed_income)
plt.scatter(x, y, s=4)
plt.xlabel("Age (Years)")
plt.ylabel("Income (Millions of Dollars)")
plt.title("Age vs Annual Income of Mixed Individuals")
plt.xticks(np.arange(0, 100, 20))
plt.show()
coeff = np.polyfit(x, y, 2)
graph(lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2], np.arange(0, 100.1, 0.1), " of Mixed Individuals")

########################################################################################################################

# Create lists for age data and income data of individuals by gender
male_age = []
male_income = []
female_age = []
female_income = []

# Open data file and go through each line of data, storing the age and income data in the corresponding lists
with open("/home/anish/PycharmProjects/asdrp/Data/final_data.csv") as file:
    next(file)
    for line in file:
        line = line.strip()
        data = line.split(",")
        if int(data[0]) == 0:
            male_age.append(int(data[1]))
            male_income.append(float(data[4]))
        elif int(data[0]) == 1:
            female_age.append(int(data[1]))
            female_income.append(float(data[4]))

# Plot age vs income for all individuals by gender

x = np.array(male_age)
y = np.array(male_income)
plt.scatter(x, y, s=4)
plt.xlabel("Age (Years)")
plt.ylabel("Income (Millions of Dollars)")
plt.title("Age vs Annual Income of Men")
plt.xticks(np.arange(0, 100, 20))
plt.show()
coeff = np.polyfit(x, y, 2)
graph(lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2], np.arange(0, 100.1, 0.1), " of Men")

x = np.array(female_age)
y = np.array(female_income)
plt.scatter(x, y, s=4)
plt.xlabel("Age (Years)")
plt.ylabel("Income (Millions of Dollars)")
plt.title("Age vs Annual Income of Women")
plt.xticks(np.arange(0, 100, 20))
plt.show()
coeff = np.polyfit(x, y, 2)
graph(lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2], np.arange(0, 100.1, 0.1), " of Women")