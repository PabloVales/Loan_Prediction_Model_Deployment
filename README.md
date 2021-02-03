# Deployment_ML_model

In this repository a binary classification on a loan prediction model is deployed using Flask and Heroku. The deployed web-app can be found here: https://loan-prediction-webapp.herokuapp.com/

# Dataset information

The dataset can be found in the following link: 

Feature information:

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
13. Loan_Status: Loan granted or not (1 for granted, 0 for not granted)

# Model

Model based on logistic regression with recursive feature elimination (RFE) for a binary classification: approved or rejected. The model is provided as a Jupyter Notebook.

# Deployment

Flask is used as the selected framework for the back-end logic. Pickling is used for the implementation on Flask. Gunicorn is used in conjuction with Heroku for the deployment of the web app. 
Corresponding versions of the used dependencies can be found in Requirements.txt. 

HTML, CSS and Jinja2 were used for the front-end development (client side)

