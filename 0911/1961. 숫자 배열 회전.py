"""
N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
"""

T = int(input())  # 테스트 케이스 받고


def rotate_90(matrix, N):
    rotated = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[i][j] = matrix[N - 1 - j][i]
    return rotated


def rotate_180(matrix, N):
    rotated = rotate_90(rotate_90(matrix, N), N)
    return rotated


def rotate_270(matrix, N):
    rotated = rotate_90(rotate_90(rotate_90(matrix, N), N), N)
    return rotated


for test_case in range(1, T + 1):  # 케이스 범위 돌면서

    N = int(input())  # 행렬의 가로세로 개수

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 2차원 배열 받아주고

    # 1. 90도 회전
    # 1행 => 3열 / 2행 => 2열 / 3행 => 1열

    # 2. 180도 회전
    # 1행 => 3행 / 2행 => 2행 / 3행 => 1행

    # 3. 270도 회전
    # 아니 걍 90도 회전 함수 만들어서 두번 세먹 써먹을란다 짱나네

    r90 = rotate_90(matrix, N)
    r180 = rotate_180(matrix, N)
    r270 = rotate_270(matrix, N)

    print(f'#{test_case}')
    for i in range(N):
        print(
            ''.join(map(str, r90[i])),
            ''.join(map(str, r180[i])),
            ''.join(map(str, r270[i]))

        )
