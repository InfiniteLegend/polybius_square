from flask import jsonify
from flask import render_template
from rsa import app


@app.route('/')
@app.route('/index')
def index():
    """
    Index page. Returns template.

    :return:
    """

    # TODO: Return home page template.
    return render_template("index.html", title="Home")


@app.route('/contact')
def develop_page():
    """
    Page with developers info. Returns template.

    :return:
    """

    # TODO: Return info page template.
    return render_template("developers.html", title="Contacts")


@app.route("/api/encode", methods=["POST"], strict_slashes=False)
def encode():
    """
    Encodes message using RSA algorithm.

    :return:
    """

    # TODO: Do the logic and assign the result to the variable below!
    response = dict()
    return jsonify(response)


@app.route("/api/decode", methods=["POST"], strict_slashes=False)
def decode():
    """
    Decodes message using RSA algorithm.

    :return:
    """

    # TODO: Do the logic and assign the result to the variable below!
    response = dict()
    return jsonify(response)
