#10.movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

#방법1
a = movie_rank
del a[3]
print(a)



#방법2
result = list()
for x in movie_rank:
    if x !='럭키':
        result.append(x)
    else:
        continue
print(result)