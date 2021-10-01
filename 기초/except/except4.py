list1 = [1,2,3]

try:
    print(list1[0])
    print(list1[1])
    print(list1[2])
    # print(list1[3])
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
except:
    print('error')
else: #예외가 발생x 실행
    print('It is work well.')
finally: #무조건 실행
    print('finally')