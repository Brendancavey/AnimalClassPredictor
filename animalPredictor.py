import joblib
import sklearn
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "my_secret_key"

#import trained ML model created from jupyter notebook
model = joblib.load('animal_type_predictor')

#curated list of different animals for predicted output
mammals = ["Monkey", "Lion", "Bear"]
birds = ["Tucan", "Eagle", "Flamingo"]
reptiles = ["Snake", "Lizard", "Chameleon"]
fish = ["Tuna", "Bass", "Dogfish"]
amphibians = ["Frog", "Toad", "Newt"]
bugs = ["Moth", "Bee", "Beetle"]
invertebrates = ["Lobster", "Octopus", "Scorpion"]


@app.route('/animalpredictor')
def index():

    return render_template("index.html")

@app.route('/prediction', methods=["POST"])
def predict():
    list = request.form.getlist("animalfeatures") #gets the values from the checkboxes user selected
    animal_features_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

    # lists for machine learning model
    pred_bool_list = []  # empty list that will be used to make the prediction. Model only recognizes 1s and 0s as true false values in the order of the animal features list.

    for i in range(0, len(animal_features_list)):
        if animal_features_list[i] == "12": #using dropdown menu for number of legs value. 12 corresponds to num of legs in features list
            pred_bool_list.append(request.form.get("legs"))
        elif animal_features_list[i] in list:
            pred_bool_list.append(1) #appending 1 if checkbox was checked indiciating true
        else:
            pred_bool_list.append(0) #appending 0 if checkbox was not checked indicating false
    print(pred_bool_list)
    print(list)
    prediction = model.predict([pred_bool_list]) #using imported model from Jupyter Notebooks to make prediction
    flash("You are most likely a(n) " + prediction[0] + "!") #prediction is the 0th index in the list
    hidden_msg = "Animals to check out!"
    #Checking for condition to link predicted output to more information via wiki
    if (prediction[0] == "Mammal"):
        animal_list = mammals
        webpage = "https://en.wikipedia.org/wiki/Mammal"
    if (prediction[0] == "Bird"):
        animal_list = birds
        webpage = "https://en.wikipedia.org/wiki/Bird"
    if (prediction[0] == "Reptile"):
        animal_list = reptiles
        webpage = "https://en.wikipedia.org/wiki/Reptile"
    if (prediction[0] == "Fish"):
        animal_list = fish
        webpage = "https://en.wikipedia.org/wiki/Fish"
    if (prediction[0] == "Amphibian"):
        animal_list = amphibians
        webpage = "https://en.wikipedia.org/wiki/Amphibian"
    if (prediction[0] == "Bug"):
        animal_list = bugs
        webpage = "https://en.wikipedia.org/wiki/Insect"
    if (prediction[0] == "Invertebrate"):
        animal_list = invertebrates
        webpage = "https://en.wikipedia.org/wiki/Invertebrate"
    print(request.form.get("legs"))

    # checking for condition verify which checkboxes were selected to output
    # most meaningful graph charts
    bool_list = [False] * len(pred_bool_list)  # true/false value list to compare to prediction_bool_list
    for i in range(0, len(pred_bool_list)):
        if (pred_bool_list[i] == 1):
            bool_list[i] = True
    print(bool_list)
    return render_template("index.html", predicted_list = animal_list, link = webpage, reveal_msg = hidden_msg, predicted_animal = prediction[0], data_button = True, reveal_traits = True,
                           hair = bool_list[0],
                           feathers = bool_list[1],
                           eggs = bool_list[2],
                           milk = bool_list[3],
                           airborne = bool_list[4],
                           aquatic = bool_list[5],
                           predator = bool_list[6],
                           teeth = bool_list[7],
                           backbone = bool_list[8],
                           breathes = bool_list[9],
                           venomous = bool_list[10],
                           fins = bool_list[11],
                           tail = bool_list[13],
                           domestic = bool_list[14])

@app.route('/learnmore', methods=["POST"])
def learnmore():
    return render_template("index.html", reveal_data=True)
@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username
if __name__ == "__main__":
    app.run(debug=True)