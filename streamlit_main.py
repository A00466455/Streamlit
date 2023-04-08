#importing necessary streamlit library and pickle library
import streamlit as st
from joblib import load

#setting a title for our streamlit webbrowser page
st.title("Iris Prediction Class Work")

#Creating labels for predicted iris flowers
LABELS = ['setosa', 'versicolor', 'virginica']

#loading model from the created pickle file
clf = load("/Users/shiney/Desktop/DT-prediction.joblib")

#creating sliders 
sp_l = st.slider('sepal length (cm)', min_value=0, max_value=10)
sp_w = st.slider('sepal width (cm)', min_value=0, max_value=10)
pe_l = st.slider('petal length (cm)', min_value=0, max_value=10)
pe_w = st.slider('petal width (cm)', min_value=0, max_value=10)

#predicting the type of iris using the existing slider values and model from our pickle file
prediction = clf.predict([[sp_l, sp_w, pe_l, pe_w]])

#writing the prediction onto the browser
st.write(LABELS[prediction[0]])
