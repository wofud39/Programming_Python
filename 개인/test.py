def add_o(n):
    return n+1
def solution(answer):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3,3,1,1,2,2,4,4,5,5]

    while True:
        for k in range(len(a)):
            a.append(a[k])
            if len(a) == len(answer):
                break
        if len(a) >= len(answer):
            break


    count1 = 0
    count2 = 0
    count3 = 0
    for x in range(len(answer)):
        if a[x] == answer[x]:
            count1 += 1
        if b[x] == answer[x]:
            count2 += 1
        if c[x] == answer[x]:
            count3 += 1

    count = [count1, count2, count3]
    large = 0
    if count[0] == count[1] and count[0] == count[2]:
        return ([1, 2, 3])

    else:

        large: int = max(count)
        jk = [i for i, value in enumerate(count) if value == large]
        jk = list(map(add_o,jk))

        return jk
print(solution([2, 1, 2, 3, 2, 4, 2, 5,1,2,3,4,2,2])) #해설지
    #모의고사
    # https://programmers.co.kr/learn/courses/30/lessons/42840