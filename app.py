from flask import Flask, request, jsonify, render_template
from mycrypto import sign_article, verify_article, simulate_attacks
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/sign", methods=["POST"])
def sign():
    data = request.get_json()
    article = data["article"]
    result = sign_article(article)
    return jsonify(result)

@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json()
    article = data["article"]
    signature = data["signature"]
    public_key = data["public_key"]
    result = verify_article(article, signature, public_key)
    return jsonify(result)

@app.route("/attacks", methods=["POST"])
def attacks():
    data = request.get_json()
    article = data["article"]
    signature = data["signature"]
    public_key = data["public_key"]
    result = simulate_attacks(article, signature, public_key)
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)