"""
N개의 16진수의 합을 구하는 프로그램을 작성하시오.
주어진 16진수의 가장 처음에 있는 숫자는 항상 0이 아니다.
주어진 테스트케이스의 해설)
D => D(13) = 13
27 => 2 + 7 = 9
B56 => B(11) + 5 + 6 = 22
1 <= N <= 20
"""

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    N = int(input())
    # N은 16진수 문자열의 길이

    hex_string = list(map(str, input().strip()))

    # 그리고 16진수 문자열 받음
    # 문자열 변환용 딕셔너리 만들어볼까나

    hex_sum = 0  # 16진수 10진수로 변환한 값 저장할 변수 (누적합 시킬거임)

    hex_dictionary = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15

    }

    for arg in hex_string:
        hex_sum += hex_dictionary[arg]

    print(f'#{test_case} {hex_sum}')
