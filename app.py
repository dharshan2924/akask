from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder=".")
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return send_from_directory(".", "index.html")

@app.route("/uploads/<path:filename>")
def uploaded_files(filename):
    return send_from_directory("uploads", filename)

# Optional analyze route (if you have backend logic)
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    # simple echo or logic
    return jsonify({"analysis": f"Received: {text}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT
    app.run(host="0.0.0.0", port=port)
