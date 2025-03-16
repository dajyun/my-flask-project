import schedule
import time
from update_data import fetch_data

# 計數器，記錄更新次數
counter = 0

def job():
    global counter
    fetch_data()
    counter += 1
    print("已更新資料次數：", counter)

# 設定每小時執行一次
# schedule.every().hour.do(job)

# 若想測試，可以暫時改成每 1 分鐘
schedule.every(1).minutes.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
