from fetcher import fetch_latest_lotto_data, get_latest_lotto_number
from analyzer import analyze_frequencies
from recommender import recommend_today_numbers
from intro import show_intro
from calculator import check_win_probability

def main():
    # 인트로 메시지 출력
    show_intro()

    while True:
        # 메인 메뉴 출력
        print("\n" + "=" * 60)
        print(" 1️⃣ 회차 수 입력 후 통계 분석")
        print(" 2️⃣ 번호 입력 후 당첨 확률 확인")
        print(" 3️⃣ 오늘의 당첨 예측 번호 (통계 기반)")
        print(" 0️⃣ 프로그램 종료")
        print("=" * 60)

        # 사용자 입력 받기
        choice = input("선택 (0~3): ")

        if choice == "1":
            # 최신 회차 번호 조회
            latest_no = get_latest_lotto_number()

            # 사용자에게 수집할 회차 수 입력 받기 (유효성 검사 포함)
            while True:
                try:
                    user_input = int(input(f"수집할 회차 수를 입력하세요 (최대 {latest_no}) : "))
                    if 1 <= user_input <= latest_no:
                        break
                    else:
                        print(f"1 이상 {latest_no} 이하의 숫자를 입력해주세요.")
                except ValueError:
                    print("숫자만 입력해주세요.")

            # 데이터 수집 및 통계 분석 실행
            print("\n데이터 수집 중...")
            fetch_latest_lotto_data(count = user_input)

            print("\n[ 로또 통계 분석 결과 ]")
            analyze_frequencies()

        elif choice == "2":
            # 사용자 번호 입력 요청
            print("\n분석할 로또 번호 6개를 입력해주세요")
            print("조건: 1~45 사이의 중복 없는 숫자 6개 (공백으로 구분)")
            try:
                # 입력 처리 및 검증
                nums = list(map(int, input("입력 : ").split()))
                if len(nums) != 6 or len(set(nums)) != 6 or not all(1 <= n <= 45 for n in nums):
                    raise ValueError

                # 당첨 분석 실행
                check_win_probability(nums)

            except ValueError:
                print("입력 형식 오류: 조건에 맞는 숫자 6개를 정확히 입력해주세요.")

        elif choice == "3":
            # 오늘의 당첨 예측 번호 출력
            print("\n이번 주 당첨 예측 번호 분석 중...")
            recommend_today_numbers()

        elif choice == "0":
            # 종료 처리
            print("\n프로그램을 종료합니다.")
            break

        else:
            # 잘못된 메뉴 선택 처리
            print("올바른 메뉴 번호를 입력해주세요.")

# 프로그램 진입점
if __name__ == "__main__":
    main()