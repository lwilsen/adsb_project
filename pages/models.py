import streamlit as st
import pandas as pd

st.title("Modeling the Data!")
st.divider()

st.header("Model Comparison: Accuracy and F1 Scores")

# Logistic Regression Results
st.markdown("### Logistic Regression")
logistic_regression = pd.DataFrame({
    "Scaler": ["StandardScaler", "MinMaxScaler", "RobustScaler"],
    "Accuracy": [0.7947, 0.7888, 0.5012],
    "F1 Score": [0.8200, 0.8252, 0.5453]
})
st.table(logistic_regression)

# SVC (rbf) Results
st.markdown("### SVC (rbf)")
svc_rbf = pd.DataFrame({
    "Scaler": ["StandardScaler", "MinMaxScaler", "RobustScaler"],
    "Accuracy": [0.8633, 0.8517, 0.5310],
    "F1 Score": [0.8803, 0.8689, 0.6832]
})
st.table(svc_rbf)

def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: lightgreen' if v else '' for v in is_max]
# Random Forest Classifier Results
st.markdown("### Random Forest Classifier")
random_forest = pd.DataFrame({
    "Scaler": ["StandardScaler", "MinMaxScaler", "RobustScaler"],
    "Accuracy": [0.9628, 0.9638, 0.9630],
    "F1 Score": [0.9636, 0.9645, 0.9637]
})
st.table(random_forest.style.apply(highlight_max, subset=["Accuracy","F1 Score"]))

# KNeighborsClassifier Results
st.markdown("### K-Neighbors Classifier")
k_neighbors = pd.DataFrame({
    "Scaler": ["StandardScaler", "MinMaxScaler", "RobustScaler"],
    "Accuracy": [0.8859, 0.9016, 0.8022],
    "F1 Score": [0.8907, 0.9055, 0.8162]
})
st.table(k_neighbors)

# AdaBoostClassifier Results
st.markdown("### AdaBoost Classifier")
ada_boost = pd.DataFrame({
    "Scaler": ["StandardScaler", "MinMaxScaler", "RobustScaler"],
    "Accuracy": [0.7573, 0.7573, 0.7573],
    "F1 Score": [0.8163, 0.8163, 0.8163]
})
st.table(ada_boost)

# GaussianNB Results
st.markdown("### Gaussian Naive Bayes")
gaussian_nb = pd.DataFrame({
    "Scaler": ["StandardScaler", "MinMaxScaler", "RobustScaler"],
    "Accuracy": [0.2684, 0.2725, 0.2645],
    "F1 Score": [0.2208, 0.2246, 0.2208]
})
st.table(gaussian_nb)

st.header("Best Model: Random Forest - MinMaxScaler")
st.write('''I used RandomSearchCV to hypertune the model parameters. The best parameters were:''')
st.table({"Values":{'n_estimators': 300, 'min_samples_split': 2, 'min_samples_leaf': 1, 'max_depth': "None",
           'bootstrap': False}})

st.subheader("Confusion Matrix")
st.write("This confusion matrix shows the percentage of predictions, and whether they were correct or not.")
st.image("./images/30652ef6-4dca-493c-9a5c-361ed56ed6c9.png", use_column_width=True)

classification_data = {
    "Class": [0.0, 1.0, 2.0, 3.0, 10.0, 14.0, 15.0, 16.0, 20.0],
    "Precision": [0.87, 0.97, 1.00, 0.91, 0.98, 0.99, 0.99, 0.00, 0.97],
    "Recall": [0.70, 0.99, 0.77, 0.92, 0.97, 0.98, 0.99, 0.00, 0.86],
    "F1-Score": [0.77, 0.98, 0.87, 0.91, 0.98, 0.99, 0.99, 0.00, 0.91],
    "Support": [184, 6032, 26, 1354, 672, 2939, 141, 5, 128]
}

# Add overall metrics for accuracy, macro avg, and weighted avg
overall_data = {
    "Class": ["Accuracy", "Macro Avg", "Weighted Avg"],
    "Precision": ["-", 0.85, 0.97],
    "Recall": ["-", 0.80, 0.97],
    "F1-Score": [0.97, 0.82, 0.97],
    "Support": [11481, 11481, 11481]
}

# Convert the dictionaries into DataFrames
classification_df = pd.DataFrame(classification_data)
overall_df = pd.DataFrame(overall_data)

# Display the tables in Streamlit
st.markdown("### Classification Report")
st.write("Here we can see the accuracy of the model for each class being predicted")
st.dataframe(classification_df)

st.markdown("### Overall Metrics")
st.dataframe(overall_df)