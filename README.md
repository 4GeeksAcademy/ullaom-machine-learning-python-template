# Diabetes Risk Prediction Web App

This repository contains a simple web application that predicts the risk of diabetes based on user input. The app is built with **Flask** and integrates a previously trained **Random Forest Classifier** model.

🔗 Try the live demo: [ullaom-machine-learning-python-template.onrender.com](https://ullaom-machine-learning-python-template.onrender.com)

---

## 🗂 Project Structure

- `src/`: Contains the app logic
  - `app.py`: Main Flask application
  - `templates/index.html`: HTML form and result display
  - `models/random_forest_classifier.sav`: Trained model
- `static/style.css`: Custom styling for the web interface
- `explore.ipynb`: EDA and model training notebook
- `requirements.txt`: List of dependencies
- `README.es.md`: Spanish version of this document

---

## 📊 Dataset Used

The model was trained using the **Pima Indians Diabetes Dataset**, available publicly from various sources (e.g., Kaggle, UCI ML Repository). This dataset includes features like:
- Pregnancies
- Glucose
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## 🚀 Deployment

The app is deployed using **Render** and can be accessed online.

To run locally:

```bash
pip install -r requirements.txt
python src/app.py
```

---

## 🙋‍♀️ Author

Developed by **Ulla Aller** as part of the Machine Learning module at 4Geeks Academy.


