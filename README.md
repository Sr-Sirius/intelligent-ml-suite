#  Intelligent ML Suite

This is a professional Flask-based web application that demonstrates core Machine Learning concepts through real-world scenarios, including regression and classification models.

---

##  Project Overview

This project was developed as part of a Machine Learning course to showcase:

- Practical implementation of supervised learning models
- Clean and scalable Flask architecture
- Real-world datasets and predictions
- Interactive user interface for model testing

---

##  Implemented Models

###  Linear Regression (Finance)
- Predicts expenses based on:
  - Income
  - Previous expenses
  - Number of transactions

---

###  Logistic Regression (Car Risk Prediction)
- Predicts accident risk level based on:
  - Average speed
  - Number of trips
  - Driving time
- Includes:
  - Confusion Matrix
  - ROC Curve
  - Accuracy, Precision, Recall, F1-score

---

###  Bernoulli Naive Bayes (Driver Behavior Classification)
- Classifies driver risk using binary features:
  - Overspeeding
  - Night driving
  - Phone usage
  - Aggressive braking
- Includes:
  - Confusion Matrix
  - ROC Curve
  - Evaluation metrics

---

##  Features

- Interactive web interface built with Flask
- Modular architecture (routes, models, services)
- Realistic datasets (1000+ records)
- Data visualization using Matplotlib
- Clean UI with theme-based design
- Multiple ML use cases (Finance, Healthcare, Cars, Fraud Detection)

---

##  Tech Stack

- Python
- Flask
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

---

##  Project Structure


---

##  Installation & Setup

1. Clone the repository

bash
git clone git@github.com:YOUR-USER/intelligent-ml-suite.git
cd intelligent-ml-suite
________________________________________
2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate
________________________________________
3. Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
________________________________________
4. Run the application
python run.py
________________________________________
 
 Dataset Information
Datasets used in this project:
•	Custom dataset (Linear Regression) 
•	realistic dataset (Logistic Regression) 
•	Binary behavioral dataset (Naive Bayes) 
with data (records) from kaggle and minor adjustments to show that the model is actually working
All datasets include:
•	Proper feature selection 
•	Balanced classes 
•	Noise to simulate real-world scenarios 
________________________________________

 Evaluation Metrics
All classification models include:
•	Accuracy 
•	Precision 
•	Recall 
•	F1-score 
•	Confusion Matrix 
•	ROC Curve (AUC) 
________________________________________
 
 Git Workflow
•	Feature multiple branches: 
o	feature/logistic-regression 
o	feature/bernoulli-naive-bayes 
•	Pull Requests used for merging 
•	Incremental commits to demonstrate progress 
________________________________________

 Author
Developed by:
Mike and Brayan — Systems Engineering Students
________________________________________

 Final Notes
This project demonstrates not only Machine Learning implementation but also:
•	Clean code practices 
•	Scalable architecture 
•	Professional development workflow 
