import requests
import json

def fetch_data():
    # 伺服器 API 的 URL
    url = "http://114.34.88.191:23080/DgApi/Api/GetData/"
    # 傳送的 JSON 資料，請根據需求修改 id 值（例如："A12345"）
    payload = {"id": "B67890"}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if result.get("result") == "200":
                data = result.get("data")
                # 將取得的資料存到 data.json 檔案中
                with open("data.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                print("資料更新成功！")
            else:
                print("API 回傳錯誤：", result.get("message"))
        else:
            print("HTTP 錯誤，狀態碼：", response.status_code)
    except Exception as e:
        print("發生錯誤：", str(e))

if __name__ == "__main__":
    fetch_data()
