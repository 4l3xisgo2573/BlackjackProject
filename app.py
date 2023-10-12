from flask import Flask, render_template, request,redirect,url_for
import random
from cardDictionary import cardDB,usedCards

app = Flask(__name__)

counter = [0,0,0]
name = ['Bot 1','Bot 2', "You"]
turn =0
players =[{},{},{}]
botOne={}
botTwo={}
userPlayer={}

@app.route("/", methods=["GET", "POST"])
def index():
    global counter,botOne,botTwo,userPlayer,turn
    if request.method == "POST":
        if request.form["action"] == "yes":
            randomCard = random.choice(list(cardDB.keys()))
            counter[turn] += cardDB[randomCard]['value']
            players[turn][randomCard] = cardDB[randomCard]
            usedCards[randomCard] = cardDB[randomCard]
            cardDB.pop(randomCard)

            return redirect(url_for("index"))
            
        elif request.form["action"] == "no":
            if turn == 2:
                print("Hello")
            else:
                turn =(turn+1)%3

    return render_template("index.html", counter=counter[turn],players = players, name = name[turn]) 


if __name__ == "__main__":
    app.run(debug=True)
