# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:21:20 2020

@author: Pablo Vales
"""

from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import sklearn


## Let's initialize our web app

app = Flask(__name__)

# Define helper functions to load model/transformer
def load_model():
    return pickle.load(open('./model/model.pkl','rb'))

def load_dtypes():
    '''This function loads a pd.Series with the required dtype for each feature'''
    return pickle.load(open('./model/dtypes.pkl', 'rb'))

def load_StandardScaler():
    return pickle.load(open('./model/StandardScaler.pkl', 'rb'))

def load_OneHotEncoder():
    return pickle.load(open('./model/OneHotEncoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def prediction():
    '''Takes results given in the browser and applies them to the model'''
    
    dic = {}
    for i, j in request.form.items():
        dic[i] = [j]
            
#   Create dataframe with input variables from the client 
#   features_df = pd.DataFrame(list(dic.values()), columns=list(dic.keys()))
    features_df = pd.DataFrame(dic)
    features_df = features_df[features_df.columns.sort_values()]
    
    numerical_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
    categorical_cols = sorted(list(set(features_df.columns)-set(numerical_cols)))
    
    #Let's load the feature types for each column and 
    #transform dtypes from features_df to the required ones (for OneHotEncoding and Scaling)
    dtype_ser = load_dtypes()
    features_df = features_df.astype(dtype_ser) #The order stays sorted with the .astype method
    
    
    #scaling numerical values
    scaler = load_StandardScaler()
    X_scaled = pd.DataFrame(scaler.transform(features_df[numerical_cols]), columns=numerical_cols)
    
    #encoding categorical values
    oh_encoder = load_OneHotEncoder()
    X_encoded = pd.DataFrame(oh_encoder.transform(features_df[categorical_cols]), columns=oh_encoder.get_feature_names(categorical_cols))
    
    X = pd.concat([X_scaled, X_encoded], axis=1)
    X = X[X.columns.sort_values()] #sort features for prediction
    
    #prediction
    model = load_model()
    y_pred = model.predict(X)
    
    if y_pred == 0:
        return render_template('index.html',output='Rejected') 
    else:
        return render_template('index.html',output='Approved') 
    
    
if __name__ == '__main__':
    app.run(debug=True)
