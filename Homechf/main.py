from recipe_book import RecipeBook


def print_menu():
    print('1. 레시피 검색')
    print('2. 레시피 추가하기')
    print('3. 재료로 검색하기')
    print('4. 전체 레시피 보여주기')
    print('5. 종료하기')
    num = input('메뉴를 선택하세요: ')

    return num

def main():
    recipe_book204 = RecipeBook()



    while True:
        num = print_menu()
        if num == '1':
            #레시피 검색
            recipe_book204.search_recipe()

        elif num=='2':
            #레시피 추가하기
            recipe_book204.add_recipe()

        elif num=='3':
            #재료로 검색하기
            recipe_book204.search_ingredient()

        elif num=='4':
            #전체 레시피 보여주기
            recipe_book204.show_recipe()

        elif num=='5':
            break
        else:
            print("다시 입력하시오: ")


if __name__ == '__main__':
    main()