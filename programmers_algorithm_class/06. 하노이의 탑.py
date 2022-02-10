'''
Q.

하노이의 탑(Tower of Hanoi)은 퍼즐의 일종이다. 
세 개의 기둥과 이 기둥에 꽂을 수 있는 크기가 다양한 원판들이 있고, 
퍼즐을 시작하기 전에는 한 기둥에 원판들이 작은 것이 위에 있도록 순서대로 쌓여 있다.

게임의 목적은 다음 두 가지 조건을 만족시키면서, 
한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것이다.

한 번에 하나의 원판만 옮길 수 있다.
큰 원판이 작은 원판 위에 있어서는 안 된다.


하노이의 탑 문제는 재귀 호출을 이용하여 풀 수 있는 가장 유명한 예제 중의 하나이다. 
그렇기 때문에 프로그래밍 수업에서 알고리즘 예제로 많이 사용한다. 
일반적으로 원판이 n개 일 때, 2n -1번의 이동으로 원판을 모두 옮길 수 있다(2n − 1는 메르센 수라고 부른다).

'''

# 입력:  옮기려는 원반의 개수 n
# 옮길 원반이 현재 있는 출발점 기둥 from_pos
# 원반을 옮길 도착점 기둥 to_pos
# 옮기는 과정에서 사용할 보조 기둥 aus_pos
# 출력: 원반을 옮기는 순서

def hanoi(n,from_pos, to_pos, aux_pos):
    if n == 1: # 원반이 한 개
        print(from_pos, '->' , to_pos)
        return
    
    # 원반 n-1 개를 aux_pos로 이동 (to_pos를 보조 기둥으로)
    hanoi(n-1, from_pos, aux_pos, to_pos)
    
    # 가장 큰 원반을 목적지로 이동
    print(from_pos, '->', to_pos)
    
    #aux_pos에 있는 원반 n-1개를 목적지로 이동 (from_pos를 보조 기둥으로)
    hanoi(n-1, aux_pos, to_pos, from_pos)
    

print('n=1')
hanoi(1,1,3,2) # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동 (2번을 보조 기둥으로)

print('n=2')
hanoi(2,1,3,2) # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동 (2번을 보조 기둥으로)

print('n=3')
hanoi(3,1,3,2) # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동 (2번을 보조 기둥으로)

'''
[OUTPUT]
n=1
1 -> 3

n=2
1 -> 2
1 -> 3
2 -> 3

n=3
1 -> 3
1 -> 2
3 -> 2
1 -> 3
2 -> 1
2 -> 3
1 -> 3
'''