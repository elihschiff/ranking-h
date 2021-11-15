from flask import Flask

app = Flask(__name__)

print("started")

@app.route("/")
def hello_world():
    return "The python web server is running!\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
