from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
	return "index route"

@app.route("/<string:name>")
def david(name):
	return f"Hello {name}"

if __name__ == "__main__":
	app.env = 'development'
	app.run(debug=True)