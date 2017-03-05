import GraphRunner
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    # define some loop data
    image_data, word_data = GraphRunner.get_weights(GraphRunner.get_graphs())

    return render_template("article.html", image_data = image_data, word_data = word_data)

app.run()