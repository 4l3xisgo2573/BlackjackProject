from flask import Flask, render_template, request,redirect,url_for
import random
from cardDictionary import cardDB,usedCards

app = Flask(__name__)

counter = 0
turn =0
botOne={}
botTwo={}
userPlayer={}

@app.route("/", methods=["GET", "POST"])
def index():
    global counter,botOne,botTwo,userPlayer,turn
    if request.method == "POST":
        if request.form["action"] == "yes":
            randomCard = random.choice(list(cardDB.keys()))
            
            counter += cardDB[randomCard]['value']
            userPlayer[randomCard] = cardDB[randomCard]
            usedCards[randomCard] = cardDB[randomCard]
            cardDB.pop(randomCard)
            turn =(turn+1)%3

            print(turn)
            return redirect(url_for("index"))
            
        elif request.form["action"] == "no":
            counter -= 1

    return render_template("index.html", counter=counter,userPlayer=userPlayer)


if __name__ == "__main__":
    app.run(debug=True)
