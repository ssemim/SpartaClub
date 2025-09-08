"""
영준이는 당근 크기 선별기를 이용해 수확한 순서대로 당근의 크기를 기록하였다.
이 당근 선별기에는 특별한 기능이 있는데 연속으로 당근의 크기가 커진 경우 그 개수를 알려준다. 당근의 크기가 수확한 순서로 주어질 때,
 선별기가 알려준 연속으로 커지는 당근의 갯수는 최대 얼마인지 확인하기 위한 프로그램을 만드시오.

 연속으로 커지지않는 경우 구간의 최소 길이는 1이다.
N개의 당근을 수확하며, 당근의 크기 C는 1부터 10까지의 정수로 정해진다.
5<=N<=1000, 1<=C<=10
"""

T = int(input())  # 테스트 케이스 수 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    N = int(input())  # 아니 당근 갯수 받는걸 까먹음

    carrots = list(map(int, input().split()))  # 당근 크기 받고

    # 연속으로 커지지 않는 경우 구간 최소 길이는 1이므로
    carrot = 1

    # 아니 최대값도 까먹었네 덜렁거림 ㄹㅈㄷ
    max_carrots = 1

    # 연속으로 커지는 당근 갯수는?

    for i in range(len(carrots) - 1):  # 당근들 길이만큼 돌면서
        if carrots[i] < carrots[i + 1]:  # 단조증가면
            carrot += 1  # 하나씩 플러스 해주고
            if carrot >= max_carrots: # 최대값도 구해주고
                max_carrots = carrot
        else:  # 단조증가 아니면
            carrot = 1  # 다시 1로 리셋


    print(f'#{test_case} {max_carrots}')
