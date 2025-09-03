T = int(input())

for test_case in range(1, 1 + T):
    N, hex_string = input().split()
    N = int(N)

    # N만 숫자로 바꿈

    # 16진수 => 2진수
    # 변환표 만들어두기

    hex_to_bin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    # 결과로 만들 2진수 문자열
    result_bin = ''

    # 변환표 참고해서 2진수로 바꾸기
    # 배열 만들어서 따로 집어넣어야하나?

    for arg in hex_string:
        result_bin += hex_to_bin[arg]

    print(f'#{test_case} {result_bin}')