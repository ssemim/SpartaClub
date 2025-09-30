T = int(input())  # 테스트 케이스 받고


def recur(idx, total_height):
    global min_height  # 최소 키 합 전역 변수로 선언
    # 1. 가지치기 조건
    if total_height >= B:  # 총 키 합이 B를 초과하면 중단하긴 하는데 일단 조건은 맞으니까
        min_height = min(min_height, total_height)

    # 2. 종료 조건
    if idx == N:  # 점원 수 만큼 다 돌았다면
        return
    # 3. 재귀 조건
    recur(idx + 1, total_height + heights[idx])  # 지금 선택된 직원의 키를 넣는다
    recur(idx + 1, total_height)  # 안 넣는다


for test_case in range(1, T + 1):
    N, B = map(int, input().split())

    # N은 정수 개수
    # B는 최대 키

    heights = list(map(int, input().split()))
    # 점원들 키 받고
    min_height = 10000000000000000  # 최소값 초기ㅣ화 해주고
    recur(0, 0)  # 재귀로 불러서 계산 시작 (부분집합 합 구하는거니까)

    print(f'#{test_case} {min_height - B}')
