"""
우아한 테크코스 4번
자세한 설명은 따로 드릴게요.
"""

infos = ["kim password", "lee abc"]
actions = [
    "ADD 30",
    "LOGIN kim abc",
    "LOGIN lee password",
    "LOGIN kim password",
    "LOGIN kim password",
    "ADD 30",
    "ORDER",
    "ORDER",
    "ADD 40",
    "ADD 50"
]


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.list_num = 0

    def LOGIN(self, name, password):
        return True

    def ADD(self, id):
        self.list_num += 1
        return True

    def ORDER(self):
        if (self.list_num != 0):
            self.list_num = 0
            return True
        else:
            return False


def solution(infos, actions):
    info = {}
    action = []
    for string in infos:
        temp = []
        temp = string.split(" ")
        info[temp[0]] = temp[1]
    for string in actions:
        temp = []
        temp = string.split(" ")
        action.append(temp)
    answer = []
    user = None
    status_flag = False
    answer = []
    for i in range(len(action)):
        if action[i][0] == "ADD":
            if status_flag == False:
                answer.append(False)
            else:
                if (user):
                    answer.append(user.ADD(action[i][1]))
                else:
                    answer.append(False)
        elif action[i][0] == "LOGIN":
            if status_flag == False:
                if not action[i][1] in info.keys():
                    answer.append(False)
                elif info[action[i][1]] == action[i][2]:
                    status_flag = True
                    user = User(action[i][1], action[i][2])
                    answer.append(user.LOGIN(action[i][1], action[i][2]))
                else:
                    answer.append(False)
            else:
                answer.append(False)
        elif action[i][0] == "ORDER":
            if status_flag == False:
                answer.append(False)
            else:
                answer.append(user.ORDER())
    return answer

answer = solution(infos, actions)
for i in answer:
    print(i)