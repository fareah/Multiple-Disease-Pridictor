"""
Created on Sun May  7 16:48:44 2023

@author: FAREAH RAHMAN
"""

import platform
from packaging import version 
if version.parse(platform.python_version())<version.parse("3.8.0"):
    import pickle5 as pickle
else:
    import pickle
    
    
import streamlit as st
from streamlit_option_menu import option_menu



diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb')) 


#sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           
                           icons = ['activity','heart','person'],
                           default_index = 0)
    
    

if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction')#Diabetes Prediction Page
    
    
    
    
   
    
    
    
    
    #getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnanacies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    #code for Prediction
    diab_diagnosis = ''
    
    #creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnanacies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = "The person is Diabetic"
        else:
            diab_diagnosis = "The person is not Diabetic"
        
    st.success(diab_diagnosis)
    
   
    

    
if(selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction')
    
    
    #getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest pain')
        
    with col1:
        trestbps = st.text_input('Trestbps value')
        
    with col2:
        chol = st.text_input('Cholestrol')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')
        
    with col1:
        restecg = st.text_input('restecg')
        
    with col2:
        thalach = st.text_input('thalach')
    
    with col3:
        exang = st.text_input('exang')
        
    with col1:
        oldpeak = st.text_input('oldpeak')
        
    with col2:
        slope = st.text_input('slope')
        
    with col3:
        ca = st.text_input('CA')
        
    with col1:
        thal = st.text_input('thal')
    
    
    #code for Prediction
    heart_diagnosis = ''
    
    #creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = "The person is having heart disease"
        else:
            heart_diagnosis = "The person is not having any heart disease"
        
    st.success(heart_diagnosis)
    
    
    
    
    
    
    
    
    