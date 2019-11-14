'''
주식가격
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
'''

from collections import deque #price = [1,2,3,2,3]

def get_non_decreasing_days(price, prices_deque):
    non_decreasing_days = 0
    for i in prices_deque: #price = 1, deque = 2,3,2,3
        if price <= i:
            non_decreasing_days += 1
        else:
            non_decreasing_days += 1 
            break
    return non_decreasing_days


def solution(prices):
    prices_deque = deque(prices) #데크 생성
    answer = []
    while prices_deque:
        price = prices_deque.popleft() #pop으로 price 변수를 만들어 비교하기 위함
        non_decreasing_days = get_non_decreasing_days(price, prices_deque)
        answer.append(non_decreasing_days)

    
    return answer
