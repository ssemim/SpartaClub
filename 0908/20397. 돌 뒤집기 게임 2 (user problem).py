"""
동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고,
게임의 규칙은 다음과 같다.
i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해,
각각 같은 색이면 뒤집고,
다른 색이면 그대로 둔다.
주어진 돌을 벗어나는 경우 뒤집기는 중지된다.
"""

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    N, M = map(int, input().split())  # N이랑 M 개수 받고
    # N = 돌의 개수
    # M = 돌 뒤집는 조건 수

    rocks = list(map(int, input().split()))

    for k in range(M):  # 돌 뒤집는 조건 수 범위 안에서 돌면서

        i, j = map(int, input().split())  # i랑 j 받아주고

        for l in range(1, j + 1):  # i를 기준으로 양옆 l칸씩
            left = i - l
            right = i + l

            # 범위 벗어나면 중단
            if left < 1 or right > N:
                break

            # 같은 색이면 뒤집기
            if rocks[left - 1] == rocks[right - 1]: # 양 사이드에 돌맹이 같으면
                rocks[left - 1] = 1 - rocks[left - 1]  # 0이면 1이고 1이면 0 왼쪽꺼
                rocks[right - 1] = 1 - rocks[right - 1] # 이건 오른쪽꺼
            else:
                continue  # 다르면 그대로 두고 다음 쌍 검사

    answer = ' '.join(map(str, rocks))
    print(f'#{test_case} {answer}')
