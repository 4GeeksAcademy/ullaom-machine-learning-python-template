#from utils import db_connect
engine = db_connect()

from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo previamente descargado
with open("models/random_forest_classifier.sav", "rb") as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        # Asumiendo 4 inputs (cambia según tus datos)
        features = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
        features = np.array(features).reshape(1, -1)
        prediction = model.predict(features)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

