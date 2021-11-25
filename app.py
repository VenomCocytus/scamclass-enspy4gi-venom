import pickle
from flask import Flask, request, render_template

app = Flask ('__name__')

vectorizer = pickle.load(open("Vectorizer.sav", "rb"))
model = pickle.load(open("Model.sav", "rb"))

@app.route('/', methods = ["GET", "POST"])
def home():
    msg = "First Message display"
    return render_template("index.html", msg =msg)


@app.route('/spamclassifier', methods = ["GET", "POST"])
def spamclassifier():
    model = pickle.load(open("Model.sav", "rb"))
    vectorizer = pickle.load(open("Vectorizer.sav", "rb"))
    mail = request.form["mail"]
    mail_to_test = vectorizer.transform([mail])
    predict = model.predict(mail_to_test)
    print(predict)
    return " a spam mail" if predict == 1 else " a ham mail"
    
if __name__ == "__main__":
    app.run(port = 8888, debug = True)