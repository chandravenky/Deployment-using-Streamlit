# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 17:32:10 2020

@author: vchan
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

#Change working directory - only for debugging purposes
#import os
#os.chdir(r'C:\Users\vchan\Desktop\git\Deployment-using-Streamlit')


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#Decorator not needed for stremlit
def welcome():
    return "Risk Classification App"


def predictions(age, marital_status, income):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: age
        in: query
        type: number
        required: true
      - name: marital_status
        in: query
        type: number
        required: true
      - name: income
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    #Generate prediction
    prediction = classifier.predict([[age, marital_status, income]])
    print(prediction)
    return prediction


#Define main function
def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","Type Here")
    marital_status = st.text_input("marital_status","Type Here")
    income = st.text_input("income","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predictions(age, marital_status, income)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Predict")
        st.text("Built by Venky")


#This runs the app
if __name__ == "__main__":
    main()
    
    