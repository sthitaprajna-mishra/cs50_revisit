from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
	today = datetime.now()
	value = today.month == 1 and today.day == 1
	return render_template("index.html", condition = value)

if __name__ == "__main__":
	app.env = "development"
	app.run(debug=True)