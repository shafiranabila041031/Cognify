import streamlit as st
# import pandas as pd
import base64
# import joblib
import numpy as np
from joblib import load

# Fungsi untuk prediksi menggunakan model Random Forest
def predict_rf(tree_ls, X_test):
    pred_ls = []
    for x in X_test:
        ensemble_preds = [predict_tree(tree, x) for tree in tree_ls]
        final_pred = max(set(ensemble_preds), key=ensemble_preds.count)  # Kelas mayoritas
        pred_ls.append(final_pred)
    return np.array(pred_ls)

def predict_tree(tree, x):
    while not tree['is_leaf']:
        if x[tree['feature_idx']] <= tree['split_point']:
            tree = tree['left_child']
        else:
            tree = tree['right_child']
    return tree['prediction']

# # Load the trained model
# model = joblib.load('randomforest_model.joblib')

# # Load Dataset
# file_path = 'alzheimers_data.csv'
# dataset = pd.read_csv(file_path)

# GUI Streamlit
st.set_page_config(page_title="Cognify", page_icon="🧠", layout="centered")

def add_background(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .block-container {{
        padding: 0 !important;
    }}
    header {{
        display: none;
    }}
    body {{
        margin: 0;
        padding: 0;
        overflow: hidden;
    }}
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        width: 100vw;
        margin: 0;
        padding: 0;
    }} 
    header, footer {{
        background-color: rgba(0, 0, 0, 0) !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = 1
if "positive" not in st.session_state:
    st.session_state.positive = False

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

# Page 1
if st.session_state.page == 1:
    add_background("Home Cognify.png")

    st.write("") 
    st.write("")  
    st.write("")  
    st.write("")  
    st.write("")  
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    if st.button("Start Your Detection Now"):
        next_page()

# Page 2
elif st.session_state.page == 2:
    add_background("Detection Cognify.png") 

    st.write("") 
    st.write("")  
    st.write("")  
    st.write("")  
    st.write("")  
    st.write("")  
    st.write("")  
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    # Gunakan kolom untuk tata letak text input
    col1, col2 = st.columns(2)

    with col1:
        memory_complaints = st.number_input(
            "Memory Complaints (0-10):",
            min_value=0.0, max_value=10.0, value=5.0, step=1.0,
            help="A test that measures a person's thinking and remembering abilities, with a score of 0-10 indicating serious problems, 11-20 moderate problems, and 21-30 normal conditions."
        )
        behavioral_problems = st.number_input(
            "Behavioral Problems (0-10):",
            min_value=0.0, max_value=10.0, value=5.0, step=1.0,
            help="Level of behavioral issues"
        )
        mmse = st.number_input(
            "MMSE Score (0-30):",
            min_value=0.0, max_value=30.0, value=15.0, step=1.0,
            help="Cognitive function test"
        )

    with col2:
        adl = st.number_input(
            "ADL Score (0-10):",
            min_value=0.0, max_value=10.0, value=5.0, step=1.0,
            help="Basic daily activities"
        )
        functional_assessment = st.number_input(
            "Functional Assessment Score (0-10):",
            min_value=0.0, max_value=10.0, value=5.0, step=1.0,
            help="Ability to perform daily functions"
        )

    # Load model dari file
    model_path = 'randomforest_model.joblib'
    forest = load(model_path)

    # Prediksi jika tombol ditekan
    if st.button("Prediksi"):
        # Data input dari user
        user_input = np.array([memory_complaints, behavioral_problems, mmse, adl, functional_assessment]).reshape(1, -1)

        # Prediksi menggunakan model
        user_prediction = predict_rf(forest, user_input)

        # Tentukan hasil berdasarkan ambang batas
        threshold = 0.5
        if np.mean(user_prediction) > threshold:
            result = "Terdeteksi Alzheimer"
            st.session_state.positive = 1
        else:
            result = "Tidak Terdeteksi Alzheimer"
            st.session_state.positive = 0

        # Set halaman ke Page 3
        st.session_state.page = 3

# Page 3
elif st.session_state.page == 3:
    # Positive prediction (detected Alzheimer's)
    if st.session_state.positive == 1:
        add_background("Result Positive.png")
    else:
        # Negative prediction (not detected)
        add_background("Result Negative.png")