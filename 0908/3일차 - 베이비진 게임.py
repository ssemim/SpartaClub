"""
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.
"""


# 이거 그리디? 로 어케풀어 트리플렛 먼저 체크하는 방식
# 재귀는 아닌거지?

T = int(input())  # 테스트 케이스 수 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    card = list(map(int, input().split())) # 카드 받고

    card_count1 = [0] * 10  # 플레이어1 카운트
    card_count2 = [0] * 10  # 플레이어2 카운트

    winner = 0 # 일단 아무도없으면 0뽑으래

    for i in range(12): # 카드 12장 뺑이
        if i % 2 == 0:  # 플레이어1 일때 (돌아가면서 뽑으니까)
            card_count1[card[i]] += 1 # 수 세고

            for j in range(10): # 카드 0부터 9까지
                # 트리플렛으로 이김
                if card_count1[j] >= 3:
                    winner = 1
                    break
                # 런으로 이김
                if j < 8 and card_count1[j] > 0 and card_count1[j + 1] > 0 and card_count1[j + 2] > 0:
                    winner = 1
                    break
            if winner: # 1이 이겼으니까 실행 끝
                break


        else:  # 플레이어2
            card_count2[card[i]] += 1


            for j in range(10):  #위랑 또각ㅌ음
                # 트리플렛으로 이김
                if card_count2[j] >= 3:
                    winner = 2
                    break
                # 런으로
                if j < 8 and card_count2[j] > 0 and card_count2[j + 1] > 0 and card_count2[j + 2] > 0:
                    winner = 2
                    break
            if winner: # 2가 이겼으니까 실행 끝
                break

    print(f"#{test_case} {winner}")