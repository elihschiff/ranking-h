from flask import Flask
import subprocess
import logging

app = Flask(__name__)


@app.route("/")
def hello_world():
    logging.info('Root route requested')
    return "The python web server is up and running!\n"

@app.route("/githash")
def githash():
    logging.info('Git version requested')
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    logging.info('App started')
