from fetcher import fetch_latest_lotto_data
from analyzer import analyze_frequencies
from recommender import recommend_numbers

if __name__ == "__main__":
    print("🔍 로또 데이터 수집 중...")
    fetch_latest_lotto_data(count=1100)  # 최신 1100회차까지 수집

    print("\n📊 통계 분석:")
    analyze_frequencies()

    print("\n🎲 랜덤 번호 추천:")
    recommend_numbers()