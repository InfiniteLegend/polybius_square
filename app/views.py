from flask import jsonify

from app import app


@app.route('/')
@app.route('/index')
def index():
    """
    Index page. Returns template.

    :return:
    """

    # TODO: Return home page template.
    return "Hello, World!"


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
