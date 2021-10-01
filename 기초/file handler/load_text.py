# load text, readline, split
#매우중요

#commit메세지 바꾸기..? push하기 전까지 바꿀 수 있음

f = open('text.txt', 'r',encoding='utf-8')

data = f.read()


#decode 는 사람이 알아듣기 위해

f.close()
print('한꺼번에 읽기: ')  #파일이 크면 굉장히 느리다 #작으면 뭐 제일빠르겠지만
print(data)


# *************************************************
with open('text.txt', 'r', encoding='utf-8'):
    data = f.read()
print(data)

# *************************************************



print('\n한줄 씩 읽기: ')  #한줄씩읽어서 출력하되 빈칸이면 멈춰라~ **가장많이쓰임
f = open('text.txt ','r', encoding='utf-8')

while True:
    line = f.readline()  #이거 2번반복하면 2줄나옴
    if line =='':
        break

    print(line.rstrip()) #line의 오른쪽에있는 빈칸이 사라진다. \n삭제
    #or   --> line.replace('\n','')


#내려쓰기 안하려면? '\n' == ' '이 원인임


f.close()



print('-'*40)  #다 읽고 줄별로 짜르기 이거는 2번째로 많이 쓰임
print('전체를 한꺼번에 읽고, 줄 별로 리스트')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines() #한번에 다 읽고
f.close()

for line in lines: #리스트를 한줄씩 출력
    print(line.rstrip())



#quiz
print('-'*40)
#이름: 김미림[tab]좋아하는 색: 파랑색
#이름: 이정보[tab]좋아하는 색: 하늘색
f = open('text.txt', 'r', encoding='utf-8')

for line in lines:
    # print('이름:'+line.rstrip()[:3]+"\t좋아하는 색: "+line.rstrip()[:-3])
    # line = '고에스더:검은색'
    data = line.split(':') #['고에스더', '검은색']

    print('이름:'+data[0].rstrip()+"\t좋아하는색: "+data[1].rstrip())



f.close()
