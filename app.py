from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("Project.sav")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        # Collect form data
        sex = request.form["Sex"]
        age = int(request.form["Age"])
        height = float(request.form["Height"])
        weight = float(request.form["Weight"])
        duration = float(request.form["Duration"])
        heart_rate = int(request.form["Heart_Rate"])
        body_temp = float(request.form["Body_Temp"])

        # Encode 'Sex'
        sex = 1 if sex.lower() == "m" else 0

        # Create input DataFrame
        data = pd.DataFrame([[sex, age, height, weight, duration, heart_rate, body_temp]],
                            columns=["Sex", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"])

        # Predict
        prediction = round(model.predict(data)[0], 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
