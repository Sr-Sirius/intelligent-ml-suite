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
    cm = confusion_matrix(y_test, y_pred)

    fig, ax = plt.subplots()
    ax.matshow(cm)

    for i in range(len(cm)):
        for j in range(len(cm)):
            ax.text(j, i, cm[i, j], ha='center', va='center')

    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()

    return base64.b64encode(buf.getvalue()).decode()

def plot_roc():
    model, X_test, y_test = train_model()

    y_prob = model.predict_proba(X_test)[:,1]

    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    ax.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()

    return base64.b64encode(buf.getvalue()).decode()