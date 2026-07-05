"""A small Flask web app that demonstrates the mine_files utility library.

Run with:
    pip install flask
    python webapp/app.py
Then open http://127.0.0.1:5000
"""

import json

from flask import Flask, jsonify, render_template, request

from mine_files import calculator, stats, string_utils, validator

app = Flask(__name__)


def _parse_number(value):
    value = value.strip()
    try:
        return int(value)
    except ValueError:
        return float(value)


def _parse_number_list(value):
    return [_parse_number(v) for v in value.replace(",", " ").split()]


CALCULATOR_OPS = {
    "add": lambda a, b: calculator.add(a, b),
    "subtract": lambda a, b: calculator.subtract(a, b),
    "multiply": lambda a, b: calculator.multiply(a, b),
    "divide": lambda a, b: calculator.divide(a, b),
    "power": lambda a, b: calculator.power(a, b),
    "gcd": lambda a, b: calculator.gcd(int(a), int(b)),
    "lcm": lambda a, b: calculator.lcm(int(a), int(b)),
}

STRING_OPS = {
    "reverse": string_utils.reverse,
    "is_palindrome": string_utils.is_palindrome,
    "capitalize_words": string_utils.capitalize_words,
    "count_vowels": string_utils.count_vowels,
    "snake_to_camel": string_utils.snake_to_camel,
    "camel_to_snake": string_utils.camel_to_snake,
}

VALIDATOR_OPS = {
    "is_valid_email": validator.is_valid_email,
    "is_valid_url": validator.is_valid_url,
    "is_strong_password": validator.is_strong_password,
    "is_valid_ip": validator.is_valid_ip,
    "is_valid_phone": validator.is_valid_phone,
}

STATS_OPS = {
    "mean": stats.mean,
    "median": stats.median,
    "mode": stats.mode,
    "variance": stats.variance,
    "std_dev": stats.std_dev,
}


@app.route("/")
def index():
    return render_template(
        "index.html",
        calculator_ops=list(CALCULATOR_OPS),
        string_ops=list(STRING_OPS),
        validator_ops=list(VALIDATOR_OPS),
        stats_ops=list(STATS_OPS),
    )


@app.route("/api/calculator", methods=["POST"])
def api_calculator():
    data = request.get_json(force=True)
    op = data["op"]
    a = _parse_number(str(data["a"]))
    b = _parse_number(str(data["b"]))
    return jsonify(result=CALCULATOR_OPS[op](a, b))


@app.route("/api/factorial", methods=["POST"])
def api_factorial():
    data = request.get_json(force=True)
    return jsonify(result=calculator.factorial(int(data["n"])))


@app.route("/api/string", methods=["POST"])
def api_string():
    data = request.get_json(force=True)
    return jsonify(result=STRING_OPS[data["op"]](data["text"]))


@app.route("/api/validator", methods=["POST"])
def api_validator():
    data = request.get_json(force=True)
    return jsonify(result=VALIDATOR_OPS[data["op"]](data["text"]))


@app.route("/api/stats", methods=["POST"])
def api_stats():
    data = request.get_json(force=True)
    numbers = _parse_number_list(data["numbers"])
    return jsonify(result=STATS_OPS[data["op"]](numbers))


@app.errorhandler(Exception)
def handle_error(exc):
    return jsonify(error=f"{type(exc).__name__}: {exc}"), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
