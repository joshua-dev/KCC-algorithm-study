"""
두 개의 리스트에서 하나씩 꺼내서 최대 곱을 만드는 문제.
EX) A = [1,2,3], B = [4,5,6]
이라면 A와 B에서 하나씩 꺼내서 곱을 하고 더하는 문제
여기서는 3*6 + 2*5 + 1*4 가 최대 값이 됨으로
32가 정답이다.
"""

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    B.reverse()
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer