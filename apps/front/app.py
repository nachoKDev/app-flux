from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try:
        r = requests.get("http://backend/api/hello", timeout=2)
        message = r.json()["message"]
    except Exception as e:
        message = f"Error: {e}"

    return f"""
    <h1>Frontend</h1>
    <pre>{message}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
