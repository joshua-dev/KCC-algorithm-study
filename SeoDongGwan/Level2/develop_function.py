import math

def solution(progresses, speeds):
    answer = []
    
    remain_day_list = []
    
    for i in range(len(progresses)):
        remain_progress = 100 - progresses[i]
        remain_day = remain_progress / speeds[i]
        remain_day_list.append(math.ceil(remain_day))
        
    for i in range(1,len(remain_day_list)):
        if remain_day_list[i-1] > remain_day_list[i]:
            remain_day_list[i] = remain_day_list[i-1]
    
    count = 1
    for i in range(1,len(remain_day_list)):
        if remain_day_list[i-1] >= remain_day_list[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
    
    answer.append(count)
        
    return answer

