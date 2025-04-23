import requests
import csv
import os

def fetch_latest_lotto_data(count = 10):
    """
    최신 회차부터 거꾸로 지정한 개수만큼 로또 데이터를 수집하여 CSV 파일로 저장합니다.

    Parameters:
        count (int): 수집할 최근 회차 수
    """
    base_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
    lotto_data = []

    # 최신 회차 구하기
    latest_round = get_latest_lotto_number()

    # 최신 회차부터 count만큼 거꾸로 수집
    for i in range(latest_round, latest_round - count, -1):
        url = f"{base_url}{i}"
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

    # 회차 오름차순 정렬
    lotto_data.sort(key = lambda x: x["회차"])

    # 저장
    os.makedirs("data", exist_ok = True)
    with open("data/lotto_data.csv", "w", newline = "", encoding = "utf-8") as f:
        writer = csv.DictWriter(f, fieldnames = lotto_data[0].keys())
        writer.writeheader()
        writer.writerows(lotto_data)

    print(f"{len(lotto_data)}개의 회차 데이터를 저장했습니다.")

def get_latest_lotto_number():
    """
    로또 API를 통해 존재하는 가장 최신 회차 번호를 찾아 반환합니다.

    Returns:
        int: 최신 회차 번호
    """
    low = 1
    high = 2000  # 안전하게 여유 있는 큰 수 설정

    while low <= high:
        mid = (low + high) // 2
        url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={mid}"
        res = requests.get(url).json()

        if res.get("returnValue") == "success":
            low = mid + 1  # 더 높은 회차가 있는지 확인
        else:
            high = mid - 1  # mid는 존재하지 않음 → 이전으로 이동

    return high  # 마지막으로 성공한 회차가 최신 회차