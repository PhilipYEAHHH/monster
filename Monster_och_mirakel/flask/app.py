from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/start/')
def väljTyp():
    f = open("klassen.txt", "r")
    klasslista = f.readlines()
    f.close()
    return render_template("start.html", namnen=dragon)

if __name__ == '__main__':
    app.run(port=2025)