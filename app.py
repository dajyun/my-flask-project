import os
from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允許所有來源的跨域請求

@app.route("/data", methods=["GET"])
def get_data():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        # 如果讀取到的 data 是字串，就再解析一次
        if isinstance(data, str):
            data = json.loads(data)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
