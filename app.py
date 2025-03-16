import os
import threading
import time
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 啟用跨域，讓 Wix 前端可以正確取得資料

# 用於儲存最新資料的全域變數
data_storage = {}

def update_data():
    """
    此函式從外部 API 抓取最新資料，並更新全域變數 data_storage。
    請根據你 PDF 中的 API 規格做適當修改。
    """
    try:
        # 外部 API 的 URL 及傳送資料 (請根據你的需求修改)
        url = "http://114.34.88.191:23080/DgApi/Api/GetData/"
        payload = {"id": "A12345"}  # 假設這裡用固定 id，實際可調整
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            # 根據 PDF 規格：當 result 為 "200" 表示成功，資料在 result["data"]
            if result.get("result") == "200":
                new_data = result.get("data", {})
                global data_storage
                data_storage = new_data
                print("Data updated:", data_storage)
            else:
                print("API error:", result.get("message"))
        else:
            print("HTTP error:", response.status_code)
    except Exception as e:
        print("Error in update_data:", str(e))

def scheduler_thread():
    """
    這個背景執行緒會每 1 小時呼叫一次 update_data()，以自動更新資料。
    """
    while True:
        update_data()
        time.sleep(3600)  # 等待 3600 秒 = 1 小時

# 啟動背景執行緒 (daemon 模式)
threading.Thread(target=scheduler_thread, daemon=True).start()

@app.route("/data", methods=["GET"])
def get_data():
    """
    當前端呼叫 /data 時，回傳最新更新的 data_storage 資料。
    若還沒有更新到資料，回傳錯誤訊息。
    """
    if data_storage:
        return jsonify(data_storage)
    else:
        return jsonify({"error": "Data not available yet"}), 503

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
