'''
문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
JEROEN	56
JAN	23
'''


def solution(name):
    answer = 0
    name_list = []
    for i in name: 
        if ord(i)-65 > 13: #N을 위방향으로 올리면 14번이지만 아래방향으로 내리면 12번이다. 때문에 13을 기준으로 위아래를 구분한다.
            name_list.append(-(ord(i)-91)) #N~Z
        else:
            name_list.append(ord(i)-65)#A~M

    for j in name_list: #한 개의 알파벳당 +1만큼 좌우 조절
         
        answer=answer+j+1
        
    print(answer)    
    if name_list[1] == 0: #만약 2번째 영어가 A이면 마지막 칸으로 가면되니 A에 대한 스틱조절 -1을 해준다
        answer = answer - 1

    print(name_list)
    return answer-1 #알파벳당 좌우조절 +1을 해줬지만 마지막 알파벳은 조절이 필요없으므로 -1

