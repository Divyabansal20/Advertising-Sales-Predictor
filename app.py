import joblib
from flask import Flask, render_template, request
import numpy as np

app= Flask(__name__)

model= joblib.load(r"model\sales_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    tv= float(request.form['tv'])
    radio= float(request.form['radio'])

    features = np.array([[tv, radio]])
    prediction= model.predict(features)

    return render_template('index.html', prediction= round(prediction[0],2))


if (__name__=='__main__'):
    app.run(debug=True)
