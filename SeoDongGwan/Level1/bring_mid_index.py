'''
가운데 글자 가져오기
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
'''

def solution(s):
    list = []
    for i in s:
        list.append(i)
        
    length = len(list)
    
    if length %2 == 0:
        index = 2
    else:
        index = 1
    middle = length//2
    
    if index == 1:
        return list[middle]
    else:
        return list[middle-1]+list[middle]
