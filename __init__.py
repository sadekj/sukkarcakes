from flask import Flask, render_template

sukkar = Flask(__name__)

@sukkar.route('/')
def index ():
	return render_template("index.html")

if __name__ == '__main__':
	sukkar.run()