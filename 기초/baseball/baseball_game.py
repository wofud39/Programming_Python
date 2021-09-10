# 베이스볼 문제

#정답제작: 0~9 세개 뽑기
def make_answer():
    return "381"

def check(guess, answer):
    strike = 0
    ball = 0
    guess[0] in answer



    for x in range(3):
        if guess[x] == answer[x]:
            strike+=1
        for i in range(3):
            if guess[x] == answer[i]:
                ball+=1
    ball = ball-strike
    return strike, ball


    # for i in range(3):
    #     for j in range(3):
    #         if guess[i] ==answer[j]:
    #             if i==j:
    #                 strike+=1
    #             else:
    #                 ball +=1

if __name__ == '__main__':
    answer = make_answer()
    print(answer)
    strike, ball = check("832", "934")
    print(strike, ball)
    strike, ball = check("431", "934")
    print(strike, ball)
    strike, ball = check("934", "934")
    print(strike, ball)