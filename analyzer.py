import pandas as pd
from collections import Counter

def analyze_frequencies(path = "data/lotto_data.csv"):
    """
    CSV에 저장된 로또 번호 데이터를 분석하여 자주 출현한 번호를 출력합니다.
    분석 회차 범위(최소~최대 회차 번호)도 함께 출력됩니다.

    Parameters:
        path (str): 분석할 로또 데이터 CSV 경로
    """
    # CSV 파일 읽기
    df = pd.read_csv(path)

    # 전체 번호 수집
    numbers = []
    for i in range(1, 7):
        numbers.extend(df[f"번호{i}"].tolist())

    # 출현 빈도 계산
    counter = Counter(numbers)
    most_common = counter.most_common()

    # 분석된 회차 범위 확인
    min_round = df["회차"].min()
    max_round = df["회차"].max()

    # 결과 출력
    print("\n📊  통계 분석 중 ...")
    print(f"분석 범위 : {min_round}회차 ~ {max_round}회차")
    print("\n[ 출현 빈도 TOP 10 번호 ]")
    print("-" * 40)
    for num, count in most_common[:10]:
        print(f"🎯  번호 {num:>2} : {count} 회")
    print("-" * 40)