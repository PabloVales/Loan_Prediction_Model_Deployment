# Deployment of a machine learning model

The objective of this project is to showcase the deployment of a machine learning model. Such model is based on a binary classification that predicts whether a client will be given a loan. Since the main objective is the deployment itself, the approach taken for this classification is a simple one based on a logistic regression model and optimized with recursive feature elimination (RFE). The deployed web-app can be found here: https://loan-prediction-webapp.herokuapp.com/

# Content

A loan application is used by borrowers to apply for a loan. Through the loan application, borrowers reveal key details about their finances to the lender. The loan application is crucial to determining whether the lender will grant the request for funds or credit.

# Problem statement and objective

A bank's filtering process to reject or approve a loan can be a time consuming and tedious process. Therefore, the idea behind this ML project is to build an ML model and web application that the bank can use to classify if a user can be granted a loan or not. 

# Dataset information

The dataset contains information about Loan Applicants. There are 12 independent columns and 1 dependent column. This dataset includes attributes like Loan ID, gender, if the loan applicant is married or not, the level of education, applicant’s income etc.

The training dataset can be downloaded by typing the following line in the Jupyter Notebook (importing pandas as pd):

```
loan_data  = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Loan_Data/loan_train.csv" )

```

Test dataset can be downloaded with the following line of code (importing pandas as pd):

```
test_data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/Loan_Data/loan_test.csv')

```

## Feature information:

1. Loan_ID: A unique ID assigned to every loan applicant
2. Gender: Gender of the applicant (Male, Female)
3. Married: The marital status of the applicant (Yes, No)
4. Dependents: No. of people dependent on the applicant (0,1,2,3+)
5. Education: Education level of the applicant (Graduated, Not Graduated)
6. Self_Employed: If the applicant is self-employed or not (Yes, No)
7. ApplicantIncome: The amount of income the applicant earns
8. CoapplicantIncome: The amount of income the co-applicant earns
9. LoanAmount: The amount of loan the applicant has requested for
10. Loan_Amount_Term: The  no. of days over which the loan will be paid
11. Credit_History: A record of a borrower's responsible repayment of debts (1- has all debts paid, 0- not paid)
12. Property_Area : The type of location where the applicant’s property lies (Rural, Semiurban, Urban)

Target: 

13. Loan_Status: Loan granted or not (1 for granted, 0 for not granted)

# Model

Model based on logistic regression with recursive feature elimination (RFE) for a binary classification (loan approved or rejected) with an accuracy of 89%. The code for the data wrangling and the machine learning model is provided as a Jupyter Notebook.

# Deployment

- Flask is used as the selected framework for the back-end logic. 
- The machine learning model is saved and loaded to the back-end by pickling
- The web-app is deployed to Heroku.



Pickling is used for the implementation on Flask. Gunicorn is used in conjuction with Heroku for the deployment of the web app. 
Corresponding versions of the used dependencies can be found in 'Requirements.txt'. Note that this file is required for a succesful deployment in Heroku.  

HTML, CSS and Jinja2 were used for the front-end development (client side)

