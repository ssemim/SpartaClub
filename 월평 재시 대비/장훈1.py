T = int(input())


def recur(idx, total_height):
    global min_answer  # 쌓았을때의 최소값 (전역 변수로 지름)

    # 2. 가지치기 조건
    if total_height >= B:
        # 최소 키가 최대높이인 B를 초과한다면 종료
        min_answer = min(min_answer, total_height)
        # 그래도 조건은 만족하는거니까, min으로 최소값에 해당하는지 체크
        return
    # 1. 종료 조건
    if idx == N:
        return  # 직원들 끝까지 다 고려했으면 종료

    # 3. 재귀 조건
    recur(idx + 1, total_height + heights[idx])  # 지금 해당되는 직원의 키를 더한다
    recur(idx + 1, total_height)  # 지금 해당되는 직원의 키를 더하지 않는다


for test_case in range(1, T + 1):
    N, B = map(int, input().split())

    # N은 점원들 수
    # B는 최대 높이

    heights = list(map(int, input().split()))
    # 직원들 키 받고
    min_answer = 100000000000000
    # 최소값 초기화 세팅

    recur(0, 0)
    print(f'#{test_case} {min_answer - B}')
