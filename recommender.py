# recommender.py
import random

def recommend_numbers():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    print("🎯 추천 번호:", numbers)
    return numbers
