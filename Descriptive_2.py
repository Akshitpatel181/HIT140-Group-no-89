import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
df1 = pd.read_csv('dataset1.csv')  # Replace with the correct path to dataset1.csv
df2 = pd.read_csv('dataset2.csv')  # Replace with the correct path to dataset2.csv
df3 = pd.read_csv('dataset3.csv')  # Replace with the correct path to dataset3.csv

# Calculate the mode for key variables in each dataset
# For df1 (gender)
mode_gender = df1['gender'].mode()[0]

# For df2 (computer use on weekends)
mode_computer_we = df2['C_we'].mode()[0]

# For df3 (optimism)
mode_optimism = df3['Optm'].mode()[0]

# Print the modes with interpretation
print(f"Mode for Gender (DF1): {mode_gender} (1 = Male, 0 = Other)")
print(f"Mode for Computer Use on Weekends (DF2): {mode_computer_we} hours")
print(f"Mode for Optimism (DF3): {mode_optimism} (1 = None of the time, 5 = All of the time)")

# Plot bar charts for visualizing the distributions and the mode
plt.figure(figsize=(15, 5))

# Bar chart for df1 (Gender)
plt.subplot(1, 3, 1)
gender_counts = df1['gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values, color='skyblue')
plt.axvline(mode_gender, color='r', linestyle='dashed', linewidth=2, label=f'Mode: {mode_gender}')
plt.title('Gender Distribution (DF1)')
plt.xlabel('Gender (1 = Male, 0 = Other)')
plt.ylabel('Count')
plt.xticks([0, 1])  # Ensure ticks show 0 and 1 for gender
for i in range(len(gender_counts)):
    plt.text(gender_counts.index[i], gender_counts.values[i], str(gender_counts.values[i]), ha='center', va='bottom')
plt.legend()

# Bar chart for df2 (Computer use on weekends)
plt.subplot(1, 3, 2)
computer_we_counts = df2['C_we'].value_counts().sort_index()
plt.bar(computer_we_counts.index, computer_we_counts.values, color='lightgreen')
plt.axvline(mode_computer_we, color='r', linestyle='dashed', linewidth=2, label=f'Mode: {mode_computer_we}')
plt.title('Computer Use on Weekends (DF2)')
plt.xlabel('Hours')
plt.ylabel('Count')
for i in range(len(computer_we_counts)):
    plt.text(computer_we_counts.index[i], computer_we_counts.values[i], str(computer_we_counts.values[i]), ha='center', va='bottom')
plt.legend()

# Bar chart for df3 (Optimism)
plt.subplot(1, 3, 3)
optimism_counts = df3['Optm'].value_counts().sort_index()
plt.bar(optimism_counts.index, optimism_counts.values, color='lightcoral')
plt.axvline(mode_optimism, color='r', linestyle='dashed', linewidth=2, label=f'Mode: {mode_optimism}')
plt.title('Optimism (DF3)')
plt.xlabel('Optimism Score (1-5)')
plt.ylabel('Count')
for i in range(len(optimism_counts)):
    plt.text(optimism_counts.index[i], optimism_counts.values[i], str(optimism_counts.values[i]), ha='center', va='bottom')
plt.legend()

plt.tight_layout()
plt.show()

