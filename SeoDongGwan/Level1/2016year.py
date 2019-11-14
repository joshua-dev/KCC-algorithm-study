#2016년


#문제 설명

#2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.

#요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다.

#예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.

#제한 조건
#2016년은 윤년입니다.
#2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

def solution(a,b):

    final_day_of_each_month = [31,29,31,30,31,30,31,31,30,31,30.31] #2016년 각 달의 일수를 리스트로 받는다.

    total_day = 0 # 총 일수를 세기위해서 변수를 지정해준다.

    for i in range(a-1): #1월부터 a월까지 일수를 모두 더한다.
        total_day += final_day_of_each_month[i]


    answer_of_day = total_day + (b-1) # a달의 1일이 되는 총 일수 + a달의 일수-1 -> 초기일수가 1이기때문에 -1 해준다.


    if answer_of_day%7 == 0: #2016년 1월 1일이 화요일이기 때문에 총 일수를 7로 나눈 것이 0이면 화요일
        answer = "THU"

    if answer_of_day%7 == 1: #위와 같이 실행
        answer = "WEN"

    if answer_of_day%7 == 2:
        answer = "THR"

    if answer_of_day%7 == 3:
        answer = "FRI"
        
    if answer_of_day%7 == 4:
        answer = "SAT"

    if answer_of_day%7 == 5:
        answer = "SUN"

    if answer_of_day%7 == 6:
        answer = "MON"

    return answer

        
