"""
동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고,
게임의 규칙은 다음과 같다.
i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해,
각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

"""

"""
첫 줄에 게임의 개수 T, 
다음 줄부터 게임별로 첫 줄에 돌의 수 N, 뒤집기 횟수 M, 
다음 줄에 N개 돌의 초기상태, 이후 M개의 줄에 걸쳐 i, j가 주어진다.
"""

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    N, M = map(int, input().split())

    # N : 돌의 수
    # M : 뒤집기 횟수

    # 돌받아오자

    rocks = list(map(int, input().split()))

    # 배열에 집어넣고

    for _ in range(M):  # 뒤집을 횟수만큼 반복하면서
        i, j = map(int, input().split())
        # i번째 돌을 사이에 두고,
        # 마주보는 j개의 돌에 대해 뒤집긔
        # 인덱스는 0으로 시작하는게 맞더라 ㄱㅊ

        # 그러면 지금 돌은
        now_rock = rocks[i - 1]

        # 그리고 j개의 돌에 대해서
        for k in range(1, j + 1):  # j만큼
            left = i - k - 1  # 왼
            right = i + k - 1  # 오

            # 범위 밖이면 제낌
            if left < 0 or right >= N:
                break

            # 색이 같으면 둘 다 뒤집기
            if rocks[left] == rocks[right]:
                rocks[left] ^= 1
                rocks[right] ^= 1

    print(f'#{test_case} {" ".join(map(str, rocks))}')
