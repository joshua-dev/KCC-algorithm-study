def solution(n, words):
    answer = [0,0]
    past=[]
    past.append(words[0])
    words.remove(words[0])
    count=0
    problem=False
    for word in words:
        count+=1
        if word in past:
            problem=True
            break
        else:
            past.append(word)
            if past[-2][-1]==past[-1][0]:
                pass
            else:
                problem=True
                break
 
    if not problem:
        return answer
    else:
        answer[1],answer[0]=divmod(count,n)
        answer[0]+=1
        answer[1]+=1
        return answer
