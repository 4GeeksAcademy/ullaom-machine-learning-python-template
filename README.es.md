# Predicción de Riesgo de Diabetes

Este proyecto utiliza un modelo de aprendizaje automático para predecir si una persona tiene riesgo de diabetes en función de sus datos médicos básicos. Se ha implementado una aplicación web interactiva con Flask y desplegado gratuitamente en Render.

🔗 **Demo en vivo:** [https://ullaom-machine-learning-python-template.onrender.com](https://ullaom-machine-learning-python-template.onrender.com)

## 📁 Estructura del proyecto

```
📦 ullaom-machine-learning-python-template
├── app.py                  # Script principal Flask
├── requirements.txt        # Dependencias del proyecto
├── static/
│   └── style.css           # Estilo de la interfaz web
├── templates/
│   └── index.html          # Página HTML con formulario y predicción
├── models/
│   └── random_forest_classifier.sav  # Modelo entrenado guardado
├── src/
│   └── explore.ipynb       # Análisis exploratorio del dataset
```

## 🧠 Modelo

Se utilizó un modelo `Random Forest Classifier` entrenado con datos médicos de pacientes, proveniente del repositorio:

📂 [Repositorio original del modelo](https://github.com/4GeeksAcademy/ulla-decision-tree-project-tutorial)

El modelo fue entrenado con las siguientes variables:

- Número de embarazos
- Nivel de glucosa
- Grosor de piel
- Nivel de insulina
- Índice de masa corporal (IMC)
- Historial familiar de diabetes
- Edad

## 💻 Aplicación Web

La aplicación permite al usuario ingresar estos valores mediante un formulario web y recibir una predicción inmediata:

- ✅ Resultado: **"Negativo (sin riesgo)"** o
- ⚠️ Resultado: **"Positivo para riesgo de diabetes"**

## ⚙️ Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

Ejecuta la aplicación localmente:

```bash
python app.py
```

## ☁️ Despliegue

El proyecto ha sido desplegado en [Render](https://render.com/), en un entorno gratuito. Usa `gunicorn` como servidor WSGI.

Archivo `render.yaml` usado:

```yaml
services:
  - type: web
    name: diabetes-risk-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    plan: free
```

## 👩‍💻 Autora

Proyecto realizado por **Ulla Aller** como parte del Bootcamp de Ciencia de Datos en 4Geeks Academy.
