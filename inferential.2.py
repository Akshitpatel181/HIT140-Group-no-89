import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, pearsonr 

# Load your datasets
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')

# Merging the datasets on 'ID'
data_full = pd.merge(pd.merge(dataset1, dataset2, on='ID'), dataset3, on='ID')

# Quick view of the data
print(data_full.head())

# Check for any missing data
print(data_full.isnull().sum())

# Filter the necessary columns: gender, screen time on weekends (S_we), and feeling cheerful (Cheer)
analysis_data = data_full[['gender', 'S_we', 'Cheer']].dropna()

# Separate data by gender
male_data = analysis_data[analysis_data['gender'] == 1]
female_data = analysis_data[analysis_data['gender'] == 0]

# Descriptive stats for males and females
print("Male Data (Screen Time on Weekends and Cheerfulness):")
print(male_data[['S_we', 'Cheer']].describe())

print("\nFemale Data (Screen Time on Weekends and Cheerfulness):")
print(female_data[['S_we', 'Cheer']].describe())

# Boxplot to visualize screen time on weekends (S_we) and cheerfulness (Cheer)
sns.boxplot(x='gender', y='Cheer', data=analysis_data)
plt.title('Cheerfulness by Gender')
plt.xlabel('Gender (1 = Male, 0 = Female)')
plt.ylabel('Cheerfulness Score')
plt.show()

# T-test to compare means of cheerfulness between males and females
t_stat, p_value = ttest_ind(male_data['Cheer'], female_data['Cheer'])

print(f"T-statistic: {t_stat}, P-value: {p_value}")
