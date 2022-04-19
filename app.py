import os
import sys

from flask import Flask

try :
    app = Flask(__name__)

    ENV=os.getenv("ENV","NOTSET")
    SECRET_CODE=os.getenv("SECRET_CODE","NOTSET")

    assert ENV !="NOTSET","ENV not set"
    assert SECRET_CODE !="NOTSET","Secret Code is not set"
except AssertionError as asserr:
    print(f"Assertion Error : {asserr}")
    sys.exit()
except Exception as err:
    print(f"Error : {err}")
    sys.exit()

@app.route("/")
def index():
    return f"In God We Trust! In {ENV} with secret Code {SECRET_CODE}"