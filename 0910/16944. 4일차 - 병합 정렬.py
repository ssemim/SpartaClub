"""
알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.
정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에
다음과 같은 제약을 주었다.
N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.
병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.

정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.
알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.
"""


# 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할

def merge_sort(left, right):
    # 1. 종료 조건
    # 더 이상 분할이 불가능 할 때 까지
    if left == right - 1:
        # 길이가 1이면 분할 불가능
        return left, right

    mid = (left + right) // 2  # 가운데 분할 지점

    # 2. 재귀 호출문
    left_s, left_e = merge_sort(left, mid)
    right_s, right_e = merge_sort(mid, right)
    # 3. 합치면 된다
    merge(left_s, left_e, right_s, right_e)

    # 합치고 나면 정렬 완료

    return left, right


def merge(left_s, left_e, right_s, right_e):
    global cnt

    # 병합되는 리스트의 크기
    n = right_e - left_s

    # 병합되는 리스트, 리스트의 인덱스
    result = [0] * n
    idx = 0

    # 왼쪽 리스트의 시작 인덱스(왼쪽 리스트의 가장 작은 원소)
    l = left_s
    # 오른쪽 리스트의 시작 인덱스(오른쪽 리스트의 가장 작은 원소)
    r = right_s

    # 1. 비교할 왼쪽 오른쪽이 둘 다 남아있는 경우
    while l < left_e and r < right_e:
        if L[l] < L[r]:
            result[idx] = L[l]
            l += 1
            idx += 1

        else:
            result[idx] = L[r]
            r += 1
            idx += 1

        # 2-1. 오른쪽만 남아있는 경우
    while r < right_e:
        result[idx] = L[r]
        r += 1
        idx += 1

        # 2-2. 왼쪽만 남아있는 경우
    while l < left_e:
        result[idx] = L[l]
        l += 1
        idx += 1

    # N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰지 확인 (이거 횟수 세야함)
    if L[left_e - 1] > L[right_e - 1]:
        cnt += 1

    # 병합된 결과 주르륵 돌리면서 넣(?)
    for i in range(n):
        L[left_s + i] = result[i]


T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 범위 돌면서

    N = int(input())  # N개의 정렬 대상

    L = list(map(int, input().split()))  # 정렬 대상을 일단 받음

    cnt = 0

    merge_sort(0, N)

    print(f'#{test_case} {L[N // 2]} {cnt}')
