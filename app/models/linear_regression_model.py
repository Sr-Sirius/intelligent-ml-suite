import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data/finance_data.csv", delimiter=";")
data.columns = data.columns.str.strip()

# Define inputs (X) and output (y)
X = data[["Income", "Previous_Expenses", "Transactions"]]
y = data["Expense"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)


# Prediction function
def predict_expense(income, previous_expenses, transactions):
    input_data = [[income, previous_expenses, transactions]]
    prediction = model.predict(input_data)
    return round(prediction[0], 2)