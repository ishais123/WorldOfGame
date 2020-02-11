from flask import Flask
import Utils

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>Hello to world of game</h1>
        </body>
    </html>"""


@app.route("/score")
def score_page():
    try:
        score = open("Scores.txt", "r")  # score file
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.BAD_RETURN_CODE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>Your score is """ + str(score.readline()) + """ Points</h1>
        </body>
    </html>"""


if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=8080)