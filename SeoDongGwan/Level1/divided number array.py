'''
나누어 떨어지는 숫자 배열

문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.
'''

def solution(arr,divisor):

    answer=[]

    for i in arr:  # 어레이의 값을 순차적으로 받는다.

        if (i%divisor) == 0: #어레이의 값이 divisor와 나눴을때 나머지가 0이면 answer어레이에 그 값을 추가
            answer.append(i)

    if len(answer) == 0: #만약 어레이가 비어있다면 -1을 추가
        answer.append(-1)

        
    answer.sort() # 최종 숫자 배열을 정렬

    return answer
