# 13.다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]

summ = 0
for x in nums:
    summ += x
avg = summ/len(nums)
print('평균: ',avg)