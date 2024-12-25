from predict import app
import pytest

@pytest.fixture
def client():
    return app.test_client()


def test_pinger(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"MESSAGE" : "Hello, I am Ping......!!!!!"}

def test_predict(client):
    test_data = {
    "Gender" : "Male",
    "Married": "Unmaried",
    "ApplicantIncome" : 50000,
    "LoanAmount" : 5000,
    "Credit_History" : "Cleared Debts"
    }

    resp = client.post('/predict', json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status" : "Rejected"}