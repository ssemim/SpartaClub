"""
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

"""

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서
    N = int(input())  # 수열의 길이

    arr = list(map(int, input().strip()))  # 공백 없이 배열 받아오고

    y_max = 0  # 최대 연속 한 개수
    y_now = 0  # 지금 연속한 개수

    for arg in arr:  # 배열 돌면서
        if arg == 1:  # 든게 1이면
            y_now += 1  # 지금연속에 쁠라스
        else:  # 1 아니면
            if y_now > y_max:  # 지금 연속이 최대 연속보다 크다면
                y_max = y_now  # 최대값 덮어쓰고
            y_now = 0  # 지금 연속 초기화

        if y_now > y_max:  # 지금 연속이 최대 연속보다 크다면
            y_max = y_now  # 최대값 또 덮어써 (위에있는건 else안에만 적용되는거니깐 또 써)

    print(f'#{test_case} {y_max}')
