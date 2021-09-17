answer = [1,3,5,2,4,3,3,1]  #8개
def char1(): # 1번수포자
    a = list()
    count=0
    anscrt = 0
    while True:
        for i in range(1,5+1):
            a.append(i)
            count+=1
            if count ==len(answer):
                break
        if count ==len(answer):
            break
    for x in range(len(answer)):
        if answer[x] == a[x]:
            anscrt+=1

    return('수포자 1은 {0}문제를 맞췄습니다.'.format(anscrt))  #여기서 format은   f''(f스트링)이면 안된다.

print(char1())
