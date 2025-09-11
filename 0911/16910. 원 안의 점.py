import math

"""
N이 주어질 때, 원점을 중심으로
반지름이 N인 원 안에 포함되는 격자점
(x,y 좌표가 모두 정수인 점)의 개수를 구하는 프로그램을 작성하라.
다시 말하자면, x2+y2<=N2인 격자점의 개수를 구하는 프로그램을 작성하라.
"""

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트케이스 돌면서
    N = int(input())  # 반지름 길이 N 받고

    # x^2 + y^2 = N^2 인 원 안에 x,y좌표가 모두 정수인 점을 구해
    # 원의 중심은 (0,0)
    # 점의 개수만 출력하면 돼

    point = 0  # 격자점 개수 저장할 변수

    for x in range(-N, N + 1):  # -N부터 N까지 돌면서
        for y in range(-N, N + 1):
            if math.pow(x, 2) + math.pow(y, 2) <= math.pow(N, 2):
                point += 1  # 만족하면 +1씩 누적

    print(f'#{test_case} {point}')
