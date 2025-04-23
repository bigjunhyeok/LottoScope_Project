import pandas as pd
from collections import Counter
from datetime import datetime, timedelta

def recommend_today_numbers(path = "data/lotto_data.csv", recent_count = 100):
    """
    최근 N회차 데이터를 기반으로, 다음 회차의 당첨 예측 번호를 출력합니다.

    Parameters:
        path (str): 로또 데이터 CSV 파일 경로
        recent_count (int): 분석에 사용할 최근 회차 수

    Returns:
        list: 예측 추천 번호 리스트 (6개)
    """
    # CSV 파일에서 로또 데이터 불러오기
    df = pd.read_csv(path)

    # 최신 회차 정보 정확히 추출
    latest_round = df["회차"].max()
    latest_row = df[df["회차"] == latest_round].iloc[0]
    latest_draw_date = datetime.strptime(latest_row["추첨일"], "%Y-%m-%d")

    # 다음 회차 정보 계산
    next_round = latest_round + 1
    next_draw_date = latest_draw_date + timedelta(days = 7)

    # 최근 N회차만 사용하여 분석
    recent_df = df[df["회차"] > (latest_round - recent_count)]

    # 번호 1~6만 추출해서 리스트화
    numbers = []
    for i in range(1, 7):
        numbers.extend(recent_df[f"번호{i}"].tolist())

    # 출현 빈도 높은 번호 6개 선정
    counter = Counter(numbers)
    most_common = sorted([num for num, _ in counter.most_common(6)])

    # 출력용 날짜 포맷
    today = datetime.today().strftime("%Y-%m-%d (%a)")
    next_draw_date_str = next_draw_date.strftime("%Y-%m-%d (%a)")

    # 예측 결과 출력
    print("\n[ 이번 주 당첨 예측 번호 ]")
    print("-" * 50)
    print(f"기준 날짜 : {today}")
    print(f"예측 대상 회차 : {next_round}회차")
    print(f"예측 대상 추첨일자 : {next_draw_date_str}")
    print(f"분석에 사용된 회차 수 : 최근 {recent_count}회차 기준")
    print(f"통계 기반 추천 번호 : {most_common}")
    print("-" * 50)

    return most_common