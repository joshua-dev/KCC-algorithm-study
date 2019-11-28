from collections import defaultdict
from functools import reduce
from operator import mul

def solution(clothes):

    num_clothes_kind = defaultdict(int)

    for name, kind in clothes:
        num_clothes_kind[kind] += 1
        
    tmp = [ num + 1 for num in num_clothes_kind.values() ]
    answer = reduce(mul, tmp)
    answer = answer -1
    return answer
