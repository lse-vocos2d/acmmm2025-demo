import os
import pathlib
import re
import json
import random
import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.send_from_directory('.', 'index.html')

@app.route('/webdemo-out/<path:filename>')  # type: ignore
def get_webdemo_item(filename: str):
    return flask.send_from_directory(pathlib.Path(__file__).parent / 'webdemo-out', filename)

@app.route('/jslib/vue@3.4.35/<path:filename>')  # type: ignore
def get_vuejs_3_4_35(filename: str):
    return flask.send_from_directory(pathlib.Path(__file__).parent / 'jslib/vue@3.4.35', filename)


if __name__ == '__main__':
    # run with
    #   python <filename>.py
    app.run(host='0.0.0.0', port=24678, debug=True)


