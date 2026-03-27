from flask import Blueprint, render_template, request
from app.models.linear_regression_model import predict_expense

regression_bp = Blueprint('regression', __name__)

@regression_bp.route('/')
def regression_home():
    return render_template('regression/info.html')


@regression_bp.route('/predict', methods=['GET', 'POST'])
def predict():

    prediction = None
    warning = None

    if request.method == 'POST':
        income = float(request.form['income'])
        previous = float(request.form['previous_expenses'])
        transactions = float(request.form['transactions'])

        # Validation
        if previous > income:
            warning = "Warning: Previous expenses are higher than income. Prediction may be inaccurate."

        prediction = predict_expense(income, previous, transactions)

    return render_template(
        'regression/predict.html',
        prediction=prediction,
        warning=warning
    )