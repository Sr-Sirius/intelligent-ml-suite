import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import io
import base64


def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    # Go ONE MORE LEVEL UP to reach project root
    project_root = os.path.dirname(base_dir)

    file_path = os.path.join(project_root, "data", "car_risk_data.csv")

    data = pd.read_csv(file_path, delimiter=";")

    X = data[['speed', 'trips', 'time']]
    y = data['risk']

    return train_test_split(X, y, test_size=0.3, random_state=42)


def train_model():
    X_train, X_test, y_train, y_test = load_data()

    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model, X_test, y_test


def predict_risk(speed, trips, time):
    model, _, _ = train_model()

    proba = model.predict_proba([[speed, trips, time]])[0][1]
    prediction = model.predict([[speed, trips, time]])[0]

    label = "High Risk" if prediction == 1 else "Low Risk"

    return label, round(proba, 4)

def evaluate_model():
    model, X_test, y_test = train_model()

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return accuracy, precision, recall, f1, y_test, y_pred

def plot_confusion_matrix(y_test, y_pred):
    import seaborn as sns

    cm = confusion_matrix(y_test, y_pred)

    labels = [
        ["True Neg\n(TN)", "False Pos\n(FP)"],
        ["False Neg\n(FN)", "True Pos\n(TP)"]
    ]

    plt.figure(figsize=(6,5))

    sns.heatmap(
        cm,
        annot=labels,
        fmt="",
        cmap="Blues",
        xticklabels=["Low Risk", "High Risk"],
        yticklabels=["Low Risk", "High Risk"]
    )

    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")
    plt.title("Confusion Matrix")

    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()

    return base64.b64encode(buf.getvalue()).decode()

def plot_roc(y_test, y_prob):
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(6,5))

    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}", linewidth=2)
    plt.plot([0,1], [0,1], linestyle='--')  # random baseline

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")

    plt.legend(loc="lower right")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()

    return base64.b64encode(buf.getvalue()).decode()