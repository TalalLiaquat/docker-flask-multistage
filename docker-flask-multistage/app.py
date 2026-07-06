from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Docker Multi-Stage Build Project</h1>
    <p>Python Flask Application Running Successfully 🚀</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)