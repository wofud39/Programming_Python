f = open('text.txt','w',encoding='utf-8')


#다 가져오는게 아니라 한줄 한줄 읽어오는것임
f.write('AAA : ')
f.write('파란색')


f.write('\n')


f.write('BBB : ')
f.write('보라색')

f.close()


#파이썬 권장코드
with open('text.txt','w', encoding='utf-8') as f:
    f.write('김모씨:')
    f.write('파랑색')
    f.write('\n')
    f.write('이모씨:')
    f.write('하늘색')

    # 여긴 close없이 벗어나면 바로 close해준다.