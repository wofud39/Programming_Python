class Recipe:


    def __init__(self, name):
        # 재료, 재료의 개수(양)
        self.ingredient = {}    #{}가 딕션어리임Dictionary    마지막에 오는 애로 값이 변경됨

        # 내용-----------------------
        self.contents = ''

        # 이름-----------------------
        self.name = name

        # 몇 인분인지-----------------
        self.people = 1

        # 영상 링크-------------------
        self.video = ''



    def set_contents(self):
        contents = input('레시피 내용을 입력하세요: ')
        self.contents='입력된 정보가 없습니다.' if contents=='' else contents

    def set_people(self):
        people = input('몇 인분인가요?: ')
        self.people = '1' if people=='' else people


    def set_video(self):
        video = input('레시피 url을 입력하세요: ')
        self.video ='입력된 정보가 없습니다.' if video=='' else video

    def set_ingredient(self):
        while True:
            ingredient = input("재료를 입력하세요: (입력예시: '감자 100')\n모든 재료 입력이 끝났으면 ENTER키를 누르세요.")
            if ingredient=='':
                break
            ingredient_name, ingredient_gram = ingredient.split()
            #'감자 200'.split() -->  '감자','200'
            self.ingredient[ingredient_name]=ingredient_gram

        #=====>>>>>>>>  split안에다가 나눌 기준을 작성     재령 = 재령 존재함 --재령.split()-->띄어쓰기임 빈칸으로 냅둔다는건
                                                                                    # '재령' '존재함' 이렇게 나눠짐


    def __str__(self):
        return f'\n레시피: {self.name}\n양: {self.people}인분\n정보: {self.contents}\n영상링크: {self.video}\n재료: {self.ingredient}'
    

    def set_recipe(self):
        self.set_people()
        self.set_ingredient()
        self.set_contents()
        self.set_video()
    
    
# 카레 = Recipe('카레')
# 카레.set_recipe()
#
#
# print(카레)
