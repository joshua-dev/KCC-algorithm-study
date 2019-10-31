'''
N개의 최소공배수
문제 설명
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

제한 사항
arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.
'''


def GCD(number): # 한 숫자에 대한 최대공약수의 리스트를 구하는 함수

    GCD = []
    
    for i in range(1,101,1):
        if number%i == 0:
            GCD.append(i)

    return GCD

    

def solution(arr):

    if len(arr) == 1: #만약 리스트의 원소가 1개라면 바로 리턴
        return arr[0]

    answer = arr[0]
    LCM_list =[]
    final_GCD = 1
    LCM = 1
    
    for j in range(1,len(arr)): # 첫번째 리스트와 나머지 리스트의 최대공약수의 공통 수를 추출한다.
          
        GCD_list = list(set(GCD(answer)) & set(GCD(arr[j])))

    for k in range(0,len(GCD_list)): #최대공약수의 곱을 구한다.(최종 최대공약수)
        final_GCD = final_GCD * GCD_list[k]


    
    for l in range(0,len(arr)): # 모든 수를 최대공약수로 나눈 나머지 값에 대한 리스트
        LCM_list.append(arr[l]//final_GCD)
        
    LCM_list.append(final_GCD) # 최대공약수로 나눈 나머지 리스트에 최대공약수도 추가
    
    
    for m in range(0,len(LCM_list)): #최대공약수와 최대공약수로 나눈 나머지 값을 모두 곱한다.
        LCM = LCM * LCM_list[m]
        
    return LCM

    
    
        
