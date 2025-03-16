import schedule
import time
from update_data import fetch_data

def job():
    fetch_data()

# 設定每小時執行一次
schedule.every().hour.do(job)

# 如果想要測試，可以暫時改成每 1 分鐘
# schedule.every(1).minutes.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        # 每秒檢查一次是否有工作要執行
        time.sleep(1)
