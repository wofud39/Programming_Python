with open('binary.bin','wb') as f: #wb는 이진수를 쓴다는 이야기
    byte_list = bytes([255, 0, 127]) #bytes() 011010101,1111이런식으로
            #8비트 최대, 최소, 중간
    f.write(byte_list)