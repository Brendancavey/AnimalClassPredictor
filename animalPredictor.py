from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route('/animalpredictor')
def index():
    flash("What animal do you see yourself as?...")
    return render_template("index.html")

@app.route('/prediction', methods=["POST", "GET"])
def predict():
    flash("A " + str(request.form['name_input']) + "? That sounds amazing!")
    return render_template("index.html")


@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username
if __name__ == "__main__":
    app.run(debug=True)