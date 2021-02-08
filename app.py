from flask import Flask
from models.modeler import inspect_db, refresh_model
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/inspect/<object_name>')
def get_db_object_metadata(object_name: str):
    mdl = refresh_model(object_name)
    j_mdl = json.dumps(mdl)
    return j_mdl


if __name__ == '__main__':
    app.run()
