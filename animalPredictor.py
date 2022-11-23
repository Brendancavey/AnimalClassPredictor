import joblib
import sklearn
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "my_secret_key"

#import trained ML model created from jupyter notebook
model = joblib.load('animal_type_predictor')
@app.route('/animalpredictor')
def index():
    flash("What animal do you see yourself as?...")
    return render_template("index.html")

@app.route('/prediction', methods=["POST", "GET"])
def predict():
    #flash("A " + str(request.form['name_input']) + "? That sounds amazing!")
    list = request.form.getlist("animalfeatures")
    animal_features_list = ["0", "1", "2", "3"]
    pred_bool_list = []

    for i in range(0, len(animal_features_list)):
        if animal_features_list[i] in list:
            pred_bool_list.append(1)
        else:
            pred_bool_list.append(0)
    print(pred_bool_list)
    print(list)
    #prediction = model.predict(request.form.getlist("animalfeatures"))
    #flash(prediction[0])
    return render_template("index.html")


@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username
if __name__ == "__main__":
    app.run(debug=True)