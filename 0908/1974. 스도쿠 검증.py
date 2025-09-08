"""
스도쿠는 숫자퍼즐로,
가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한,
1 에서 9 까지의 숫자가 겹치지 않아야 한다.
입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우,
1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

[제약 사항]
1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.

"""

# 아니 이게 ㅜ머야

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서
    # 모든 스도쿠가 1~9까지 하나씩 있는거 만족이냐?
    # 만족일시 1 아닐시 0

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 가로세로 9줄

    element = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 스도쿠 요소들 저장용 배열

    is_sudoku = 1  # 이게 맞는 스도쿠인가 저장할 변수

    # 1. 가로가 1~9까지 다 있는가?

    for arg in sudoku:
        # 이러면 arg 자체가 하나의 행렬
        if sorted(arg) != element:  # 정렬시켰을 때 요소들이 다르다면
            is_sudoku = 0
            break  # 틀린거니까 제껴

        # 2. 세로가 1~9까지 다 있는가?
        # 가로 검사 다 통과한 상태에서
    for i in range(9):
        temp_arr = []  # 이거 행렬 검사용 임시 배열 (열바뀔때마다 초기화)
        for j in range(9):
            # 세로검사를 위해 2중 포문을 돌려보자
            # 두번째 for 문 안에서
            nums = sudoku[j][i]  # 이러면 세로행이 우선
            temp_arr.append(nums)  # 집어넣고

        temp_arr.sort()  # 오름차순으로 정렬하고
        if temp_arr != element:  # 요소들이 다르다면
            is_sudoku = 0
            break  # 틀린거니까 제껴

    # 3. 가로세로 3따리 행렬안에 1~9가 다 있는가?
    # 가로세로 검사 모두 통과한 상황
    # 이중 포문 돌면서 3개씩 범위 잘라서 검사하자
    for k in range(0, 9, 3):  # 행 시작점 (0, 3, 6)
        for l in range(0, 9, 3):  # 열 시작점 (0, 3, 6)
            temp_arr = []  # 임지 저장용 배열
            for x in range(k, k + 3):  # 3칸 범위씩 와리가리
                for y in range(l, l + 3):
                    temp_arr.append(sudoku[x][y])

            if sorted(temp_arr) != element: # 정렬한거랑 다르면
                is_sudoku = 0  # 스도쿠 틀렸슴
                break  # 또 제끼

    print(f'#{test_case} {is_sudoku}')
