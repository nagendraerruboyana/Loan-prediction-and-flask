# Loan Prediction Application

## Overview
This repository, **Loan-prediction-and-flask**, contains the implementation of a Loan Prediction web application built using Flask. The application predicts the likelihood of loan approval based on key applicant details such as gender, marital status, income, loan amount, and credit history. This project is part of my portfolio to showcase skills in data preprocessing, machine learning, and web application deployment.

## Repository Structure

```
Loan-prediction-and-flask/
|
├── artefacts/              # Contains model training files and serialized model (pkl files)
├── data/                   # Contains training, testing, and validation datasets
├── .gitattributes          # Specifies text file encoding rules for Git
├── .gitignore              # Specifies intentionally untracked files to ignore
├── README.md               # Project documentation (this file)
├── predict.py              # Script to handle predictions using the Flask app
├── requirements.txt        # Lists required Python packages
```

## Features
1. **Model Training**
   - Logistic Regression is used as the predictive model.
   - Training data includes variables like:
     - **Gender**
     - **Married**
     - **ApplicantIncome**
     - **LoanAmount**
     - **Credit_History**
     
2. **Web Application**
   - Built using Flask framework.
   - Provides an interactive interface for users to input details and get loan approval predictions.

3. **Deployment**
   - The Flask app is deployed for local usage.

## Dataset
The dataset used for this application contains applicant information and loan details. Key input features include:
- **Gender**: Male/Female
- **Married**: Yes/No
- **ApplicantIncome**: Applicant's income
- **LoanAmount**: Requested loan amount
- **Credit_History**: 1 (good credit history) or 0 (poor credit history)

Other features in the dataset are predefined and not required as inputs for the prediction model.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Loan-prediction-and-flask.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Loan-prediction-and-flask
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Model Training**
   - The logistic regression model has been trained and saved as a `.pkl` file in the `artefacts` folder.
   - If retraining is needed, use the training scripts included in the repository.

2. **Running the Application**
   - Start the Flask app:
     ```bash
     python predict.py
     ```
   - Access the app on `http://127.0.0.1:5000/` in your web browser.
   - Input the required details to get loan predictions.

## File Descriptions
- **artefacts/**
  - Contains the trained model saved in `.pkl` format and other related files.

- **data/**
  - Includes datasets for training, testing, and validation.

- **predict.py**
  - Main script for handling predictions and running the Flask application.

- **requirements.txt**
  - Lists Python dependencies required for the project.

- **README.md**
  - Documentation for the project (this file).

## Future Enhancements
- Extend the app with additional features like applicant history and feedback mechanism.
- Deploy the application on cloud platforms like AWS, Azure, or Heroku for public access.

## Acknowledgments
- This project is inspired by real-world loan prediction use cases and serves as a demonstration of my skills in machine learning, Flask development, and application deployment.


