import os
import pickle  # Pre-trained model loading
import streamlit as st  # Web app
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

# Loading the models
diabetes_model = pickle.load(open(r"C:\Users\viraj\Documents\AICT internship1\savedfiles\ diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\viraj\Documents\AICT internship1\savedfiles\ heartdisease_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\viraj\Documents\AICT internship1\savedfiles\ parkinsons_model.sav", 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age')
        RestingBP = st.text_input('Resting Blood Pressure')
        RestECG = st.text_input('Resting Electrocardiographic results')
        ST_Depression = st.text_input('ST depression induced by exercise')
        Thal = st.text_input('Thal (0 = normal, 1 = fixed defect, 2 = reversible defect)')
    with col2:
        Sex = st.text_input('Sex')
        SerumCholesterol = st.text_input('Serum Cholesterol in mg/dl')
        MaxHeartRate = st.text_input('Maximum Heart Rate achieved')
        Slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ChestPainType = st.text_input('Chest Pain types')
        FastingBloodSugar = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        ExerciseInducedAngina = st.text_input('Exercise Induced Angina')
        MajorVessels = st.text_input('Major vessels colored by fluoroscopy')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [Age, Sex, ChestPainType, RestingBP, SerumCholesterol, FastingBloodSugar, RestECG,
                      MaxHeartRate, ExerciseInducedAngina, ST_Depression, Slope, MajorVessels, Thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'

    st.success(heart_diagnosis)

# Parkinson's Disease Prediction Page
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo = st.text_input('MDVP (Hz)')
        MDVP_Shimmer = st.text_input('MDVP Shimmer')
        HNR = st.text_input('HNR')
        D2 = st.text_input('D2')
    with col2:
        MDVP_Fhi = st.text_input('MDVP (Hz)')
        MDVP_Jitter = st.text_input('MDVP Jitter')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')
    with col3:
        MDVP_Flo = st.text_input('MDVP (Hz)')
        MDVP_dB = st.text_input('MDVP (dB)')
        DFA = st.text_input('DFA')
        Spread1 = st.text_input('Spread1')
        Spread2 = st.text_input('Spread2')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Shimmer, MDVP_dB, HNR, RPDE, DFA, Spread1, Spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person has Parkinson’s disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinson’s disease'

    st.success(parkinsons_diagnosis)
