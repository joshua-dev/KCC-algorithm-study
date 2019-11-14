"""
종이를 접은 횟수 n이 매개변수로 주어질 때, 종이를 절반씩 n번 접은 후 모두 펼쳤을 때 생기는 접힌 부분의 모양을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
종이를 접는 횟수 n은 1 이상 20 이하의 자연수입니다.
종이를 접었다 편 후 생긴 굴곡이 ∨ 모양이면 0, ∧ 모양이면 1로 나타냅니다.
가장 왼쪽의 굴곡 모양부터 순서대로 배열에 담아 return 해주세요.
입출력 예
n	result
1	[0]
2	[0,0,1]
3	[0,0,1,0,0,1,1]

"""
def solution(n):
    answer = []
    f = 0
    while f != n:
        answer.append(0)
        f += 1
        if f > 1:
            for i in range(2**(f-1)-2,-1,-1):
                if answer[i] == 0:
                    answer.append(1)
                elif answer[i] == 1:
                    answer.append(0)
    return answer