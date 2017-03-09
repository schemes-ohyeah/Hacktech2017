import GraphRunner
from flask import Flask, render_template
app = Flask(__name__)

image_graph, word_graph = GraphRunner.get_graphs()
image_data = GraphRunner.get_weights(image_graph)
word_data = GraphRunner.get_weights(word_graph)

print("image_data")
for val in image_data.keys():
    print("Key: ",  val)
    print("\tValue", image_data[val])

print("word_data")
for val in word_data.keys():
    print("Key: ",  val)
    print("\tValue", word_data[val])

@app.route("/")
def index():
    # define some loop data
    return render_template("article.html", image_data = image_data, word_data = word_data)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
