# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import joblib


def main():
    
    html_temp="""
    <div style="background-color:lightblue;padding:15px">
    <h2 style="color:black";text-align:center>Health Insurance Cost Prediction</h2>
    </div>
    
    
    """
    
    
     #st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown(html_temp,unsafe_allow_html=True)
    model =joblib.load('model_joblib_gr')
    
   
    p1 = st.slider('Enter your Age',18,100)
    
    s1 = st.selectbox('Gender',('Male','Female'))
    
    if s1=='Male':
        p2=1
    else:
        p2=0
        
    p3 =st.number_input("Enter your BMI Value")
    
    
    p4 = st.slider('Enter no of childrens',0,4)
    
    
    s2=st.selectbox('Select Smoker',('yes','No'))


    if s2=='Yes':
       p5=1
    else:
       p5=0
       
    p6=st.slider('Enter your Region',1,4)
        
    
    if st.button("Pridect"):
        pred=model.predict([[p1,p2,p3,p4,p5,p6]])
        
        
        st.balloons()
        st.success("Your insurance cost is{}".format(round(pred[0])))
     
    
    
if __name__ =='__main__':
    main()
    
    