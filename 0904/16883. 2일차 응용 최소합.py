T = int(input())
# 우 하
di = [0, 1]
dj = [1, 0]


# 현재위치 (i,j) i는 행번호, j는 열번호
# (0,0) => 우 or 하 이동 반복 => (N-1,N-1)
# now_sum : (i,j) 까지 오면서 더해왔던 누적 합
def solve(i, j, now_sum):
    global min_sum

    # 가지치기
    if min_sum < now_sum:
        return

    # 종료
    if (i, j) == (N - 1, N - 1):
        # 도착했으니 합을 구하고
        # 그 합이 최소인가?
        min_sum = min(now_sum, min_sum)
        return

    # 재귀호출(다음단계)
    # 방향 선택지 2개 => 재귀호출도 2개
    # 오른쪽 or 아래
    for d in range(2):
        # d 방향으로 이동한 후 위치
        ni, nj = i + di[d], j + dj[d]
        # (ni, nj) 가 유효한 인덱스인지 검사
        if 0 <= ni < N and 0 <= nj < N:
            # 유효한 위치면 (ni,nj)로 이동, 합 추가
            solve(ni, nj, now_sum + matrix[ni][nj])


for tc in range(1, T + 1):
    # 가로세로 크기
    N = int(input())

    # N * N 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답: 합이 최소가 되도록
    min_sum = 10000000

    # 재귀호출
    # (0,0) 에서 이동 시작하고, (0,0) 위치에 있던 숫자를 합에 더함
    solve(0, 0, matrix[0][0])

    print(f"#{tc} {min_sum}")


# 분명 들었는데 혼자 다시 보니까 먼말인지 하나도 몰겠다 큰일