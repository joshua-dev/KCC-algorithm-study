"""
소수만들기, nums에 1 2 7 6 4와 같은 수의 리스트가 들어가고
여기서 3개를 뽑아 소수를 만드는 경우의 수를 구하라

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
"""
some_list = []
def primeCheck(num):
    #소수 구하는 함수
    for i in range(2, num):
        if num%i == 0:
            if num == i:
                return 1
            elif num != i:
                return 0

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                some_list.append(nums[i]+nums[j]+nums[k])

    for i in range(len(some_list)):
        temp = primeCheck(some_list[i])
        if temp == None:
            answer+=1
    return answer