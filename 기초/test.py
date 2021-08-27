# 구구단 7단 출력하기
# i : 1~9: 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(1, 9 + 1):
    print(f'7 x {i} = {7 * i}')

# 구구단 2~9단 출력하기
#dan: 2~9단
#i: x1~9
for dan in range(2, 9 + 1):     #2~9
    for i in range(1, 9 + 1):   #x1~x9
        print(f'{dan} x {i} = {dan * i}')
        #print() #1번
    print()     #2번
#print()         #3번

#구구단 2~7단까지 출력하기    break
for dan in range(2, 9 + 1):     #2~9
    for i in range(1, 9 + 1):   #x1~x9
        print(f'{dan} x {i} = {dan * i}')
    print()     #2번
    if dan == 7:        #7단 위에서 출력하고, 끝내라
        break

#구구단 2~7단 출력하되, x1, x3, x5, x7, x9 인 것만 출력하기    break, continue
for dan in range(2, 9 + 1):     #2~9
    for i in range(1, 9 + 1):   #x1~x9
        if i % 2 == 0:  #if i == 2 or i == 4 or i == 6 or i == 8:
            continue
        print(f'{dan} x {i} = {dan * i}')
    print()     #2번
    if dan == 7:        #7단 위에서 출력하고, 끝내라
        break
