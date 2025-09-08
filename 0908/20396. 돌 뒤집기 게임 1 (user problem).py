"""
동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고, 게임의 규칙은 다음과 같다.
뒤집기는 i번째부터 j개의 돌을 i번째 돌의 색으로 바꿔놓는다.
뒤집기는 가능한 돌에 대해서만 진행한다.
"""

T = int(input())  # 테스트케이스 수 받고

for test_case in range(1, 1 + T):  # 테스트 케이스 돌면서
    N, M = map(int, input().split())  # N과 M받고
    # N = 돌 개수
    # M = 돌 뒤집는 조건 수

    rocks = list(map(int, input().split()))  # 초기 돌 상태 받고

    for k in range(M):  # M개의 돌 뒤집기 조건 안에서
        i, j = map(int, input().split())  # i와 j 받고

        # i 번째 돌부터 (i번째 돌 색으로 뒤집음)
        # j 개의 돌을 뒤집는다
        # 이거 돌이 0번부터 있는게 아니라 1번 부터 시작하네
        for l in range(i - 1, i - 1 + j):  # 돌멩돌멩
            if l < N:
                rocks[l] = rocks[i - 1]
                # 돌맹이 범위 내에서만 덮어쓰기

    answer = ' '.join(map(str, rocks))
    # 다뒤집고 출력
    print(f"#{test_case} {answer}")
