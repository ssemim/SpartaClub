"""
A사는 여러 곳에 공장을 갖고 있다.
봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.
각 제품의 공장별 생산비용이 주어질 때
전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.
예를 들어 3개의 제품을 생산하려는 경우 각 공장별 생산비용은 다음과 같이 주어진다.
이때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.
"""

# 제품 번호의 순열을 만드는 문제
# 순서대로 앞 공장에 넣어서 비용 계산해서 최소 구하면 되는 문제다

T = int(input())  # 테스트 케이스 받고


# idx : 단계 / 공장의 번호 (여기서는)
# selected : 내가 지금까지 생산한 제품 번호 모음

# selected 배열을 공장 번호랑 횟수에 맞게 셋팅해주면 된다

# selected[j] => 몇 번 공장에서 얼마나 생산했니
# now_cost => 현재 단계까지 선택한 공장들의 비용 합
# idx번 공장에서 생산할 제품을 고르는 것이 문제
def perm(idx, selected, now_cost):  # 순열 만드는 함수

    global min_cost

    # 현재 단계까지 계산한 비용 now_cost가
    # 이전에 내가 계산한 최소 비용 min_cost보다 큰 경우, 답이 될 가능성이 없다
    if now_cost >= min_cost:
        return

        # 종료 조건
    if idx == N:  # 공장 끝번까지 가면 끝
        # 모든 공장에서 어떤 제품을 생산할건지 선택 완료
        # 최소 값을 비교해서 구하면 된다
        min_cost = min(now_cost, min_cost)
        return

        # 재귀 호출 (다음 단계)
        # idx번 공장에서 생산할 제품을 선택
        # 선택할 수 있는 가지 수 최대 N 개
        # 0~idx -1 번 공장에서 생산했던 제품은 선택 불가
        # 제품 번호 j
    for j in range(N):
        # idx번 공장에서 j번 제품 생산
        if j not in selected:  # 기록에 생산한 적 없으니까 생산할 수 있겠다
            selected.append(j)
            # j번 제품을 idx번 공장에서 생산했으니 비용 추가
            new_cost = now_cost + arr[j][idx]
            # idx + 1 빈공장으로 (다음 단계), 생성한 제품 번호 목록, 지금까지 생산 비용
            perm(idx + 1, selected, new_cost)
            selected.pop()  # j번 제품 생산 기록 취소


for test_case in range(1, T + 1):  # 테스트케이스 범위 만큼 돌면서

    # 제품 / 공장 개수
    N = int(input())

    # 생산 비용 표
    # arr[i][j] => i번 제품을 j번 공장에서 생산하는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 값은 최소 비용이므로
    min_cost = 15 * 100  # 일단 범위 밖으로 크게 세팅해두고

    # 공장 순서는 고정 시켜놓고
    # 제품 순서만 바꿔서 순열을 만들고
    # 제품 공장에서 생산하는 제품의 생산 비용을 모두 계산해서 합친 후에
    # 그중에 최소를 구하면 된다

    perm(0, [], 0)
    print(f'#{test_case} {min_cost}')
