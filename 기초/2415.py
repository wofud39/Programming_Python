#휴대폰 번호를 입력할때 -있던 , 없든 , 없이 출력하기

phone_number1='010-2540-5357'
phone_number2='010 7584 1367'
phone_number3='01073201685'
# phone_number = phone_number1

# # - /' ' 둘다 바꾸는법 ㄱㄱㄱ
# result = phone_number1.replace('-','').replace(' ','')



'''
print("원번호: " + str(phone_number1))
result = phone_number1.replace('-','')
print("수정된 번호: " +str(result))

print("-------------------------------------")
print("원번호: " + str(phone_number2))
result = phone_number2.replace(' ','')
print("수정된 번호: " +str(result))

print("-------------------------------------")
print("원번호: " + str(phone_number3))
result = phone_number3.replace(' ','')
print("수정된 번호: " +str(result))
'''


'''
Quiz2-1. 학번을 student_number변수에 넣고, 학급을 출력하고, 학과를 출력하기
반이0 미만이거나 7이상이면 "잘못입력했습니다" 추렭하기
student_number='2100' 또는 student_number='2000'
<출력예시>
1반 뉴미디어 소프트 웨어과 또는잘못입력했스비다.
'''
# if number==1: 로 쓰고 싶다면 number=int(number)
# student_number='2100'  #student_number[1:2]
# number=student_number[1]
# if student_number[1]=='1':
#     print("1반 뉴미디어소프트웨어과")
# elif student_number[1]=='2'


#mayjors=['뉴솦','뉴솦','뉴웹','뉴웹','뉴디','뉴디]
#print(f"{number}반 {mayjors[number-1]}")


# if 1<=number and number<=6:
#     print(f"{number}반 {mayjors[number-1]}")
# else:
#     print('잘못입력했습니다.')


#나도코딩...

def average(*numbers):
    return sum(numbers)/len(numbers)
print(average(10,20,30))
print(average(4,23))

#
# def get_mayjor(student_number):
#     mayjor=['소','소','솔','솔','디','디']
#     grade=student_number[0]
#     classroom=int(student_number[1])
#     return ㅏ하시발...
#
# round(bmi,1)
# 반올림해서 1까지..하여간 정수로 나온다는 말 어쩌고
# #bmi..
# sival..


a=range(1,11,2) #1부터 11까지(11제외) 2씩증가
#
# 10이하 짝수 큰수부터 10,8,6,4,2: range(10,1,-2)



'''
Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.

result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1
'''

def n_sum(n):
    #하나씩 쪼개자
    n=123
        #1,2,3
        #123 // 100:1
        #123 //10: 2
        #123 %10 : 3
    #123--> "123"
    n=str(n)

    #쪼갠거 하나씩 더하자=> 리턴