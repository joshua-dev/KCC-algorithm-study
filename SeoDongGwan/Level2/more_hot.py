'''
더 맵게
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 1 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
'''

import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville) #힙 생성

    while len(scoville) > 1: # scoville의 변수가 1개 남을때까지 루프
        n1 = heapq.heappop(scoville) #첫번째 힙 변수
        n2 = heapq.heappop(scoville) #두번째 힙 변수
        if n1 < K or n2 < K: # n1과 n2가 K보다 작다면
            heapq.heappush(scoville, n1+(n2*2)) #n1,n2를 공식대로 계산 후 삽입
            count+=1 #카운트 증가
        else:
            return count
        
    if scoville[0] > K: #scoville이 1개의 변수를 가지고 있고 그 변수가 K보다 크다면 count 리턴
        return count
    else: #K를 못 넘었다면 리턴 -1
        return -1
