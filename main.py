from turtle import color
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
import math
import joblib
detection1=joblib.load('model.pkl')

def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def detection(gender,SeniorCitizen,Partner,Dependents, tenure,PhoneService,MultipleLines,InternetService, OnlineSecurity,
       OnlineBackup,DeviceProtection,TechSupport,StreamingTV,
       StreamingMovies,Contract,PaperlessBilling,PaymentMethod,
       MonthlyCharges):  
   
    prediction=detection1.predict([[gender,float(SeniorCitizen),Partner,Dependents,int(tenure),PhoneService,MultipleLines,InternetService, OnlineSecurity,
       OnlineBackup,DeviceProtection,TechSupport,StreamingTV,
       StreamingMovies,Contract,PaperlessBilling,PaymentMethod,
       float(MonthlyCharges)]])
    return prediction

  
def add_bg_from_url():
    st.set_page_config(layout="wide")
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.absolutdata.com/wp-content/uploads/2023/02/2023-Tech-Trends-for-Telecoms-and-MVNOs-Blog.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title     
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-White:LavenderBlush;padding:13px">
    <h1 style ="color:white;text-align:center;">Customer Churn Prediction Using Machine Learning </h1>

    </div>
    """
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    #st.date_input("Select Future date")
    gender1=st.selectbox("Gender:",["Male","Female"])
    if gender1=="Male":
        gender=1
    else:
        gender=0
    SeniorCitizen=st.text_input("Enter the value Of SeniorCitizen")
    
    Partner1=st.selectbox("Partner:",['Yes','No'])
    if Partner1=='Yes':
        Partner=1
    else:
        Partner=0
    
    Dependents1=st.selectbox("Dependents:",['Yes','No'])
    if Dependents1=='Yes':
        Dependents=1
    else:
        Dependents=0
        
    tenure=st.text_input("Enter The Value of Tenure")   
    
    PhoneService1=st.selectbox("PhoneService:",['Yes','No'])
    if PhoneService1=='Yes':
        PhoneService=1
    else:
        PhoneService=0
        
    MultipleLines1=st.selectbox("MultipleLines:",['Yes','No'])
    if MultipleLines1=='Yes':
        MultipleLines=1
    else:
        MultipleLines=0
    
    InternetService1=st.selectbox("InternetService:",['DSL','Fiber Optic','No'])
    if InternetService1=='Fiber Optic':
        InternetService=0
    
    elif InternetService1=='DSL':
        InternetService=0
    
    else:
        InternetService=2
        
    
    OnlineSecurity1=st.selectbox("OnlineSecurity:",['Yes','No'])
    if OnlineSecurity1=='Yes':
        OnlineSecurity=1
    else:
        OnlineSecurity=0
    
    OnlineBackup1=st.selectbox("OnlineBackup:",['Yes','No'])
    if OnlineBackup1=='Yes':
        OnlineBackup=1
    else:
        OnlineBackup=0
    
    DeviceProtection1=st.selectbox("DeviceProtection:",['Yes','No'])
    if DeviceProtection1=='Yes':
        DeviceProtection=1
    else:
        DeviceProtection=0
        
    TechSupport1=st.selectbox("TechSupport:",['Yes','No'])
    if TechSupport1=='Yes':
        TechSupport=1
    else:
        TechSupport=0
       
    StreamingTV1=st.selectbox("StreamingTV:",['Yes','No'])
    if StreamingTV1=='Yes':
        StreamingTV=1
    else:
        StreamingTV=0 
    
    StreamingMovies1=st.selectbox("StreamingMovies:",['Yes','No'])
    if StreamingMovies1=='Yes':
        StreamingMovies=1
    else:
        StreamingMovies=0
    
    Contract1=st.selectbox("Contract:",['Month-to-month','One year','Two year'])
    if Contract1=='Month-to-month':
        Contract=0

    elif Contract1=='One year':
        Contract=1
    
    elif Contract1=='Two year':
        Contract=2
   
    PaperlessBilling1=st.selectbox("PaperlessBilling:",['Yes','No'])
    if PaperlessBilling1=='Yes':
        PaperlessBilling=1
    else:
        PaperlessBilling=0

    PaymentMethod1=st.selectbox("PaymentMethod:",['Bank transfer (automatic)','Credit card (automatic)','Electronic check','Mailed check'])
    if PaymentMethod1=='Bank transfer (automatic)':
        PaymentMethod=0
    elif PaymentMethod1=='Electronic':
        PaymentMethod=2
    
    elif PaymentMethod1=='Mailed check':
        PaymentMethod=3
    
    else:
        PaymentMethod=1

    MonthlyCharges=st.text_input("Enter The Value of MonthlyCharges")

   
   
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result

    
    if st.button("Churn Prediction"):
        result=detection(gender,SeniorCitizen,Partner,Dependents, tenure,PhoneService,MultipleLines,InternetService, OnlineSecurity,
       OnlineBackup,DeviceProtection,TechSupport,StreamingTV,
       StreamingMovies,Contract,PaperlessBilling,PaymentMethod,
       MonthlyCharges)
        if result==0:
            result="No Churn "
            
        elif result==1:
            result=" Churn Client"
        
        else:
            result="Error"
         
        
      #st.image('image22.jpg')  
  
    st.success('Customer Churn Crediction ------>>{}'.format(result))
if __name__=='__main__':
    main()