# #시작
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
#
# #두번째
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)
#
#
# #참 / 거짓
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not(5>10))
#
#
# #애완동물을 소개해주세요~
# animal="강아지"
# name = "연탄이"
# age=4
# hobby="산책"
# is_adult= age>=3
# print("우리집 "+animal+"의 이름은 "+name+"에요")
# hobby="공놀이"
#
# #print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
# print(name,"는 ",str(age),"살이며, ",hobby,"을 아주 좋아해요")
# print(name+"는 어른일까요?"+str(is_adult))
#
#
# #주석편
# '''
# 이거도 주석됨
# '''
#
#
# #Quiz) 변수를 이용하여 다음 문장을 출력하시오
# #변수=station     변수값= 사당, 신도림, 인천공항
# station="사당"
# print(station+"행 열차가 들어오고 있습니다.")
# station="신도림"
# print(station+"행 열차가 들어오고 있습니다.")
# station="인천공항"
# print(station+"행 열차가 들어오고 있습니다.")
#
#
# #연산자
# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)
#
# print(2**3)#2의 3제곱 ==8
# print(5%3) #나머지구하기 ==2
# print(10%3)#==1
# print(5//3)#몫 ==1
# print(10//3)
#
# print(10>3)#true
# print(4>=7)#false
# print(10<3)#false
# print(5<=5)#true
#
# print(3==3)#true
# print(4==2)#false
# print(3+4==7)#true
#
#
# print(1 != 3)       #같지 않다 True
# print(not(1 != 3))  #false
#
# print((3>0)and(3<5))#true
# print((3>0) & (3<5))#true  둘다 true여야 true출력
#
# print((3>0)or(3>5))#둘중 하나라도 true면 true출력
# print((3>0)|(3>5)) #위와 동일한식임 ㅇㅇ
#
# print(5>4>3)#true
# print(5>4>7)#false
#
# #간단한 수식
# print((2+3*4))
# print((2+3)*4)
# number=2+3*4
# print(number)
# number=number+2
# print(number)
# number+=2
# print(number)
# number*=2
# print(number)
# number  /=2
# print(number)
# number-=2
# print(number)
#
# number%=5
# print(number)
#
# #숫자처리 함수
# print(abs(-5)) #5(절대값)
# print(pow(4,2))#4의 2승
# print(max(5,12)) #둘 중에 큰값을 출력==12
# print(min(5,12)) #최소값 5를 출력
# print(round(3.14)) #3반올림
# print(round(4.99)) #5반올림
#
# from math import *
# print(floor(4.99))#내림 ==4
# print(ceil(3.14))#올림 ==4
# print(sqrt(16)) #제곱 4의제곱이니까 4가 출력됨
#
# #랜덤함수
# from random import *
# # print(random()) #0.0이상 1.0미만의 랜덤값을 생성한다.
# # print(random()*10)#0.0이상 10.0미만의 랜덤값을 생성한다.
# # print(int(random()*10))#0~10미만의 소수x랜덤값 생성 int로 감싸주면됨
# print(int(random()*10)+1)#1~10이하의 임의의 값 생성
# print(int(random()*10)+1)#1~10이하의 임의의 값 생성
# print(int(random()*10)+1)#1~10이하의 임의의 값 생성
# print(int(random()*10)+1)#1~10이하의 임의의 값 생성
# print(int(random()*10)+1)#1~10이하의 임의의 값 생성
# print(int(random()*10)+1)#1~10이하의 임의의 값 생성
# print(int(random()*10)+1)#1~10이하의 임의의 값 생성
#
#
# print(int(random()*45)+1)#1~45이하
#
#
# print(randrange(1,46))#1~46미만
# print(randint(1,45))#1~45이하
#
# #
# # #Quiz) 당신은 최근에 코딩 스터디 모임을 새로 마들었습니다.
# # 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로함
# # 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
#
# '''
# 조건1 : 랜덤으로 날자를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
#
# (출력예시)
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
# '''
# from  random import *
#
# date=randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월"+str(date)+"일로 선정되었습니다.")
#
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 ="파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은쉬워요
# """
# print(sentence3)
#
#
# #슬라이싱
# jumin ="990120-1234567"
# print("성별: "+jumin[7])
# print("연: "+jumin[0:2]) #0~1
# print("월: "+jumin[2:4])
# print("일: "+jumin[4:6])
#
# print("생년월일: "+jumin[:6])
# print("뒤 7자리: "+jumin[7:])
# print("뒤7자리 (뒤에서부터): "+jumin[-7:])
#
#
# #문자열 처리함수
# python="Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) #이문자가 대문자인지 확인
# print(len(python)) #길이변환
# print(python.replace("Python","Java"))
#
# index=python.index("n")
# print(index)
# index=python.index("n",index+1)
# print(index)
#
# print(python.find("Java")) #없어도 다음문장 진행 가능
# #print(python.index("Java")) 없으면 강제중지
# print("hi")
#
# print(python.count("n")) #n의 등장횟수 알려줌
#
#
# #문자열 포멧
# print("a"+"b")
# print("a","b")
#
# #방법1
# # print("나는 %d살입니다."%20)
# # print("나는 %s를 좋아해요."%"파이썬")
# # print("Apple은 %c로 시작해요."%"A")
#
# #%s
# #print("나는 %s살입니다."%20)
# print("나는 %s색과 %s색을 좋아해요."%("파란", "빨간"))
#
#
#
# #방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))
#
# #방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20,color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))
#
# #방법4(v3.6이상)
# age=20
# color="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
#
#
# #탈출문자
# print("백문이 불여일견\n백견이 불여일타")
#
# #저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩" 입니다.')
# print("저는 \"나도코딩\"입니다.")
#
# #\\: 문장 내에서 \로 표시됨
# print("C:\\Users\\NADOCOIdslafjlg")
#
# #\r: 커서를 맨앞으로 이동
# print("Red Apple\rPine") #이해가잘안됨
#
# #\b: 백스페이스(한글자삭제
# print("Redd\bApple")
#
# #\t:탭
# print("Red\tApple")
#
#
#
# #Quiz)사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# # 예) http://naver.com
# # 규칙1: http://부분은 제외 =>naver.com
# # 규칙2: 처음만나는점(.)이후 부분은 제외 => naver
# # 규칙3: 남은 글자중 처음 세자리+글자갯수+글자 내 'e'갯수 +"!"로 구성
# #                     nav   5               1       !
# # 예) 생성된 비밀번호: nav5!
#
#
# url="http://youtube.com"
#                         #http:// 을 ---> " "공백으로 만든다는 말
# my_str = url.replace("http://","") #규칙1
# my_str=my_str[:my_str.index(".")] #my_str[0:5]
# print(my_str)
#
# password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))
#
#
# #리스트[]
#
# #지하철 칸별로 10명, 20명, 30명
# # subway1=10
# # subway2=20
# # subway3=30
#
# subway=[10,20,30]
# print(subway)
# #          0       1        2
# subway=["유재석","조세호", "박명수"]
# print(subway)
#
# #조세호씨가 몇번재 칸에 타고있는가
# print(subway.index("조세호"))
#
#
# #하하씨가 다음정류장에서 다음칸에 탐
# subway.append("하하")
# print(subway)
#
# #정현돈씨를 유재석/ 조세호 사이에 태워봄
# subway.insert(1,"정형돈")
# print(subway)
#
#
# #지하철에 있는사람을 한명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
#
# print(subway.pop())
# print(subway)
#
# print(subway.pop())
# print(subway)
#
# #같은 이름의 사람이 몇명 잇는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))
#
# #정렬도 가능
# num_list=[5,2,4,3,1]
# num_list.sort()
# print(num_list)
#
# #순서뒤집기 리버스
# num_list.reverse()
# print(num_list)
#
# #모두 지우기
# num_list.clear()
# print(num_list)
#
# #다양한 자료형과 함께 사용
# num_list=[5,4,3,2,1]
# mix_list=["조세호",20,True]
# print(mix_list)
#
# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)
#
#
# #사전
# cabinet={3: "유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
#
# print(cabinet.get(3))
# #print(cabinet[5])  오류나고 종료됨
# #print(cabinet.get(5))  없다고 뜨고 다음줄 실행
# #print(cabinet.get(5,"사용가능")) 값이 있으면 값출력 없으면 "사용가능"을 출력함
# print("hi")
#
# print(3 in cabinet) #3이라는 키가 캐비넷에 있으면True
# print(5 in cabinet)
#
# cabinet={"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])
#
# #새손님
# print(cabinet)
# cabinet["A-3"]="김종국"
# cabinet["C-20"]="조세호"
# print(cabinet)
#
# #간 손님
# del cabinet["A-3"]
# print(cabinet)
#
# #key들만 출력
# print(cabinet.keys())
#
# #key, value 쌍으로 출력
# print(cabinet.items())
#
# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)
#
#
#
# #튜플 --내용변경과 추가가 불가능
# menu=("돈까스","치즈까스")
# print(menu[0])
# print(menu[1])
#
# # menu.add("생선까스")  불가능
#
# name="김종국"
# age=20
# hobby="코딩"
# print(name,age,hobby)
#
#
#
# #튜플의 경우
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name,age,hobby)
#
#
#
# #집합(set)
# #중복안됨, 순서 없음
# my_set={1,2,3,3,3}
# print(my_set)
#
# java={"유재석", "김태호", "양세형"}
# python=set(["유재석", "박명수"])
#
# #교집합(java와 python을 모두 할 수 있는 개발자)
# print(java&python)
# print(java.intersection(python))
#
# #합집합(java 도 할수있거나 python을 할수잇는개발자)
# print(java|python)
# print(java.union(python))
# #순서그대로 출력안되고 그냥 보이는거 출력함
#
# #차집합(java는 할수있지만 python은 할줄모르는개발자
# print(java-python)
# print(java.difference(python))
#
# #python할줄아는사람이 늘어남
# python.add("김태호")
# print(python)
#
# #java를 잊었어요
# java.remove("김태호")
# print(java)
#
#
#
# #자료구조의 변경
# #커피숍
# menuA={"커피","우유","주스"}
# print(menuA,type(menuA))
#
# menuA=list(menuA)
# print(menuA,type(menuA))
#
# menuA=tuple(menuA)
# print(menuA,type(menuA))
#
#
# menuA=set(menuA)
# print(menuA,type(menuA))
#
#
# #퀴즈
#
# from random import *
# lst=[1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))
#
#
#
#
# from random import *
# users = range(1,21)#1~20까지 생성
# # print(type(users))
# users=list(users)
# # print(type(users))
#
# print(users)
# shuffle(users)
# print(users)
#
# winners=sample(users,4) #4명중 1명치킨 3명 커피
#
# print("--당첨자발표--")
# print("치킨: {0}".format(winners[0]))
# print("커피: {0}".format(winners[1:]))
# print("ㅊㅊ")

#--------------------------------------------------
#if
# weather=input("오늘 날씨는 어때요? ")
# if weather=="비" or weather=="눈":
#     print("우산을 챙기세요")
# elif weather=="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")
#
#
# temp = int(input("기온은 어때요? "))
# if 30<= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10<=temp and temp<30:
#     print("괜찮은 날씨에요")
# elif 0<=temp<10:
#     print("외투를 챙기세요")
# else:
#     print("너무추워요. 나가지마세요.")
#
#
#
# #for
# print("대기번호 : 1")
# print("대기번호 : 2")
#
# for waiting_no in [0,1,2,3,4]:  #숫자 말고 range가 들어가도 됨 ㅇㅇ
#     print("대기번호: {0}".format(waiting_no))

# starbucks =["아이언맨","토르","아이엠그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

#whlie문
# customer="토르"
# index = 5
# while index>=1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
#     index-=1
#     if index==0:
#         print("커피는 폐기처분되었습니다.")


# customer="아이언맨"
# index=1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출{1}회".format(customer,index))
#     index+=1

# customer="토르"
# person = "Unknown"
#
# while person !=customer:
#     print("{0}, 커피가 준비되었습니다. ".format(customer))
#     person=input("이름이 어떻게 되세요?  ")

#continue 와 break

# absent = [2,5]#결석
# no_book =[7]
# for student in range(1,11): #1~10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지, {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#한줄for문
# 1-->101로 바꾸는거

# students = [1,2,3,4,5]
# print(students)
# students=[i+100 for i in students]
# print(students)


#Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을때, 총 탑승 수를 구하는 프로그램을 작성하시오.

#조건1: 승객별 운행 소요 시간은 5분~50분 사이 난수
#조건2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

# from random import *
# cnt= 0 #총 탑승객 수
# for i in range(1,51): #1~50이라는 수 (승객)
#     time = randrange(5,51) #5-50분 소요시간
#     if 5<=time <=15:
#         print("[0] {0}번째 손님(소요시간: {1}분)".format(i,time))
#         cnt+=1
#     else:
#         print("[ ] {0}번째 손님(소요시간: {1}분)".format(i, time))
# print("총 탑승 승객: {0} 분".format(cnt))


#함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money
def withdraw(balance, money):
    if balance>=money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은{0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지않았습니다. 잔액은{0}원입니다.".format(balance))
        return balance
def withdraw_night(balance, money): #저녁에 출금
    commission=100 #수수료100원
    return commission, balance - money - commission

balance=0 #잔액
balance=deposit(balance,1000)
# balance=withdraw(balance,2000)
# balance=withdraw(balance,500)
commission, balance = withdraw_night(balance, 500)
print("수수료{0}원이며, 잔액은{1} 원입니다.".format(commission, balance))



#기본값
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용언어: {2}"\
#           .format(name,age,main_lang))
#
# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")
# 같은학교 같은 학년 같은반 같은수업

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이: {1}\t주 사용언어: {2}"\
#           .format(name,age,main_lang))
# profile("유재석")
# profile("김태호")

# #키워드값
# def profile(name, age, main_lang):
#     print(name,age,main_lang)
# profile(name="유재석",main_lang="파이썬",age=20)
# profile(main_lang="자바",age=25, name="김태호")
#
#
# #가변인자
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름: {0}\t나이: {1}\t".format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)
#
# profile("유재석",20,"Python","Java","C","C++","C#")
# profile("김태호",25,"Kotlin","Swift","","","")

#-----가변인자2
# def profile(name,age,*language):
#     print("이름: {0}\t나이: {1}\t".format(name,age),end=" ")
#     for lang in language:
#         print(lang,end=" ")
#     print()
#
# profile("유재석",20,"Python","Java","C","C++","C#")
# profile("김태호",25,"Kotlin","Swift","","","")
#
#
# #지역변수(일부사용가능),전역변수(모든곳에서사용가능)
#
# gun=10 #전역변수
#
# def checkpoint(soldiers):
#     global gun #전역 공간에 있는 gun을 사용(위에 gun=10이라쓰인거)
#     gun = gun-soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#
# def checkpoint_ret(gun,soldiers):
#     gun=gun-soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun
# print("전체 총: {0}".format(gun))
# # checkpoint(2) #2명이 경계근무나감
# gun=checkpoint_ret(gun,2)
# print("남은총: {0}".format(gun))
#
#
# #Quiz 표준체중을 구하는 프로그램을 작성하시오
# #   *표준체중: 각 개인의 키에 적당한 체중
# #   (성별에따른공식)
# #   남: 키m * 키m *22
# #   여: 키m * 키m *21
#
# def std_weight(height,gender):
#     if gender =="남자":
#         return height*height*22
#     else:
#         return height * height * 21
#
# height = 175 #cm단위
# gender="남자"
# weight=round(std_weight(height/100,gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))


# #학생이름을 길이로 변환
# students=["Iron man", "Thor","I am groot"]
# students=[len(i) for i in students]
#
# print(students)
#
# #학생이름을 대문자로 변환
# students=["Iron man", "Thor","I am groot"]
# students=[i.upper()for i in students]
# print(students)

