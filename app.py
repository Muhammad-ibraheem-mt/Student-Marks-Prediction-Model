import pandas as pd
import streamlit as st 
import joblib 


model = joblib.load('Q:\Project\mp.joblib')

st.title('Marks Prediction')


st.markdown(
   """
   <b>
   <i>
   Model will Predict Marks based on Study Hours
   """,unsafe_allow_html=True
)


st.markdown(
   """
   <b style='color:red;'>
   <i>
   Study Hours 
   """,unsafe_allow_html=True
)

exp = st.slider(
    '',
    min_value=1,
    max_value=12,
    value=1
)

if st.button('Predict'):
   val =model.predict([[exp]])
   st.markdown(f'''
               <span style='
               background-color:black;
               color:white;
               width:90px;
               font-weight:900;
               border-radius:5px;
               '>
              &nbsp;  Model Predicted Value &nbsp; <b style='color:yellow;'>{val[0]:.0f}% &nbsp;</span>


''',unsafe_allow_html=True)
