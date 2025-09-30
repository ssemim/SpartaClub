"""
장훈이는 서점을 운영하고 있다.
서점에는 높이가 B인 선반이 하나 있는데 장훈이는 키가 매우 크기 때문에,
선반 위의 물건을 자유롭게 사용할 수 있다.
어느 날 장훈이는 자리를 비웠고,
이 서점에 있는 N명의 점원들이 장훈이가 선반 위에 올려놓은 물건을 사용해야 하는 일이 생겼다.
각 점원의 키는 Hi로 나타나는데,
점원들은 탑을 쌓아서 선반 위의 물건을 사용하기로 하였다.
점원들이 쌓는 탑은 점원 1명 이상으로 이루어져 있다.
탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고,
2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.
탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데
탑의 높이가 높을수록 더 위험하므로 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.
"""


def recur(idx, total_height):
    # idx는 인덱스 번호
    # total_height는 점원들 높이
    global min_answer  # 쌓았을때의 최소값 (전역 변수로 지름)

    # 1. 가지치기 조건
    if total_height >= B:  # 가지치기: B이상이면 더 이상 쌓지 마라
        min_answer = min(min_answer, total_height)
        return

    # 2. 종료 조건
    if idx == N:  # N명을 모두 고려했을 때
        return

    # 3. 재귀 조건
    recur(idx + 1, total_height + heights[idx])  # 탑에 포함 시키는 경우
    recur(idx + 1, total_height)  # 탑에 포함 안 시키는 경우


T = int(input())  # 테스트 케이스 수 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    # N은 점원 수
    # B는 선반 높이
    min_answer = 10000 * N  # 나올 수 없다면 최대 값으로
    recur(0, 0)
    print(f'#{test_case} {min_answer - B}')
