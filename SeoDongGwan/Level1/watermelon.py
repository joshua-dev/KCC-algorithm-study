
#수박수박수박수박수...


#문제

#길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
#예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

#제한 조건
#n은 길이 10,000이하인 자연수입니다






def solution(n):

    if (n%2)==0:  # n이 짝수일 때
    
        watermelon_string = "수박" #n이 짝수라면 무조건 수박이라는 단어가 출력된다. 

        answer = watermelon_string *(n//2) #2보다 큰 2의 배수의 값에 대한 답을 도출하기 위해 n/2의 몫의 값만큼의 스트링을 늘려준다. 
        
    elif n ==1: #n=1일 경우는 따로 분리
        
        watermelon_string = "수"

    elif n%2 == 1: #n이 홀수일 때

        watermelon_string = "수박수" #1보다 큰 홀수라면 수박수가 나온다.

        if n>4: #만약 n이 3보다 큰 값인 홀수라면(5와 7 등) 수박수에 박수라는 스트링을 붙여준다.

            answer = watermelon_string + "박수"*((n//2)-1)

        else: #n=3이면 수박수 출력

            answer = watermelon_string
        
    return answer
