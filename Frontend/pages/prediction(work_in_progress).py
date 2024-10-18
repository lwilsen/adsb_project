import pickle

import streamlit as st
import pandas as pd
'''
with open("rf_best_mod.pkl", "rb") as f:
    rf_mod = pickle.load(f)

def user_input_features():
    "Takes user inputs and returns a pandas dataframe for predictions"
    Male = st.sidebar.slider("Male (0 = No, 1 = Yes)", 0, 1, 0)
    Age = st.sidebar.text_input("Enter your Age:", "20")
    Sib = st.sidebar.text_input("Number of Siblings", 0, 15, 2)
    Sp = st.sidebar.slider("Spouse (0 = No, 1 = Yes)", 0, 1, 0)
    SibSp = int(Sib) + Sp
    Par = st.sidebar.text_input("Number of Parents:", "2")
    ch = st.sidebar.text_input("Number of Children", 0, 15, 0)
    Parch = int(Par) + int(ch)
    Fare = st.sidebar.text_input("Fare", "20")
    Fare = int(Fare)
    Class = st.sidebar.slider("Class", 1, 3, 1)
    class_to_one_hot = lambda Class: (
        [1, 0, 0] if Class == 1 else [0, 1, 0] if Class == 2 else [0, 0, 1]
    )
    class_1, class_2, class_3 = class_to_one_hot(Class)
    data = {
        "Male": Male,
        "Age": Age,
        "SibSp": SibSp,
        "Parch": Parch,
        "Fare": Fare,
        "class_1": class_1,
        "class_2": class_2,
        "class_3": class_3,
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()'''