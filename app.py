# importin flask module in project
from flask import Flask

#create object of flask class
app = Flask(__name__)

@app.route("/")

def first_flask():
    return "this is my first flask program"

app.run()

@app.route("/flask_2")

def second_flask():
    return "py is fun"

app.run(debug = True)