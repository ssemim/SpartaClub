"""
N X N크기의 농장이 있다.
이 농장에는 이상한 규칙이 있다.
규칙은 다음과 같다.
   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)
   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.
"""

# 진짜 이상한 규칙이라고 생각합니다
T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서
    N = int(input())  # 밭의 가로세로 길이

    farm = [list(map(int, input().strip())) for _ in range(N)]

    # 숫자 있는거나 주르륵 받아서 2차원 배열로 밭 세팅해주고
    # 정사각형이니까 가운데 행(열)을 c라고 한다면
    # 아니 생각해보니까 데칼코마니잖아 쿨하게 반으로 갈라버리자

    half = N // 2  # 반갈죽

    # 그러면, 어차피 마름모꼴이라 행렬 따로 복잡하게 생각 할 필요 없어 짱인데?
    # 가운데 줄 딱 빼고, 그 앞이랑 그 뒤만 먼저 더해보자

    total_sum = 0  # 농작물 이득 저장할 변수 만들고

    print(f"DEBUG farm: {farm}")
    print(f"DEBUG total_sum before calculation: {total_sum}")

    for i in range(N):  # 행 돌면서
        
        for j in range(N): # 양 사이드로 그 거리만큼 줄면서
            if abs(i-half) + abs(j-half) <= half:
                total_sum+= farm[i][j] # 이득 얼마인지 누적 고


    print(f"#{test_case} {total_sum}")