from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)  #object of the class


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
