interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

string = ""
for x in interest:
    string+=(x+" / ")
# string += (interest[0]+"/")
# string += (interest[1]+"/")
# string += (interest[2]+"/")
# string += (interest[3]+"/")
# string += (interest[4]+"/")

print(string[:-2])

# "산성전자/LG전자/Naver/SK하이닉스/미래에셋대우"

a = "/ ".join(interest)
print(a)