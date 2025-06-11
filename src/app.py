#from utils import db_connect
#engine = db_connect()

from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo previamente descargado
import os

model_path = os.path.join(os.path.dirname(__file__), 'models/random_forest_classifier.sav')
with open(model_path, "rb") as f:
    model = pickle.load(f)


@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        try:
            features = [
                float(request.form['Pregnancies']),
                float(request.form['Glucose']),
                float(request.form['SkinThickness']),
                float(request.form['Insulin']),
                float(request.form['BMI']),
                float(request.form['DiabetesPedigreeFunction']),
                float(request.form['Age'])
            ]
            features = np.array(features).reshape(1, -1)
            result = model.predict(features)[0]
            prediction = "Positivo para riesgo de diabetes" if result == 1 else "Negativo (sin riesgo)"
        except Exception as e:
            prediction = f"Error al procesar: {e}"

    return render_template('index.html', prediction=prediction)


