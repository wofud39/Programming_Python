from builtins import enumerate


class Drink:
    # 클래스(내용 수정못하게 튜플로)
    _CUPS = ('레귤러','점보')                #기본값=='레귤러'
    _ICES = ('0%','50%','100%','150%')     #기본값=='100%'
    _SUGARS = ('0%', '50%', '100%', '150%')#기본값=='100%'

    def __init__(self,name,price):   #초기화
        self.name=name
        self.price=price
        self.cup= 0         #'레귤러'       Drink._CUPS[self.cup]이걸써서 부른거임
        self.ice= 2         #'100%'
        self.sugar= 2       #'100%'

    def set_cup(self):
        for index,cup in enumerate(Drink._CUPS):     #컴 종류 보여주기
            print(f'{index+1}: {cup}')

        #컵선택하기
        cup=input('컵사이즈를 선택하세요: ')
        if cup=='':
            self.cup=0
        else:
            cup = int(cup)
            self.cup = cup - 1    #컵self에 넣자

        if self.cup==1:           #점보면, +500
            self.price+=500

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):          #얼음량 종류 보여주자
            print(f'{index+1}: {ice}')
        ice = input('얼음량을 선택하세요: ')        #선택하자
        if ice=='':
            self.ice = 2
        else:
            self.ice= int(ice)-1

        # self.ice = 2 if ice == '' else int(ice)-1
        #|||||    if뒤에꺼이면 self.ice= 2! 아니면 else 뒤에꺼꺼
        #slf.ice에 설정하자

    def set_sugar(self):
        #당도 종류 보여주자
        for index, sugar in enumerate(Drink._SUGARS):
            print(f'{index+1}: {sugar}')
        sugar = input('당도를 선택하세요: ')
        if sugar=='':
            self.sugar=2
        else:
            sugar=int(sugar)-1
            self.sugar=sugar
        #당도 선택하자
        #self.sugar에 넣자

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):    #프린트할떄 return
        return f'이름: {self.name}\t가격: {self.price}원'+f'\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}'+f'\t당도: {Drink._SUGARS[self.sugar]}'




class Coffee(Drink):     #Drink를 다 상속 받음
    pass



class Bubbletea(Drink):
    _PEARLS = ('타피오카', '화이트', '알로에', '젤리')
    def __init__(self, name, price):
        super().__init__(name,price)        #부모초기화 호출
        self.pearl = 0      #'타피오카'

    def set_pearl(self):

        #펄종류 보여주자
        for index, pearl in enumerate(Bubbletea._PEARLS):
            print(f'{index+1}: {pearl}')
        pearl = input('펄을 선택하세요: ')


        #self.pearl에 넣자자
        #---------------------------
        # self.pearl = 0 if pearl =='' else int(pearl) -1
        if pearl=='':
            self.pearl=0
        else:
            pearl=int(pearl)-1
            self.pearl=pearl
        #펄종류보여주자
        #펄 선택하자
        #self.pearl에 넣자


    def order(self):
        

        super().order()
        self.set_pearl()
        # 부모 클래스의 order()호출하자
        # set_pearl() 호출하자


    def __str__(self):
        
        result = super().__str__() #부모클래스를 부름
        return result+f'\t펄종류: {Bubbletea._PEARLS[self.pearl]}'
        #부모클래스의 __str__() (이름, 가격, 컵사이즈, 얼음량, 당도, 펄)


class Order:
    def __init__(self):
        self.menu = []#self.menu 매장에 있는 음료수 전체
        self.init_menu()#init_menu()
        self.order_menu = []#self.order_menu 내가 고른 메뉴들

    def init_menu(self):
        사랑이꺼 = Coffee('카페모카', 2500)
        하람이꺼 = Bubbletea('오레오 쉐이크', 3900)
        에스더꺼 = Bubbletea('타로 밀크티', 3300)
        self.menu.append(사랑이꺼)  #Ctrl + D 누르면 복사 붙여넣기 ㄱㄴ
        self.menu.append(하람이꺼)
        self.menu.append(에스더꺼)


    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1}: {drink.name}\t{drink.price}원')

    def sum_price(self):
        sum_value=0#self.order_menu 하나씩꺼내서 그 Drink의 가격을 합계내고 리턴
        for drink in self.order_menu:
            sum_value +=drink.price
        return sum_value



    def order_drink(self):

        while True:     #반복
            self.show_menu()    #메뉴 보여주자
            drink = input('메뉴를 선택하세요: ')    #메뉴 선택하자
            drink = int(drink) - 1
            new_drink  = self.menu[drink]
            new_drink.order()   #옵션 선택하자
            self.order_menu.append(new_drink)   #self.order_menu에 추가하자
            is_add = input('더 주문하시겠니까? (n: 종료)')    #더 주문?
            if is_add == 'n':
                break
        print(self) #주문내역 보여주자


    def __str__(self):
        s = '-'*20 + '주문 내역'+'-'*20 +'\n'    #주문내역 제목보여주자
        for drink in self.order_menu:      #주문한 음료수들 목록 보여주자
            s+=str(drink)
        s += f'총금액: {self.sum_price()}원'#총 합계 가격 보여주자
        return s


# 사랑이꺼 = Drink('밀크티',2500)
# 사랑이꺼.order()
# print(사랑이꺼)

# 사랑이꺼 = Coffee('카페모카',2500)
# 사랑이꺼.order()
# print(사랑이꺼)

# 하람이꺼 = Bubbletea('오레오 쉐이크', 3900)
# 하람이꺼.order()
# print(하람이꺼)


order=Order()
order.order_drink()