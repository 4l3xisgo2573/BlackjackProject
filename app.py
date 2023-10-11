from flask import Flask, render_template, request,redirect,url_for
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
            randomCard = random.choice(list(cardDB.keys()))
            counter += cardDB[randomCard]['value']
            userPlayer[randomCard] = cardDB[randomCard]
            cardDB.pop(randomCard)
            print(randomCard)
            return redirect(url_for("index"))
            
        elif request.form["action"] == "no":
            counter -= 1

    return render_template("index.html", counter=counter, chosenCard=chosenCard,userPlayer=userPlayer)


if __name__ == "__main__":
    app.run(debug=True)
