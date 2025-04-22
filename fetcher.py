# fetcher.py
import requests
import csv
import os

def fetch_latest_lotto_data(count=10):
    base_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
    lotto_data = []

    for i in range(1, count + 1):
        url = base_url + str(i)
        res = requests.get(url).json()
        if res.get("returnValue") == "fail":
            continue
        row = {
            "회차": res["drwNo"],
            "추첨일": res["drwNoDate"],
            "번호1": res["drwtNo1"],
            "번호2": res["drwtNo2"],
            "번호3": res["drwtNo3"],
            "번호4": res["drwtNo4"],
            "번호5": res["drwtNo5"],
            "번호6": res["drwtNo6"],
            "보너스": res["bnusNo"]
        }
        lotto_data.append(row)

    os.makedirs("data", exist_ok=True)
    with open("data/lotto_data.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=lotto_data[0].keys())
        writer.writeheader()
        writer.writerows(lotto_data)
    print(f"{len(lotto_data)}개의 회차 데이터를 저장했습니다.")
