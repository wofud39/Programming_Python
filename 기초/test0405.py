# #구구단 7단 출력하기
#
# print(f'7 x 1 = {7*1}')
# print(f'7 x 2 = {7*2}')
# print(f'7 x 3 = {7*3}')
#
# print("=====  7단 구구단  =====")
# for x in range(1,9+1): #9+1대신 10도 가능
#     print(f'7 x {x} = {7*x}')

#구구단 2~9단 출력하기
#dan = 2~9단
#i= 1~9



# print(f'\n<2415이재령_구구단출력>')
# for x in range (2,9+1):
#     print(f'\n=====  {x}단  ======')
#     for i in range(1,9+1):
#         print(f'{x} x {i} = {x*i}')
#     #print()    가 와도 됨 위에 print구구단 뺴고

#
print("2~7단까지")
for x in range (2,9+1):

    if(x>=7+1):
        break
    else:
        print(f'\n=====  {x}단  ======')
        for i in range(1,9+1):
            print(f'{x} x {i} = {x*i}')



#break다른버전
# #for dan
# if dan==7:
#     break



for x in range(1, 9 + 1 , 2):
    #if i==2 or i==4 or i==6 or i==8:
    #    continue
    if (x >= 9 + 1):
        break
    else:
        print(f'\n=====  {x}단  ======')
        for i in range(1, 9 + 1):
            print(f'{x} x {i} = {x * i}')