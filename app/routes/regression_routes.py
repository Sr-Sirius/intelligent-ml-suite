from flask import Blueprint, render_template, request
from app.models.linear_regression_model import predict_expense

regression_bp = Blueprint('regression', __name__)

@regression_bp.route('/')
def regression_home():
    return render_template('regression/info.html')


@regression_bp.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None

    if request.method == 'POST':
        income = float(request.form['income'])
        previous_expenses = float(request.form['previous_expenses'])
        transactions = float(request.form['transactions'])

        prediction = predict_expense(income, previous_expenses, transactions)

    return render_template('regression/predict.html', prediction=prediction)