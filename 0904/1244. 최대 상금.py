"""
교환 횟수만큼 자리 교환을 해서 만들 수 있는 가장 큰 수 찾아야함
"""


def go_change():


T = int(input())  # 테스트 케이스 받고
for test_case in range(1, T + 1):  # 돌면서
    num, change = input().split()  # 숫자판 정보, 교환횟수
    num_list = list(num)  # 문자열을 리스트로 (교환 날먹용)
    change = int(change)  # 교환 횟수 (정수)
    visited = set()  # 방문 기록 저장용

    result = go_change()  

    print(f"#{test_case} {result}")


#몰루,,,,,,,,,,,,,,,,,,,,,,,,,,,,(캐졸리니가 내일다시하자)