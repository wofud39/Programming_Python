import math
num = '62421'
print(num[-2:])
if int(num[-2:]) > 50:
    print(num.replace(int(num[-3]),int(num[-3])+1))
else:

    print(num.replace(int(num[-2:]), 00))