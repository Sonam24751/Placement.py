import streamlit as st
import joblib

model=joblib.load('placement.pkl')

def main():
 st.title('Welcome to placement Predictor')
# cgpa=st.number_input('enter your cgpa')
 cgpa=st.slider('Choose your package from slider ',min_value=0.0,max_value=10.0,step=0.1)
 st.write('enter your cgpa',cgpa)


 if st.button('Predict'):
    result=model.predict([[cgpa]])
    st.success(f'your package would be {result}')


if __name__=='__main__':
    main()