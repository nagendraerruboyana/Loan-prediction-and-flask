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
├── dockerfile              # Docker configuration for containerized deployment
├── task-definition.json    # ECS Task Definition for deploying on AWS
└── test_predict.py         # Unit tests for prediction logic
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
   - Integrated with Docker for easy deployment in isolated environments.

3. **Deployment**
   - The Flask app is deployed for local usage and has been containerized using Docker for easier deployment on cloud platforms like AWS or Heroku.
   - **AWS ECS Task Definition** for easy deployment on AWS services.

4. **CI/CD with GitHub Actions**
   - This repository includes a **GitHub Actions** workflow to automate testing and deployment.
   - The workflow performs the following:
     - **Tests the application** by running unit tests located in `test_predict.py`.
     - **Deploys the application** to AWS using ECS and ECR after successful tests.
     - Ensures that the Docker image is built, pushed to ECR, and the ECS task definition is updated.

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

4. **Optional**: Build and run the Docker container for isolated environment setup:
   ```bash
   docker build -t loan-prediction .
   docker run -p 5000:5000 loan-prediction
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

3. **Running Tests**
   - Run unit tests for prediction logic:
     ```bash
     pytest test_predict.py
     ```

## GitHub Actions Workflow
This repository includes a GitHub Actions workflow (`.github/workflows/automate_actions.yml`) that automates the following processes:

1. **Testing**: Runs unit tests located in `test_predict.py` to ensure the correctness of the application logic.
   
2. **Deployment**: 
   - Builds a Docker image and pushes it to Amazon Elastic Container Registry (ECR).
   - Updates the Amazon ECS task definition and deploys the image to ECS for running the application in production.

   This process is triggered on any push to the `main` branch.

## File Descriptions
- **artefacts/**
  - Contains the trained model saved in `.pkl` format and other related files.

- **data/**
  - Includes datasets for training, testing, and validation.

- **predict.py**
  - Main script for handling predictions and running the Flask application.

- **requirements.txt**
  - Lists Python dependencies required for the project.

- **dockerfile**
  - Contains the instructions for building the Docker image for containerized deployment.

- **task-definition.json**
  - AWS ECS Task Definition for deploying the application on AWS cloud.

- **test_predict.py**
  - Unit tests for prediction logic.

## Future Enhancements
- Extend the app with additional features like applicant history and feedback mechanism.
- Deploy the application on cloud platforms like AWS, Azure, or Heroku for public access.

## Acknowledgments
- This project is inspired by real-world loan prediction use cases and serves as a demonstration of my skills in machine learning, Flask development, and application deployment.