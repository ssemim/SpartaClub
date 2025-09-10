"""
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다.
그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지
이진 탐색을 통해 확인하려고 한다.
전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면,
중심 원소의 인덱스 m=(l+r)//2 이고, 이진 탐색의 왼쪽 구간은 l부터 m-1,
오른쪽 구간은 m+1부터 r이 된다.
이때 B에 속한 어떤 수가 A에 들어있으면서,
동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.
다음은 10개의 정수가 저장된 리스트 A에서 이진 탐색으로 6을 찾는 예이다.
"""


def binary_search(arr, target, l, r, prev_dir):
    if l > r:  # 탐색 범위를 벗어나면 아웃
        return False

    m = (l + r) // 2  # 중간값 찍고

    if arr[m] == target:  # 값 찾으면 참
        return True

    if arr[m] < target:
        # 오른쪽 구간을 탐색 ㄱ
        if prev_dir == 'left':
            # 이전에 왼쪽 지금 오른쪽: 번갈아가며 찾았음
            pass
        elif prev_dir == 'right':
            # 이전에 오른쪽 지금도 오른쪽: 아웃
            return False
        # 방향이 없거나 바뀐 경우에는 계속 ㄱ
        return binary_search(arr, target, m + 1, r, 'right')

    else:  # 왼쪽 ㄱ
        if prev_dir == 'right':
            # 이전에 오른쪽 지금 왼 : 번갈아가며 찾음
            pass
        elif prev_dir == 'left':
            # 이전에 왼쪽  지금도 왼쪽 : 아웃
            return False  # 또 돌아가
        return binary_search(arr, target, l, m - 1, 'left')


T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스를 돌면서

    N, M = map(int, input().split())  # 각각 정수 개수 받고

    A = list(map(int, input().split()))  # A 리스트 받고
    B = list(map(int, input().split()))  # B 리스트 받고

    # B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진탐색

    A.sort()  # 정렬하고
    count = 0  # 카운트값 저장할 변수 때리고

    for target in B:  # B 돌면서
        if binary_search(A, target, 0, N - 1, None):
            count += 1  # 조건 맞았을 때 마다

    print(f"#{test_case} {count}")
