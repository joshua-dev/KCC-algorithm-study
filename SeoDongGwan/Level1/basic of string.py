'''
문자열 다루기 기본
문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
'''


def solution(s):

    string_list = [] #s로 받은 문자를 리스트에 받기 위한 공간을 만든다

    for i in s: #각각의 문자열을 구분하여 리스트에 추가한다.
        string_list.append(i)


    try:
        for i in range (0,len(string_list)): #리스트는 10을 1,0으로 구분한다 따라서 숫자인지 판단하기 위해 리스트의 요소들이 10보다 작다면 숫자임을 알 수 있다.
            if int(string_list[i]) <10: #숫자라면 pass
                pass

    except ValueError: #만약 리스트에 문자가 있다면 ValueError로 False가 된다.
      answer = False

    else: #문자가 없다면 다음 문장을 실행
   
        if int(len(string_list))==4: #s의 길이가 4이면 True
            answer = True

        elif int(len(string_list))==6: #s의 길이가 6이면 True
            answer = True

        else: #4나 6이 아니라면 False
            answer = False
        

    
    return answer

