class Celebrity:
    def __init__(self, name):

        #이름
        self.name=name

        #group

    def set_name(self, name):
        self.name=name

    def set_entertainment(self,entertainment):
        self.entertainment=entertainment

    # def info(self):  #우리 클래스가 가지고 있는걸 출력
    #     print(f'이름: {self.name}\t소속사: {self.entertainment}')

    def __str__(self):
        return f'이름: {self.name}\t소속사: {self.entertainment}'


# IU = Celebrity('이지은')    #new Celebrity() ---in java/python은 없음
# # IU.set_name('이지은')
# IU.set_entertainment('이담')
# IU.info()
# print(IU.name, IU.entertainment)
# print(IU)           #클래스의 __str__() 호출됨
#
# 소연 = Celebrity('전소연')
# # 소연.set_name('전소연')
# 소연.set_entertainment('CUBE')
# 소연.info()


class Talent(Celebrity):
    def __init__(self,name):
        super().__init__(name)      #Celebrity클래스(부모클래스)의 생성자 호출

    def set_drama(self,drama):
        self.drama=drama


    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'
        # return f'이름:{self.name}|\t소속사: {self.entertainment}|\t드라마: {self.drama}'



이광수 = Talent('이광수')
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)


class Singer(Celebrity):
    def __init__(self,name,song):      #변수의 값을 처음으로 세팅하는 함수__init__
        super().__init__(name)              #self.name=name
        self.song=song
    def __str__(self):       #리턴받는 애들을 str로 변환하는 함수
        return super().__str__()+f'\t노래: {self.song}'


현진=Singer('현진','新메뉴')
현진.set_entertainment('JYP')
print(현진)
필릭스=Singer('필릭스','Back Door')
필릭스.set_entertainment('JYP')
print(필릭스)

스트레이키즈=[]
스트레이키즈.append(현진)
스트레이키즈.append(필릭스)
print(스트레이키즈)

for 멤버 in 스트레이키즈:        #i 현진이라는 객체가 들어감..
    print(멤버)

# for i in range(len(스트레이키즈)):  #i: 0, 1
#     print(스트레이키즈[i])