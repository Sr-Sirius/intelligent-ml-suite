from flask import Blueprint, render_template

regression = Blueprint("regression", __name__)

@regression.route("/")
def info():
    return render_template("regression/info.html")

@regression.route("/predict")
def predict():
    return render_template("regression/predict.html")