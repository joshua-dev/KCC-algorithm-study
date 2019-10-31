"""
저울추가 담긴 배열 weight가 매개변수로 주어질 때, 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값을 return 하도록 solution 함수를 작성해주세요.

예를 들어, 무게가 각각 [3, 1, 6, 2, 7, 30, 1]인 7개의 저울추를 주어졌을 때, 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21입니다.

제한 사항
저울추의 개수는 1개 이상 10,000개 이하입니다.
각 추의 무게는 1 이상 1,000,000 이하입니다.
"""
def solution(weight):
    answer = 1
    weight.sort()
    for i in range(len(weight)):
        if answer < weight[i]:
            break
        else:
            answer += weight[i]
    return answer