from collections import Counter


def freqQuery(queries):
    # Dict = Counter([])
    # arr = []
    # for element in queries:
    #     if element[0] == 1:
    #         # arr.append(element[1])
    #         arr.append(element[1])
    #         Dict.update(arr)
    #         arr.clear()
    #     elif element[0] == 2:
    #         # try:
    #         # arr.remove(element[1])
    #         # except:
    #         #     pass
    #         # Dict.pop(element[1])
    #         if element[1] in Dict:
    #             del Dict[element[1]]
    #     else:
    #         if element[1] in Dict.values():
    #             print(1)
    #         else:
    #             print(0)

    freq = Counter()

    cnt = Counter()

    arr = []

    for q in queries:
        if q[0] == 1:
            cnt[freq[q[1]]] -= 1
            freq[q[1]] += 1
            cnt[freq[q[1]]] += 1

        elif q[0] == 2:
            if freq[q[1]] > 0:
                cnt[freq[q[1]]] -= 1
                freq[q[1]] -= 1
                cnt[freq[q[1]]] += 1

        else:
            if cnt[q[1]] > 0:
                arr.append(1)
            else:
                arr.append(0)

    print(arr)
    return arr




freqQuery([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]])
