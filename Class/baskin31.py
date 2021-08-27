class Icecream:
    def __init__(self, name):       #생성자. 주로 변수 초기화
        self.name=name  #다른곳에서도 name을 쓸 수 있게함



    #이름: name
    #설명: explanation
    def set_explanation(self, explanation):
        self.explanation=explanation

    def __str__(self):              #객체를 우리가 알아보기 쉽게 문자열로 리턴, 주로 print()에서 호출
        return f'이름: {self.name}'


# 아이스홈런볼 = Icecream('아이스홈런볼')
# 아이스홈런볼.set_explanation('초콜릿아이스크림과 바닐라 아이스크림 속에 초코코팅 홈런볼과 피넛이 쏙쏙!')
# print(아이스홈런볼)
# print(아이스홈런볼.explanation)
#
#
# 엄마는외계인 = Icecream('엄마는외계인')
# 엄마는외계인.set_explanation('오랫동안 먹었는데 맛있음')
# print(엄마는외계인)
# print(엄마는외계인.explanation)
#
#
# 베리베리스트롱베리=Icecream('베리베리스트롱베리')
# print(베리베리스트롱베리)
#
#
# t31요거트=Icecream('31요거트')
# print(t31요거트)
#


class Order:

    _CATEGORIES = ['싱글레귤러','더블레귤러','파인트']
    _PRICES=(3200, 6200, 8200)

    # 컵의 크기(종류)
    def __init__(self):
        #종류(컵)
        self.set_cateries()
        #메뉴
        self.menu=[]
        self.init_menu()

        #주문한메뉴
        self.order_menu=[]



    # 가격
    def __str__(self):
        pass
    def set_cateries(self):
        for index, category in enumerate(Order._CATEGORIES):   #index랑 값 둘다 꺼내줌
            print(index+1, category)
        category_num=input('종류를 골라주세요: ')
        self.category = int(category_num)


    def init_menu(self):
        self.menu.append(Icecream('엄마는외계인'))
        self.menu.append(Icecream('베리베리스트롱베리'))
        self.menu.append(Icecream('31요거트'))


    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(f'{index+1}. {icecream}')

    def order(self):
        self.show_menu()  #아이스크림 보여주자(메뉴보여주자)
        for _ in range(self.category):    #종류에 따라 반복
            # 메뉴 선택
            icecream=input('아이스크림을 골라주세요: ')
            icecream = int(icecream)
            # 주문한 메뉴에 추가하자
            self.order_menu.append(self.menu[icecream-1])
        # 종류 출력하자
        print('-'*10 + '주문 내역입니다'+'-'*10)
        print(Order._CATEGORIES[self.category-1])
        print(str(Order._PRICES[self.category-1])+'원')

        # 주문한 메뉴 출력하자자
        for icecream in self.order_menu:
            print(icecream)




        #종류를 고른다(싱글레귤러, 더블레귤러, 파인트)
        #메뉴 초기화하자
        #아이스크림 보여주자(메뉴보여주자)
        #종류에 따라 반복
            #메뉴 선택
            #주문한 메뉴에 추가하자
        #종류 출력하자
        #주문한 메뉴 출력하자자

order=Order()
order.order()

