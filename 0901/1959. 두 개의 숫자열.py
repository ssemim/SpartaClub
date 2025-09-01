T = int(input())  # 테스트 케이스 수 받고

for test_case in range(1, T + 1):  # 케이스만큼 돌면서
    N, M = map(int, input().split())  # N은 짧은 배열 길이 # M은 긴배열 길이
    A = list(map(int, input().split()))  # 짧은 배열 받고
    B = list(map(int, input().split()))  # 긴 배열 받고

    # 무조건 A가 더 짧도록 셋팅
    if N > M:
        A, B = B, A  # 배열 바꿔줘용
        N, M = M, N  # 길이도 바꿔줘용

    max_sum = float('-inf')  # 제일 작을 수 있는 수로 설정하고

    for i in range(M - N + 1):  # 무빙칠 위치 찍고 (맨 마지막에 시작할 i 기준임) 큰 배열이니가
        current_sum = 0  # 현재 위치 곱 합을 저장할거
        for j in range(N):  # 짧은거도 돌면서
            current_sum += A[j] * B[i + j]  # A의 j번째랑 B의 i+j 번째 곱해서 저장

        if current_sum > max_sum:
            max_sum = current_sum  # 지금꺼가 더 크면 덮어쓰기

    print(f"#{test_case} {max_sum}")
