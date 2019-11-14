'''
전화번호 목록
문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
'''

 

def solution(phone_book):
    phone_book.sort() #정렬
    for p1, p2 in zip(phone_book, phone_book[1:]): #동일한 개수로 이루어진 자료형을 묶어준다
        if str(p2).startswith(str(p1)): #n번째와 n+1번째 변수를 비교해 n번째 변수가 n+1변수앞에 포함이 되있다면 False
            return False
    return True # 접두어가 없다면 True
