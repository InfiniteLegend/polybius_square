from flask import jsonify
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    """
    Index page. Returns template.

    :return:
    """

    # TODO: Return home page template.
    return render_template("index.html", title="Home")


@app.route('/info')
def info_page():
    """
    Info page. Returns template.

    :return:
    """

    # TODO: Return info page template.
    return render_template("info.html", title="Information")


@app.route("/api/encode", methods=["POST"], strict_slashes=False)
def encode():
    """
    Encodes message using Polybius algorithm.

    :return:
    """

    # TODO: Do the logic and assign the result to the variable below!
    response = dict()
    return jsonify(response)


@app.route("/api/decode", methods=["POST"], strict_slashes=False)
def decode():
    """
    Decodes message using Polybius algorithm.

    :return:
    """

    # TODO: Do the logic and assign the result to the variable below!
    response = dict()
    return jsonify(response)
