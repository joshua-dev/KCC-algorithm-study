def solution(n):
 
    one_count = bin(n).count('1') # bin을 통해 10진수를 2진수로 바꿔줄 수 있고 
                          # count를 통해 1을 바로 세줄 수 있다.
    for i in range(n+1,1000001): # n보다 큰 수부터 제한사항에 만족하는 수까지 반복해준다.
 
        if bin(i).count('1') == one_count: # 1의 개수가 n가 같은 수가 나오면 그 수를 출력한다.
 
            return i
