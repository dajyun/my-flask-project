import os
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/data", methods=["GET"])
def get_data():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 404

if __name__ == "__main__":
    # Render 會自動把 PORT 設定為系統環境變數
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
