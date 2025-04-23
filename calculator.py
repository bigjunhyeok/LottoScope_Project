import pandas as pd
from collections import Counter

def check_win_probability(user_numbers, path = "data/lotto_data.csv", recent_count = 100):
    """
    사용자가 입력한 번호에 대해:
    1. 과거 당첨 결과를 분석하고 (등수, 확률 % 포함)
    2. 최근 회차 출현 빈도 기반으로 예측 가능성도 보여줍니다

    Parameters:
        user_numbers (list[int]): 사용자가 입력한 번호 6개
        path (str): 로또 데이터 CSV 경로
        recent_count (int): 최근 회차 기준 출현 통계 범위
    """
    # CSV 불러오기
    df = pd.read_csv(path)

    # --- 1. 과거 당첨 결과 분석 ---
    result_stats = {
        "1등": 0,
        "2등": 0,
        "3등": 0,
        "4등": 0,
        "5등": 0,
        "꽝": 0
    }

    # 회차별 비교
    for _, row in df.iterrows():
        winning_numbers = [row[f"번호{i}"] for i in range(1, 7)]
        bonus_number = row["보너스"]
        match_count = len(set(user_numbers) & set(winning_numbers))

        if match_count == 6:
            result_stats["1등"] += 1
        elif match_count == 5:
            if bonus_number in user_numbers:
                result_stats["2등"] += 1
            else:
                result_stats["3등"] += 1
        elif match_count == 4:
            result_stats["4등"] += 1
        elif match_count == 3:
            result_stats["5등"] += 1
        else:
            result_stats["꽝"] += 1

    total_rounds = sum(result_stats.values())

    print("\n🔍  입력한 번호의 과거 당첨 분석 :")
    print("-" * 45)
    for rank, count in result_stats.items():
        percent = (count / total_rounds) * 100
        reward = {
            "1등": "💸 약 20~30억 원",
            "2등": "💰 약 5천~7천만 원",
            "3등": "💵 약 150만 원",
            "4등": "📦 고정 5만 원",
            "5등": "📦 고정 5천 원",
            "꽝": "😭 아쉽지만 다음 기회에"
        }[rank]
        print(f"{rank} ({count}회, {percent:.2f}%) → {reward}")
    print("-" * 45)

    # --- 2. 최근 회차 출현 빈도 분석 ---
    df_recent = df.sort_values("회차", ascending = False).head(recent_count)

    all_recent_numbers = []
    for i in range(1, 7):
        all_recent_numbers.extend(df_recent[f"번호{i}"].tolist())

    counter = Counter(all_recent_numbers)

    print(f"\n📊  최근 {recent_count}회 기준, 입력한 번호 출현 빈도:")
    print("-" * 45)
    for num in user_numbers:
        count = counter.get(num, 0)
        level = "🔥 매우 자주 나옴" if count >= 10 else ("😊 적당히 등장" if count >= 5 else "🧊 드물게 등장")
        print(f"번호 {num:>2} → {count:>2}회 출현 ({level})")
    print("-" * 45)