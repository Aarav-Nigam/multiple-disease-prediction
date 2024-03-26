import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️",
)


# Set dark theme as default with custom font size
st.markdown(
    """
    <style>
    *{
    color:black;
    }
    body {
        background-color: #1f1f1f; /* Set background color to dark */
        
    }
    .css-1sbuyq5 {
        background-color: #2c2c2c; /* Set specific element background color */
    }
    .css-1sbuyq5:hover {
        background-color: #3c3c3c; /* Set hover background color */
    }
    .css-1sbuyq5:focus {
        box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.3); /* Add focus effect */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(f"{working_dir}/saved_models/diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(
    open(f"{working_dir}/saved_models/heart_disease_model.sav", "rb")
)
parkinsons_model = pickle.load(
    open(f"{working_dir}/saved_models/parkinsons_model.sav", "rb")
)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        menu_icon="hospital-fill",
        icons=["activity", "heart", "person"],
        default_index=0,
        styles={
            "container": {"background-color": "#2c2c2c"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#3c3c3c"},
        },
    )

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")

    st.markdown(
    """
    <style>
    .stApp {
        background-color: #1f1f1f;
        background-image: url('https://medlineplus.gov/images/Diabetes_share.jpg'); /* Add your image filename here */
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies", key="pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level", key="glucose")

    with col3:
        BloodPressure = st.text_input("Blood Pressure value", key="blood_pressure")

    with col1:
        SkinThickness = st.text_input("Skin Thickness value", key="skin_thickness")

    with col2:
        Insulin = st.text_input("Insulin Level", key="insulin")

    with col3:
        BMI = st.text_input("BMI value", key="bmi")

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            "Diabetes Pedigree Function value", key="diabetes_pedigree_function"
        )

    with col2:
        Age = st.text_input("Age of the Person", key="age")

    # Code for Prediction
    diab_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Diabetes Test Result" , type='primary'):
        user_input = [
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age,
        ]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")

    st.markdown(
    """
    <style>
    .stApp {
        background-color: #1f1f1f;
        background-image: url('https://www.heartresearch.com.au/wp-content/uploads/2016/08/shutterstock_208215142-1024x585.jpg'); /* Add your image filename here */
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age", key="age")

    with col2:
        sex = st.text_input("Sex", key="sex")

    with col3:
        cp = st.text_input("Chest Pain types", key="cp")

    with col1:
        trestbps = st.text_input("Resting Blood Pressure", key="trestbps")

    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl", key="chol")

    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl", key="fbs")

    with col1:
        restecg = st.text_input("Resting Electrocardiographic results", key="restecg")

    with col2:
        thalach = st.text_input("Maximum Heart Rate achieved", key="thalach")

    with col3:
        exang = st.text_input("Exercise Induced Angina", key="exang")

    with col1:
        oldpeak = st.text_input("ST depression induced by exercise", key="oldpeak")

    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment", key="slope")

    with col3:
        ca = st.text_input("Major vessels colored by flourosopy", key="ca")

    with col1:
        thal = st.text_input(
            "thal: 0 = normal; 1 = fixed defect; 2 = reversable defect", key="thal"
        )

    # Code for Prediction
    heart_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Heart Disease Test Result",type='primary' ):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = "The person is having heart disease"
        else:
            heart_diagnosis = "The person does not have any heart disease"

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    st.markdown(
    """
    <style>
    .stApp {
        background-color: #f1f1f1;
        # background-image: url('https://www.diabetes.co.uk/wp-content/uploads/2022/11/parkinsons-disease-.jpg'); /* Add your image filename here */
        # background-size: cover;
        # background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)", key="fo")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)", key="fhi")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)", key="flo")

    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)", key="jitter_percent")

    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)", key="jitter_abs")

    with col1:
        RAP = st.text_input("MDVP:RAP", key="rap")

    with col2:
        PPQ = st.text_input("MDVP:PPQ", key="ppq")

    with col3:
        DDP = st.text_input("Jitter:DDP", key="ddp")

    with col4:
        Shimmer = st.text_input("MDVP:Shimmer", key="shimmer")

    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)", key="shimmer_db")

    with col1:
        APQ3 = st.text_input("Shimmer:APQ3", key="apq3")

    with col2:
        APQ5 = st.text_input("Shimmer:APQ5", key="apq5")

    with col3:
        APQ = st.text_input("MDVP:APQ", key="apq")

    with col4:
        DDA = st.text_input("Shimmer:DDA", key="dda")

    with col5:
        NHR = st.text_input("NHR", key="nhr")

    with col1:
        HNR = st.text_input("HNR", key="hnr")

    with col2:
        RPDE = st.text_input("RPDE", key="rpde")

    with col3:
        DFA = st.text_input("DFA", key="dfa")

    with col4:
        spread1 = st.text_input("spread1", key="spread1")

    with col5:
        spread2 = st.text_input("spread2", key="spread2")

    with col1:
        D2 = st.text_input("D2", key="d2")

    with col2:
        PPE = st.text_input("PPE", key="ppe")

    # Code for Prediction
    parkinsons_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Parkinson's Test Result", type='primary'):
        user_input = [
            fo,
            fhi,
            flo,
            Jitter_percent,
            Jitter_Abs,
            RAP,
            PPQ,
            DDP,
            Shimmer,
            Shimmer_dB,
            APQ3,
            APQ5,
            APQ,
            DDA,
            NHR,
            HNR,
            RPDE,
            DFA,
            spread1,
            spread2,
            D2,
            PPE,
        ]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)