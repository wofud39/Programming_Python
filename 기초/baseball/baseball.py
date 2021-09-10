answer = make_answer()
print(answer)


#무한반복
while True:
#숫자 ask
    guess = input('뭘까? ')
#strike, ball 판정하기
    strike, ball = check(guess, answer)
#출력
    print(f'{guess}\strike: {strike}, ball: {ball}')
#정답==숫자, 끝내기
    if answer==guess:
        print('정답입니다.')
        break
