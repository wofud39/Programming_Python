#12.다음 리스트에 저장된 데이터의 개수를 화면에 구하라.

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자",
        "김치만두", "쫄면", "쏘세지", "라면", "팥빙수",
        "김치전"]

a = len(cook)
print("전체: ",a)

b = len(set(cook))
print("중복제거: ", b)

#-------------------------------------
#중복제거 1
result = list()
for x in cook:
    if x not in result:
        result.append(x)
    else:
        continue

c = len(result)
print(c)


#-------------------------------------
# 중복제거 2
result = dict()
for i in cook:
    result[i] = 1

d = len(result)
print(d)

