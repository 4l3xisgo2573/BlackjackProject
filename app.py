from flask import Flask, render_template, request
import random
from cardDictionary import cardDB

app = Flask(__name__)




chosenCard = cardDB[1]["cardImg"]

counter = 0
botOne={}
botTwo={}
userPlayer={}

@app.route("/", methods=["GET", "POST"])
def index():
    global counter,botOne,botTwo,userPlayer
    
    
    if request.method == "POST":
        if request.form["action"] == "yes":
            
            randomCard = random.randint(1,len(cardDB))
            print(randomCard)
            counter += cardDB[randomCard]['value']
            print(f"Chosen Card Value: {cardDB[randomCard]['value']}")
        elif request.form["action"] == "no":
            counter -= 1

    return render_template("index.html", counter=counter, chosenCard=chosenCard)


if __name__ == "__main__":
    app.run(debug=True)
