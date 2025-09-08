"""
정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.
그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.
예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
양의 정수 N 개 A1, …, AN이 주어진다.
 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.
"""

T = int(input())  # 테스트 케이스 수 받고

for test_case in range(1, T + 1):  # 테스트 케이스 수 만큼 돌면서
    N = int(input())  # 받는 숫자들 길이 받고

    nums = list(map(int, input().split()))  # 숫자들 받아주고

    # 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는걸 구해야함
    dan_product = []  # 이건 단조증가값 저장용 변수
    max_product = -1 # 에라이

    for i in range(1, N):  # 첫번째 숫자 i
        for j in range(i + 1, N):  # 그리고 i보다 더 큰 숫자 j

            is_dan = True  # 단조증가 하나?

            product = nums[i] * nums[j]  # 그러면 곱은 배열의 i번째랑 j번째 곱한거
            multi = str(product)  # 곱한 값 문자열로 바꿔주고

            for c in range(len(multi) - 1):  # 문자열값 길이만큼 돌면서
                if multi[c] > multi[c + 1]:  # 단조증가 아니라면
                    is_dan = False
                    break  # 버려

            if is_dan:  # for문 길이 다 돌았을때 모든 자리수가 단조증가 하는거 맞으면
                if max_product < product:
                    max_product = product

    print(f'#{test_case} {max_product}')
