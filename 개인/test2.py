answer = [1,3,5,2,4,4,3,1]  #8개
# 1번수포자
a = list()
count1=0
anscrt1 = 0
while True:
    for i in range(1,5+1):
        a.append(i)
        count1+=1
        if count1 ==len(answer):
            break
    if count1 ==len(answer):
        break
for x in range(len(answer)):
    if answer[x] == a[x]:
        anscrt1+=1

# 2번 수포자
b = list()
anscrt2 = 0
count2 = 0
while True:
    for i in range(1, 5 + 1):

        if 5 > i >= 2:  # 2가 들어올경우
            b.append(2)
            b.append(i + 1)
            count2 += 2
        elif i < 2:
            b.append(2)
            b.append(i)
            count2 += 2
        else:  # i가 5인경우
            continue
        if count2 == len(answer):
            break
    if count2 == len(answer):
        break
for x in range(len(answer)):
    if answer[x] == b[x]:
        anscrt2 += 1

# 3번 수포자
c = list()
cpz = [3,1,2,4,5]
anscrt3 = 0
count3 = 0
while True:
    for i in range(0, 5): #5번잘라서 반복
        c.append(cpz[i])
        c.append(cpz[i])
        count3+=2

        if count3 == len(answer):
            break
    if count3==len(answer):
        break

for x in range(len(answer)):
    if answer[x] == c[x]:
        anscrt3+=1

anscrt = [anscrt1, anscrt2, anscrt3]
for x in range(1,3+1):
    print('수포자 {0}은 {1}문제를 맞췄습니다.'.format(x, anscrt[x-1]))  #여기서 format은   f''(f스트링)이면 안된다.


result = 0
if anscrt1 == anscrt2 ==anscrt3:
    print('모든 사람이 {}문제씩 맞췄습니다.'.format(anscrt1))

else:
    if anscrt1 <anscrt2:
        result = '2번'
        if anscrt2<anscrt3:
            result = '수포자 3'
        else:
            #anscrt2>anscrt3
            result = '수포자 2'

    else:
        #anscrt1 > anscrt2
        result = '수포자 1'
        if anscrt1 <anscrt3:
            result = '수포자 3'
        else:
            #anscrt1>anscrt3:
            result = '수포자 1'

    print('따라서 가장 문제를 많이 맞힌 사람은 {0}입니다'.format(result))




