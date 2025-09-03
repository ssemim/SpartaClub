"""
원재가 컴퓨터를 만지다가 실수를 저지르고 말았다. 메모리가 초기화된 것이다.
다행히 원래 메모리가 무슨 값이었는지 알고 있었던 원재는 바로 원래 값으로 되돌리려고 했으나
메모리 값을 바꿀 때 또 문제가 생겼다.
메모리 bit중 하나를 골라 0인지 1인지 결정하면
해당 값이 메모리의 끝까지 덮어씌우는 것이다.

예를 들어 지금 메모리 값이 0100이고,
3번째 bit를 골라 1로 설정하면 0111이 된다.
원래 상태가 주어질 때 초기화 상태 (모든 bit가 0) 에서
원래 상태로 돌아가는데 최소 몇 번이나 고쳐야 하는지 계산해보자.

원래 값으로 복구하기 위한 최소 수정 횟수를 출력한다.
"""

# 원재 안타깝긔

T = int(input())  # 테스트 케이스 받고
for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    final_memory = list(map(int, input().strip()))  # 목표 메모리 배열로 받아주고

    # 하나 건들면 그 인덱스부터 끝까지 똑같아진다는거지

    memory_long = len(final_memory)
    now_memory = [0] * memory_long  # 초기 메모리 상태 만들어주고
    now = 0  # 몇 번째 메모리 보고있는지 저장할 변수
    count = 0  # 몇 번 변하는지 저장할 변수

    while now < memory_long:  # 범위 안 넘을때 반복문 돌면서
        if final_memory[now] == now_memory[now]:
            now += 1
            # 지금 서로 마주보고 있는 메모리의 값이 같으면 다음칸으로
        else:  # 메모리의 값이 같지 않다면
            now_memory[now] = final_memory[now]  # 지금 메모리에 목표 메모리 값 넣고
            for i in range(now, memory_long):  # 반복문 돌면서
                now_memory[i] = final_memory[now]  # 뒤에 있는 놈들 전부 지금 메모리로 덮어씌워
            count += 1  # 변했다고 표시하고
            now += 1  # 이것도 돌았으면 다음 칸으로

        if final_memory == now_memory:  # 지금 값이랑 최종값 똑같아지면
            break  # 탈출

    print(f'#{test_case} {count}')
