'''
가장 큰 수
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
'''


def solution(numbers):
    answer_list = []  # 10이하의 수 배열
    answer_list_of_over_10 = []  # 10이상의 수 배열
    for i in numbers:
        if i < 10:  # 10보다 작다면 10이하 배열에 추가
            answer_list.append(i)

    answer_list.sort()
    answer_list.reverse()  # 10이하의 수 배열을 역정렬

    for j in numbers:  # 10보다 크다면 10이상 배열에 추가
        if j >= 10:
            answer_list_of_over_10.append(j)
    answer_list_of_over_10.sort()

    for i in range(0, len(answer_list_of_over_10)):
<<<<<<< HEAD
            for j in range(0,len(answer_list)):
                if answer_list_of_over_10[i]>answer_list[j]*11: #만약 30과 3이 있다면 303보다는 330이 크다 그래서 10이하의 수*11을  
                    answer_list.insert(j, answer_list_of_over_10[i])#한 값보다 10이상의 수가 크다면 해당 수의 앞에 10이상의 수를 배열에 추가
                    del answer_list_of_over_10[i] #10이하의 수에 추가된 10이상의 수는 10이상의 수배열에서 삭제

    answer_list_of_over_10.reverse() #만약 10이상의 수가 남아있다면 역정렬한다
    final_answer = answer_list + answer_list_of_over_10 # 정렬이 된 두개의 배열을 더한다

    for n in final_answer: 
=======
        for j in range(0, len(answer_list)):
            # 만약 30과 3이 있다면 303보다는 330이 크다 그래서 10이하의 수*11을
            if answer_list_of_over_10[i] > answer_list[j]*11:
                # 한 값보다 10이상의 수가 크다면 해당 수의 앞에 10이상의 수를 배열에 추가
                answer_list.insert(j, answer_list_of_over_10[i])
                # 10이하의 수에 추가된 10이상의 수는 10이상의 수배열에서 삭제
                del answer_list_of_over_10[i]

    answer_list_of_over_10.reverse()  # 만약 10이상의 수가 남아있다면 역정렬한다
    final_answer = answer_list + answer_list_of_over_10  # 정렬이 된 두개의 배열을 더한다

    for n in final_answer:
>>>>>>> 823ea370111be7284c2e1b04d0976c39577e9536
        print(n, end='')

    # return answer로 배열을 스트링으로 뽑아내는 법은 잘 모르겠습니다..


'''
def solution(numbers):

    for i in range(0,len(numbers)-1):
        if numbers[i] >=10:
            remember_number = numbers[i]
            print(remember_number)
            number_of_over_10= numbers.pop(i)
            numbers.append(number_of_over_10//10)
            numbers.sort()
            numbers.reverse()
            
    print(numbers)
    '''
