T = int(input())  # 테스트 케이스 받고

# idx = 단계 (공장 번호)
# selected = 내가 지금까지 생산한 제품번호 모음

# selected 배열을 공장 번호랑 횟수에 맞게 셋팅

# now_cost : 지금 돌아가고있는 비용
def perm(idx, selected, now_cost):  # 순열 만드는 함수 만들기

    global min_cost  # 전역 변수로 땡겨놓고

    # 2. 가지치기 조건 (중간에 계산하는 값이 이미 최소값을 넘었을 때)
    if now_cost >= min_cost:
        return

    # 1. 종료 조건 (길이가 N에 도달했을 때 -> 공장 끝까지 갔을 때)
    if idx == N:
        min_cost = min(now_cost, min_cost)
        return

    # 3. 재귀 조건 (1.넣는다 / 2. 안넣는다)
    for j in range(N):
        # idx번 공장에서 j번 제품
        if j not in selected:  # 생산한 적 없으면 만들기 가능
            selected.append(j)
            # j번 제품을 idx번 공장에서 생산하고 비용 추가
            new_cost = now_cost + arr[j][idx]
            # idx + 1 빈공장으로 (다음 단계), 생성한 제품 번호 목록, 지금까지 생산 비용
            perm(idx + 1, selected, new_cost)
            selected.pop()  # j번 제품 생산 기록 취소

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    N = int(input())  # 제품 공장 갯수

    arr = [list(map(int, input().split())) for _ in range(N)]
    # 공장 개수와 한 줄씩 공장별 생산비용을 2차원 배열로

    # 공장 순서는 고정시켜놓고, 제품 순서만 바꿔서 순열 만들고
    # 거기서 만드는 비용 전부 계산해서 합친다음에 최소값을 뱉어

    min_cost = float('inf')  # 초기 최소값 설정
    perm(0, [], 0)
    print(f'#{test_case} {min_cost}')