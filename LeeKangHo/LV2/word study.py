"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
입력 1
Mississipi
출력 1
?
예제 입력 2
zZa
예제 출력 2
Z

"""
str = input()
str = str.upper()
kangho = list(set(list(str)))
pivot = 0
answer = ''
for i in kangho:
    if pivot < str.count(i):
        pivot = str.count(i)
        answer = i
    elif pivot == str.count(i) and answer != i:
        answer = '?'
print(answer)
