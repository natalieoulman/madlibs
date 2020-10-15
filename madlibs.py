"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')

def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Start a game of Madlibs"""

    answer = request.args.get("answer")
    length = request.args.get("length")

    if answer == "yes" and length == "long":
        return render_template("long_game.html")
    elif answer == "yes" and length == "short":
        return render_template("short_game.html")
    else:
        return render_template("goodbye.html")

@app.route("/short_game")
def show_madlib():

    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    color = request.args.get("color")
    person = request.args.get("person")

    return render_template("madlib.html",
                            noun=noun,
                            adjective=adjective,
                            color=color,
                            person=person)

@app.route("/long_name")
def show_long_game():
    verb_w_ing = request.args.get("verb_w_ing")
    place_noun = request.args.get("place_noun")
    holiday_song = request.args.get("holiday_song")
    adj_1 = request.args.get("adj_1")
    adj_2 = request.args.get("adj_2")
    friend = request.args.get("friend")
    verb_ed_1 = request.args.get("verb_ed_1")
    verb_ed_2 = request.args.get("verb_ed_2")
    amt_time_1 = request.args.get("amt_time_1")
    verb = request.args.get("verb")
    plural_noun = request.args.get("plural_noun")
    relative_1 = request.args.get("relative_1")
    number = request.args.get("number")
    food = request.args.get("food")
    relative_2 = request.args.get("relative_2")
    verb_ed_3 = request.args.get("verb_ed_3")
    noun = request.args.get("noun")
    singer = request.args.get("singer")
    adj_3 = request.args.get("adj_3")
    person = request.args.get("person")
    messy_food = request.args.get("messy_food")
    body_part = request.args.get("body_part")
    amt_time_2 = request.args.get("amt_time_2")
    holiday_food = request.args.get("holiday_food")

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
