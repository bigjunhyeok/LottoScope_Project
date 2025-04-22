# analyzer.py
import pandas as pd
from collections import Counter

def analyze_frequencies(path="data/lotto_data.csv"):
    df = pd.read_csv(path)
    numbers = []

    for i in range(1, 7):
        numbers.extend(df[f"번호{i}"].tolist())
    counter = Counter(numbers)
    most_common = counter.most_common()

    print("🔢 출현 빈도 상위 번호:")
    for num, count in most_common[:10]:
        print(f"{num:>2}번 → {count}회")
