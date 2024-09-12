import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Step 1: Load the datasets (Make sure to provide correct paths for your CSV files)
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')

# Step 2: Merge the datasets on the 'ID' column
merged_data = pd.merge(pd.merge(dataset1, dataset2, on='ID'), dataset3, on='ID')

# Step 3: Create the total screen time variable (sum of weekend and weekday screen time)
merged_data['Total_screen_time'] = merged_data[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].sum(axis=1)

# Step 4: Define the independent variable (Total_screen_time) and dependent variable (well-being indicator - Optimism)
X = merged_data[['Total_screen_time']]
y = merged_data['Optm']  # We're predicting the 'Optimism' well-being indicator

# Step 5: Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Fit the linear regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Step 7: Make predictions on the testing data
y_pred = lr_model.predict(X_test)

# Step 8: Evaluate the model (R-squared score)
r2 = r2_score(y_test, y_pred)

# Step 9: Display the regression coefficient, intercept, and R-squared value
coefficients = lr_model.coef_
intercept = lr_model.intercept_

print(f"R-squared value: {r2}")
print(f"Regression Coefficient: {coefficients[0]}")
print(f"Intercept: {intercept}")

# Step 10: Plot the actual vs predicted values of optimism
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Values')
plt.plot(X_test, y_pred, color='red', label='Regression Line')

# Step 11: Adding labels and title
plt.xlabel('Total Screen Time')
plt.ylabel('Optimism Score')
plt.title('Linear Regression: Total Screen Time vs Optimism')
plt.legend()

# Step 12: Display the plot
plt.show()