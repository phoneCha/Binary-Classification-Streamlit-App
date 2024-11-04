import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score 
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, PrecisionRecallDisplay
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, roc_curve, precision_recall_curve
import seaborn as sns

def main():
    ################ Step 1 Create Web Title #####################

    st.title("Binary Classification Streamlit App")
    st.sidebar.title("Binary Classification Streamlit App")
    st.markdown(" เห็ดนี้กินได้หรือไม่??? 🍄‍🟫🍄‍🟫🍄‍🟫")
    st.sidebar.markdown(" เห็ดนี้กินได้หรือไม่??? 🍄‍🟫🍄‍🟫🍄‍🟫")

    ############### Step 2 Load dataset and Preprocessing data ##########

    # create read_csv function
    @st.cache_data(persist=True)
    def load_data():
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DATA_DIR = os.path.join(BASE_DIR, 'data')
        file_path = os.path.join(DATA_DIR, 'mushrooms.csv')

        data = pd.read_csv(file_path)
        label = LabelEncoder()
        for col in data.columns:
            data[col] = label.fit_transform(data[col])
        return data
    
    @st.cache_data(persist=True)
    def spliting_data(df):
        y = df.type
        x = df.drop(columns=['type'])
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=0)
        return x_train, x_test, y_train, y_test
    
    def plot_metrics(metrics_list):
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            fig, ax = plt.subplots()
            ConfusionMatrixDisplay.from_estimator(model, x_test, y_test, ax=ax, display_labels=class_names)
            st.pyplot(fig)
        
        if 'ROC Curve' in metrics_list:
            st.subheader("ROC Curve")
            fig, ax = plt.subplots()
            RocCurveDisplay.from_estimator(model, x_test, y_test, ax=ax)
            st.pyplot(fig)
        
        if 'Precision-Recall Curve' in metrics_list:
            st.subheader("Precision-Recall Curve")
            fig, ax = plt.subplots()
            PrecisionRecallDisplay.from_estimator(model, x_test, y_test, ax=ax)
            st.pyplot(fig)
      
    df = load_data()
    x_train, x_test, y_train, y_test = spliting_data(df)
    class_names = ['edible','poisonous']
    st.sidebar.subheader("Choose Classifiers")
    classifier = st.sidebar.selectbox("Classifier", ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))

    ############### Step 3 Train a SVM Classifier ##########

    if classifier == 'Support Vector Machine (SVM)':
        st.sidebar.subheader("Model Hyperparameters")
        C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C')
        kernel = st.sidebar.radio("Kernel", ("rbf", "linear"), key='kernel')
        gamma = st.sidebar.radio("Gamma (Kernel Coefficient)", ("scale", "auto"), key='gamma')

        metrics = st.sidebar.multiselect("What metrics to plot?", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve"))

        if st.sidebar.button("Classify", key='classify_svm'):
            st.subheader("Support Vector Machine (SVM) Results")
            model = SVC(C=C, kernel=kernel, gamma=gamma)
            model.fit(x_train,y_train)
            accuracy = model.score(x_test, y_test)
            y_pred = model.predict(x_test)

            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            
            st.write("Accuracy: {:.2f}".format(accuracy))
            st.write("Precision: {:.2f}".format(precision))
            st.write("Recall: {:.2f}".format(recall))
            plot_metrics(metrics)

        if st.sidebar.checkbox("Show raw data", False, key='show_data_svm'):
            st.subheader("Mushroom Dataset (SVM)")
            st.write(df)

    ############### Step 4 Training a Logistic Regression Classifier ##########
    if classifier == 'Logistic Regression':
        st.sidebar.subheader("Model Hyperparameters")
        C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C_LR')
        max_iter = st.sidebar.slider("Maximum iterations", 100, 1000, step=50, key='max_iter')
            
        metrics = st.sidebar.multiselect("What metrics to plot?", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve"))
            
        if st.sidebar.button("Classify", key='classify_lr'):
            st.subheader("Logistic Regression Results")
            model = LogisticRegression(C=C, max_iter=max_iter)
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
                
            accuracy = model.score(x_test, y_test)
            precision = precision_score(y_test, y_pred, average='binary')
            recall = recall_score(y_test, y_pred, average='binary')
                
            st.write("Accuracy: {:.2f}".format(accuracy))
            st.write("Precision: {:.2f}".format(precision))
            st.write("Recall: {:.2f}".format(recall))
            plot_metrics(metrics)

        if st.sidebar.checkbox("Show raw data", False, key='show_data_lr'):
            st.subheader("Mushroom Dataset (LR)")
            st.write(df)

    ############### Step 5 Training a Random Forest Classifier ##########
    if classifier == 'Random Forest':
        st.sidebar.subheader("Model Hyperparameters")
        n_estimators = st.sidebar.slider("Number of trees in the forest", 10, 500, key='n_estimators')
        max_depth = st.sidebar.slider("Maximum depth of the tree", 1, 20, key='max_depth')
        bootstrap = st.sidebar.radio("Bootstrap samples when building trees", ('True', 'False'), key='bootstrap')

        metrics = st.sidebar.multiselect("What metrics to plot?", ("Confusion Matrix", "ROC Curve", "Precision-Recall Curve"))
        
        if st.sidebar.button("Classify", key='classify_rf'):
            st.subheader("Random Forest Classifier Results")
            model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, bootstrap=(bootstrap == 'True'))
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)

            accuracy = model.score(x_test, y_test)  
            precision = precision_score(y_test, y_pred, average='binary')
            recall = recall_score(y_test, y_pred, average='binary')

            st.write("Accuracy: {:.2f}".format(accuracy))
            st.write("Precision: {:.2f}".format(precision))
            st.write("Recall: {:.2f}".format(recall))
            plot_metrics(metrics)

        if st.sidebar.checkbox("Show raw data", False, key='show_data_rf'):
            st.subheader("Mushroom Dataset (RF)")
            st.write(df)

if __name__ == '__main__':
    main()