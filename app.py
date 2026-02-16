from flask import Flask, render_template, request
import pickle
import numpy as np
import json
import warnings
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

warnings.filterwarnings("ignore")

app = Flask(__name__)

# --------------------------------------------------
# Load ML Models
# --------------------------------------------------
with open("knn_model.pkl", "rb") as f:
    knn_model = pickle.load(f)

with open("naive_bayes_model.pkl", "rb") as f:
    nb_model = pickle.load(f)

# --------------------------------------------------
# Load Test JSON Files
# --------------------------------------------------
with open("KNNtest.json", "r") as f:
    knn_test_data = json.load(f)

with open("NBtest.json", "r") as f:
    nb_test_data = json.load(f)

# --------------------------------------------------
# Utility functions
# --------------------------------------------------
def map_species(value):
    return {
        0: "Iris-setosa",
        1: "Iris-versicolor",
        2: "Iris-virginica",
        3: "Iris-virginica"  # safety for old encodings
    }.get(value, "Unknown")


def compute_metrics(model, dataset):
    X = []
    y = []

    for row in dataset:
        X.append([
            row["SepalLengthCm"],
            row["SepalWidthCm"],
            row["PetalLengthCm"],
            row["PetalWidthCm"]
        ])

        # Support both formats
        if "Species" in row:
            y.append(row["Species"])
        elif "actual" in row:
            y.append(row["actual"])

    X = np.array(X)
    y = np.array(y)

    y_pred = model.predict(X)

    return {
        "accuracy": accuracy_score(y, y_pred),
        "report": classification_report(y, y_pred, output_dict=True),
        "confusion": confusion_matrix(y, y_pred).tolist()
    }

# --------------------------------------------------
# Routes
# --------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    actual = None
    model_name = None

    accuracy = None
    report = None
    confusion = None

    if request.method == "POST":
        try:
            # Match HTML field names
            features = np.array([
                float(request.form["SepalLengthCm"]),
                float(request.form["SepalWidthCm"]),
                float(request.form["PetalLengthCm"]),
                float(request.form["PetalWidthCm"])
            ]).reshape(1, -1)

            selected_model = request.form["model"]

            if selected_model == "knn":
                model = knn_model
                test_data = knn_test_data
                model_name = "KNN"
            else:
                model = nb_model
                test_data = nb_test_data
                model_name = "Naive Bayes"

            # Prediction
            pred = model.predict(features)[0]
            prediction = map_species(pred)

            # Metrics
            metrics = compute_metrics(model, test_data)
            accuracy = metrics["accuracy"]
            report = metrics["report"]
            confusion = metrics["confusion"]

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template(
        "index.html",
        prediction=prediction,
        actual=actual,
        model_name=model_name,
        accuracy=accuracy,
        report=report,
        confusion=confusion
    )

# --------------------------------------------------
# Run App
# --------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
