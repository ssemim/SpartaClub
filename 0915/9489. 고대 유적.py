T = int(input())  # 테스트 케이스받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서
    N, M = map(int, input().split())  # N은 세로 M은 가로
    arr = [list(map(int, input().split())) for _ in range(N)]  # 맵 세팅 해주고
    longest = 0  # 젤 긴 구조물 길이 저장할 변수

    for i in range(N):  # 일단 행에 대해서
        cnt = 0  # 길이 카운트용 변수
        for j in range(M):  # 한 줄 돌면서
            if arr[i][j] == 1:  # 이어져있으면
                cnt += 1  # 누적
            else:
                cnt = 0  # 초기화

            if longest < cnt:  # 카운트 한게 지금 최대보다 크면
                longest = cnt  # 갱신

    for j in range(M):  # 뭐 밑도 똑같음 
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0

            if longest < cnt:
                longest = cnt

    if longest == 1:  # 구조물 한 칸 따리면
        longest = 0  # 걍 없다고 0출력함

    print(f'#{test_case} {longest}')
