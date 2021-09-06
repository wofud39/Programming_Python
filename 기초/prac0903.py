print("\n====== 1번 ======")
import math
phone = 59827
print(f'{round(phone,-2)}원\n')

bill = 62421
bill = 59827
print(bill//100*100)
print(bill - bill%100)
print(math.floor(bill/100)*100)
print(int(bill/100)*100)




print("\n====== 2번 ======")
score = 56
print(f'{round(score, -1)}점')

print(round(score/10)*10)
print(round(score,-1))






print("\n====== 3번 ======")
import random
a = random.sample(range(1,45+1), 6)
print(a)


print("\n====== 4번 ======")
b = random.sample(range(1,9+1),3)
print(b[0],b[1],b[2])


list_r = random.sample(range(1,9+1),3) #숫자리스트
# join은 문자리스트만 해줌
print("".join(str(list_r)))  #중간에 삽입될 문자"".join
print("".join(str(n) for n in list_r))   # 정답
print("".join(map(str, list_r))) #맵핑..?


print("\n====== 5번 ======")
import datetime
now = datetime.datetime.now()
birth = datetime.datetime(2004,11,29)
print(now-birth)


print("\n====== 6번 ======")
xmas = datetime.datetime(2021,12,31)
print(xmas-now)

print("\n====== 7번 ======")
yearB = datetime.datetime(2021,11,29)
print(yearB-now)

if yearB<now:
    yearB = yearB.replace(year = 2022)
    #yearB.year = yearB.year+1   이건 안됨 date와 관련된건


print("\n====== 8번 ======")
# def check():
#     random.shuffle(list)
#     for i in range(1,c+1):
#         print(f'{i}번 학생| {list[i-1]}자리')
# #랜덤자리배치
# list = list()

# ask3 = input('반 총원이 몇명입니까? (숫자)')
# for k in range(1,int(ask3)+1):
#     list.append(k)
# ask = input('전출/자퇴 한 사람이 있습니까? (y/n) ')
# if ask=='y':
#     ask2 = input('몇명이 전출/자퇴 했습니까? (현원{0})'.format(len(list)))
#     c = len(list)-int(ask2)
#     del list[c:]
#     print('-'*30)
#     check()
# elif ask=='n':
#     c = len(list)
#     print('-' * 30)
#     check()

#print(list)


#랜덤자리배치2

#마지막 번호는 몇번인가요?
last_number = input('마지막번호? ')
# 1~마지막번호까지 숫자 리스트 만들기
list_class = list(range(1,int(last_number)+1))

while True:
# 뺄 번호는?
    exclude_number = input('뺄 번호는? ')
# 다 빼면 반복 끝내기
    if exclude_number=='':
        break
# 뺌
    list_class.remove(int(exclude_number))
    print(list_class)


# 섞기
random.shuffle(list_class)

#출력
print('자리\t학생번호')
for i, number in enumerate(list_class):
    print(f'{i+1}\t{number}')


