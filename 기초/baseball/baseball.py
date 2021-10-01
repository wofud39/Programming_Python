from baseball_game import make_answer, check
from costum_err import InvalidlengthengthError
answer = make_answer()

count = 0
#무한반복
while True:
#숫자 ask
    print(f"\n질문횟수 {count}")
    guess = input('뭘까? ')
    count+=1
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue
    if len(guess) != len(answer):
        # raise InvalidlengthengthError('정답의 길이와 다릅니다.')
        print(f'정답의 길이와 다른 것을 입력했네요  {len(answer)}문자')
        continue
#strike, ball 판정하기
    strike, ball = check(guess, answer)
#출력
    print(f'{guess}  strike: {strike}, ball: {ball}')
#정답==숫자, 끝내기
    if answer==guess:
        print('정답입니다.')
        break
