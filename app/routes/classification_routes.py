from flask import Blueprint, render_template, request

from app.models.classification.logistic_model import (
    predict_risk,
    evaluate_model,
    plot_confusion_matrix,
    plot_roc
)

classification_bp = Blueprint("classification", __name__)


# Logistic Regression - Concepts
@classification_bp.route("/logistic/concepts")
def logistic_concepts():
    return render_template(
        "ml/classification/logistic/concepts.html",
        theme="cars"
    )


# Logistic Regression - Application
@classification_bp.route("/logistic/application", methods=["GET", "POST"])
def logistic_application():

    prediction = None
    probability = None

    accuracy = precision = recall = f1 = None
    cm_plot = roc_plot = None

    if request.method == "POST":
        speed = float(request.form["speed"])
        trips = float(request.form["trips"])
        time = float(request.form["time"])

        prediction, probability = predict_risk(speed, trips, time)

    # Always calculate metrics (for display)
    accuracy, precision, recall, f1, y_test, y_pred = evaluate_model()

    cm_plot = plot_confusion_matrix(y_test, y_pred)
    roc_plot = plot_roc()

    return render_template(
        "ml/classification/logistic/application.html",
        prediction=prediction,
        probability=probability,
        accuracy=round(accuracy, 2),
        precision=round(precision, 2),
        recall=round(recall, 2),
        f1=round(f1, 2),
        cm_plot=cm_plot,
        roc_plot=roc_plot,
        theme="cars"
)


# Naive Bayes - Concepts
@classification_bp.route("/naive-bayes/concepts")
def nb_concepts():
    return render_template(
        "ml/classification/naive_bayes/concepts.html",
        theme="cars"
    )


# Naive Bayes - Application
@classification_bp.route("/naive-bayes/application")
def nb_application():
    return render_template(
        "ml/classification/naive_bayes/application.html",
        theme="cars"
    )