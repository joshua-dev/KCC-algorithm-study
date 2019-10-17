"""
1|2|3|4
5|6|7|9
4|1|2|3
위에 나온 것 처럼 크기가 n,4인 행렬에서
열을 따라 밑으로 내려가면서 점수를 더한다.
단 전에 밟았던 열의 점수는 더 할 수 없다.
예시의 답은
3+9+4 = > 16이 답이 된다.
"""
def solution(land):
    answer = 0
    N = len(land)
    for i in range(0,N-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
    answer = max(land[N-1])

    return answer