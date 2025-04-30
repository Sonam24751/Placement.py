import streamlit as st
import joblib


model = joblib.load('placement.pkl')

def main():
   
    st.markdown("<h1 style='color:orange;'>Placement Package Predictor</h1>", unsafe_allow_html=True)

    cgpa = st.slider('Choose your CGPA', min_value=0.0, max_value=10.0, step=0.1)
    st.write('You entered CGPA:', cgpa)

    if st.button('Predict'):
        result = model.predict([[cgpa]])
        st.success(f'Your predicted package would be: {float(result[0]):.2f} LPA')

if __name__ == '__main__':
    main()
