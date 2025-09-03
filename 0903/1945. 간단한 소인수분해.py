"""
숫자 N은 아래와 같다.
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.

[제약 사항]
N은 2 이상 10,000,000 이하이다.
"""

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서
    N = int(input())  # 이게 나눠야하는 숫자

    arr = [11, 7, 5, 3, 2]  # 인수 저장용 배열

    result = []  # abcde 저장용 배열
    # 11로 나누고
    # 7로 나누고
    # 5로 나누고
    # 3으로 나누고
    # 2로 나누고
    # 큰걸로 먼저 조져주면 되려나?

    for arg in arr:
        count = 0  # 몇 번 곱하는지 저장할 변수
        while (N % arg) == 0: # N이 나누어 떨어지는 한 계속 돌면서
            count += 1 # 나눈 횟수에 + 1
            N = N // arg # 그리고 N은 arg로 나눈게 된다 (한번 나눴자나)
        result.append(count) # while 끝나면 카운트 수 뱉어주
    result.reverse() # 11부터 나눴는데 a는 2, b는 3 일케 작은거 부터니까 뒤집
    print(f'#{test_case} {" ".join(map(str, result))}')
    # 조인붙이는법 또까먹었네 돌겠다 (따옴표좀 조심해)
