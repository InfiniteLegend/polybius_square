from flask import render_template
from flask import request

from app import app
from polybius import encode as encoding
from polybius import decode as decoding


@app.route('/')
@app.route('/index')
def index():
    """
    Index page. Returns template.

    :return:
    """
    # TODO: Return home page template.
    return render_template("index.html", title="Home")


@app.route('/about')
def info_page():
    """
    Info page. Returns template.

    :return:
    """
    # TODO: Return info page template.
    return render_template("info.html", title="About")


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
    Encodes message using Polybius algorithm.

    :return:
    """
    # TODO: Do the logic and assign the result to the variable below!
    text = request.form.get("text", "")
    password = request.form.get("password", "")
    result_data = encoding(text, password)
    return result_data


@app.route("/api/decode", methods=["POST"], strict_slashes=False)
def decode():
    """
    Decodes message using Polybius algorithm.

    :return:
    """
    # TODO: Do the logic and assign the result to the variable below!
    text = request.form.get("text", "")
    password = request.form.get("password", "")
    result_data = decoding(text, password)
    return result_data
