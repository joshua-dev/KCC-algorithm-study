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
    not_a_position = []  # A가 아닌 알파벳의 어레이 위치
    gps = 0  # 현재 위치

    for i in range(len(name)):  # 알파벳 상하 조절에 필요한 조작 횟수를 찾아 answer에 추가
        if ord(name[i]) == 65:
            pass
        else:
            tmp = ord(name[i]) - 65
            not_a_position.append(i)
            if tmp > 13:
                answer += 26-tmp
            else:
                answer += tmp

    while not_a_position:
        # 순차적으로 조작했을 때 A가 아닌 알파벳으로 가는 최솟값
        tmp1 = min(abs(not_a_position[0]-gps),
                   len(name)-abs(not_a_position[0]-gps))
        # 역순으로 조작했을 때 A가 아닌 알파벳으로 가는 최솟값
        tmp2 = min(abs(not_a_position[-1]-gps),
                   len(name)-abs(not_a_position[-1]-gps))
        # 어레이 1개 남은 상황에서 tmp1과 tmp2가 같아진다.

        if tmp1 > tmp2:  # 순차적으로 가는 방법이 더 느릴때 최솟값인 역순으로 가는 횟수를 answer에 추가
            gps = not_a_position.pop()  # 역순으로 갔을 때 조이스틱 값의 위치
            answer += tmp2
        else:  # 순차가 빠르다면 순차적으로 가는 횟수를 answer에 추가
            gps = not_a_position.pop(0)  # 순차적으로 갔을 때 조이스틱 값의 위치
            answer += tmp1

    return answer


'''
def solution(name):
    answer = 0
    name_list = []
    for i in name: 
        if ord(i)-65 > 13: #N을 위방향으로 올리면 14번이지만 아래방향으로 내리면 12번이다. 때문에 13을 기준으로 위아래를 구분한다.
            name_list.append(-(ord(i)-91)) #N~Z
        else:
            name_list.append(ord(i)-65)#A~M

    print(name_list)

 
    for j in name_list: #한 개의 알파벳당 +1만큼 좌우 조절
         
        answer=answer+j+1
        
    
    if name_list[1] == 0: #만약 2번째 영어가 A이면 마지막 칸으로 가면되니 A에 대한 스틱조절 -1을 해준다
        answer = answer - 1

    return answer-1 #알파벳당 좌우조절 +1을 해줬지만 마지막 알파벳은 조절이 필요없으므로 -1

'''
