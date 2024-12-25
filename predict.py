from flask import Flask, request
import pickle
import pandas
import numpy 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/ping', methods=['GET'])
def pinger():
    return {"MESSAGE" : "Hello, I am Ping......!!!!!"}

model = open("./artefacts/classifier.pkl", "rb")
clf = pickle.load(model)

@app.route("/predict", methods=['POST'])
def prediction():
    loan_req = request.get_json()

    if loan_req['Gender'] == 'Male':
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == 'Unmarried':
        Married = 0
    else:
        Married = 1

    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1
    
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']


    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 1:
        pred = 'Approved'
    else:
        pred = 'Rejected'

    return {"loan_approval_status": pred}