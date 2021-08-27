# print("---------------문제3---------------")
# # 3. Quiz
# # 3-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
# # 출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
# # 예시
# # id_number = 020316 일 때
#
# id_number= "020316"
# year=int(id_number[0:2])
# month=int(id_number[2:6])
#
#
# print("생년: "+str(year))
# print("월 : "+str(month))
# print("곱한값: "+str(year*month))
#
#
# print("---------------문제3-2---------------")
# # 3-2. 집 전화번호를 phone_number에 넣고,
# # 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# # 예시
# # phone_number = 02-1234-5678 또는 032-9876-4321
#
#
# phone_number= "031-1234-5678"  #<<< 지역번호를 031/ 02로 수정해본결과 둘다 됨 ㅇㅇ
#
#
# if(len(phone_number)==13):
#     print("지역번호: "+str(phone_number[0:3]))
# else:
#     print("지역번호: "+str(phone_number[0:2]))
# print("뒷자리번호: "+str(phone_number[-4:]))


# Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.


#---------------------------------------------------------------------
# Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
#
#
# # student_number= '2100'
# soft="뉴미디어소프트웨어과"
# media="뉴미디어웹솔루션과"
# design="뉴미디어디자인과"
# cls=str(student_number[1:2])
#
# if cls=='1' or cls=='2':
#     print("{0}반 {1}입니다.".format(cls,soft))
# elif cls=='3'or cls=='4':
#     print("{0}반 {1}입니다.".format(cls, media))
# elif cls=='5'or cls=='6':
#     print("{0}반 {1}입니다.".format(cls, design))
# else:
#     print("잘못입력했습니다.")




#---------------------------------------------------------------------
# Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2



# snum='2100'
# def argument(snum):
#     grade = str(snum[0:1])
#     clas = str(snum[1:2])
#
#     if clas == '1' or clas == '2':
#         print("{0}학년 {1}반 {2}입니다.".format(grade, clas, soft))
#     elif clas == '3' or clas == '4':
#         print("{0}학년 {1}반 {2}입니다.".format(grade, clas, media))
#     elif clas == '5' or clas == '6':
#         print("{0}학년 {1}반 {2}입니다.".format(grade, clas, design))
#     else:
#         print("잘못입력했습니다.")
#
# argument(snum)
#
#
#
# #---------------------------------------------------------------------
# # Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# # <함수 호출>
# # print(average(10, 20, 30)) #20.0
# # print(average(4, 23)) #13.5
#
#
# def average(*numbers):
#     return sum(numbers)/len(numbers)
#
# print(average(10, 20, 30))
# print(average(4, 23))
#
#
# #---------------------------------------------------------------------
# # Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# # (소수 첫째자리까지 반올림)
# # * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# # 18.5 미만: 저체중
# # 18.5 이상 23 미만: 보통
# # 23 이상 25 미만: 과체중
# # 25 이상: 비만
# #
# # <함수 호출>
# # bmi = get_bmi(176, 69)[
# # print(bmi) #22.3
#
#
# def bmi(cm,kg):
#     m_m=cm*0.01
#     return round(kg/(m_m*m_m),1)
#
# print(bmi(180,60))
#

#---------------------------------------------------------------------
# Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리
# 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
#
#
# def n_sum(num):
#     f=str(num)
#     k=0
#     if len(f)<10:
#         for a in f:
#             k+=int(a)
#
#
#         return(k)
#     else:
#         return -1
# # print(n_sum(123))
#
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1
#



#---------------------------------------------------------------------
# Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
# '''

# import math
#
# def get_subway_fare(km):
#     c_fare=720
#     if km <10:
#         return 720
#     elif 10<= km <50:
#         num = km-10
#         c_fare = (math.ceil(num/5)*100) + 720
#         return c_fare
#     elif km>50:
#         num = km - 50
#         c_fare = (math.ceil(num/8) * 100) + 720 + (math.ceil((50-10)/5)*100)
#         return c_fare
#
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720
#

#---------------------------------------------------------------------
# Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# 힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
# '''
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝


#num.count(str('3'))




#
# def get_three_six_nine(num):
#     cc=str(num)
#     count=0
#
#     for i in cc:    #cc: '16' i: '1' '6'
#         if i == '3' or i == '6' or i == '9':
#             count += 1
#
#     if count >= 1:
#         result = "짝"*count
#     else:
#         result = num
#
#     return result
#
#
#
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝



#---------------------------------------------------------------------
# Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime() 함수를 만든다.
# 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
# '''
# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님



# num=11
# for i in range(1,11+1):
#     if num / i == 0:
#         print( "소수")
#     else:
#         print( "소수아님")

# def is_prime(num):
#     lnum = str(num)
#     k = len(lnum)
#     cnt = 0
#     for i in range(1,k+1):
#         num /i
#
#         if num/i==1 or num/i==lnum:
#             cnt+=1
#         else:
#             cnt+=1
#         if cnt==2:
#             return "소수"
#         else:
#             return "소수아님"
#
# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님
#
# print(36/1)



