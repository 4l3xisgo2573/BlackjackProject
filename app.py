from flask import Flask, render_template, request
import cardDictionary
app = Flask(__name__)

counter = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global counter 
    if request.method == 'POST':
        if request.form['action'] == 'yes':
            counter += 1
            print()
            print(cardDictionary.cardDB[1]["value"])
            print()
        elif request.form['action'] == 'no':
            counter -= 1
    
    return render_template('index.html', counter=counter)

if __name__ == '__main__':
    app.run(debug=True)
