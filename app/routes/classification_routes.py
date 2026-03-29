from flask import Blueprint, render_template

classification_bp = Blueprint(
    "classification",
    __name__
)

# Logistic Regression - Concepts
@classification_bp.route("/logistic/concepts")
def logistic_concepts():
    return render_template(
        "ml/classification/logistic/concepts.html",
        theme="ml"
    )


# Logistic Regression - Application
@classification_bp.route("/logistic/application")
def logistic_application():
    return render_template(
        "ml/classification/logistic/application.html",
        theme="ml"
    )

# Naive Bayes - Concepts
@classification_bp.route("/naive-bayes/concepts")
def nb_concepts():
    return render_template(
        "ml/classification/naive_bayes/concepts.html",
        theme="ml"
    )


# Naive Bayes - Application
@classification_bp.route("/naive-bayes/application")
def nb_application():
    return render_template(
        "ml/classification/naive_bayes/application.html",
        theme="ml"
    )