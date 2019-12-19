def solution(begin, target, words):
    if target not in set(words):
        return 0
    queue = [begin]
    total_count = 0
    while len(words) != 0:
        for value in queue:
            # 바꾸게 될 단어를 저장하는 변수
            temp = []
            for word in words:
                count = 0
                for idx in range(len(word)):
                    # 원래 단어와 words의 각 단어를 비교해서
                    # 단어가 다르면 count 증가.
                    if value[idx] != word[idx]:
                        count += 1
                    if count == 2:
                        # 한 번에 하나만 바꿀 수 있다고 했으니
                        # 값이 다른 게 두 개 이상이면 더 볼 필요 없다
                        break
                # 각 word 단어를 비교한 다음
                # 바꿀 수 있는 단어면 temp에 저장하고
                # words에서 단어를 삭제한다.
                if count == 1:
                    temp.append(word)
                    words.remove(word)
        total_count += 1
        if target == "".join(temp):
            return total_count
        else:
            queue = temp
    return 0
