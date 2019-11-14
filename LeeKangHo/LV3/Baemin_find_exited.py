"""
중복된 닉네임이 있으면 찾아내서 이메일을 리턴하는
"""

forms = [["jm@email.com", "제이엠"], ["jason@email.com", "제이슨"], ["woonin@email.com", "워니"],
         ["mj@email.com", "엠제이"], ["nonwn@email.com", "이제엠"]]


def solution(forms):
    answer = []
    flag = {}
    for i in forms:
        flag[i[0]] = False

    for i in forms:
        for j in range(len(i[1]) - 1):
            for k in range(len(forms)):
                temp_string = i[1][j] + i[1][j + 1]
                if i[0] == forms[k][0]:
                    continue
                if temp_string in forms[k][1]:
                    if flag[forms[k][0]]:
                        flag[forms[k][0]] = True
                        answer.append(forms[k][0])
    answer.sort()
    return answer


print(solution(forms))