"""
문제 설명
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

제한 조건
스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
스킬 순서와 스킬트리는 문자열로 표기합니다.
예를 들어, C → B → D 라면 CBD로 표기합니다
선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
skill_trees는 길이 1 이상 20 이하인 배열입니다.
skill_trees의 원소는 스킬을 나타내는 문자열입니다.
skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.
입출력 예
skill	skill_trees	return
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
"""


def solution(skill, skill_trees):
    answer = 0
    skill_list = []
    hmt = [0 for i in range(len(skill_trees))]
    cmt = [0 for i in range(len(skill_trees))]
    for i in range(len(skill)):
        skill_list.append(skill[i])

    for i in range(len(skill_trees)):
        for j in range(len(skill_trees[i])):
            for z in range(len(skill)):
                if skill_trees[i][j] == skill_list[z]:
                    hmt[i] += 1

    for i in range(len(skill_trees)):
        count = 0
        idx = -1
        for j in range(len(skill_trees[i])):
            for z in range(len(skill)):
                if skill_trees[i][j] == skill_list[z]:
                    if z > idx and z - idx == 1:
                        idx = z
                        cmt[i] += 1
                    else:
                        break
    for i in range(len(hmt)):
        if hmt[i] == cmt[i]:
            answer += 1

    return answer