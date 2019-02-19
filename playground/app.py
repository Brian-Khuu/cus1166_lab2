from flask import Flask,render_template, request

app = Flask(__name__)


roster = [("Brian", 90, "Junior"), ("Sam", 93, "Senior"), ("Aoife", 85, "Sophomore"), ("Alexa", 97, "Freshman"), ("Matthew", 94, "Freshman"), ("Leona", 87, "Senior"), ("Joey", 80, "Junior")]

@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/welcome/<string:value>')
def welcome(value):
    return render_template('welcome.html', title='Welcome', name=value)


@app.route('/roster/<string:view>')
def roster(view):
    class_roster = [("Brian", 90, "Junior"), ("Sam", 93, "Senior"), ("Aoife", 85, "Sophomore"), ("Alexa", 97, "Freshman"), ("Matthew", 94, "Freshman"), ("Leona", 87, "Senior"), ("Joey", 80, "Junior")]
    return render_template('roster.html', title='Roster', class_roster=class_roster,view=view)


if __name__ == "__main__":
    app.run()
