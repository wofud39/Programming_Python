#5-1. 모듈이란?
# 다른파일에 적힌 함수를 지금 내가 쓸 파일로 가져오는것


#5-2. 패키지란?
# 모듈을 크게 감싸는것 class

#5-3.  theater_module.py 모듈(파일)의 price 함수를
# p학번 라는 이름으로 호출 하도록 import문을 작성하세요
from theater_module import price as p2415
p2415(3)


#5-4. __all__의 역할은?
# from travel import * 를 썼을때 그냥 안불러와진다
# __all__ = ["victnam"] 과 같은 식으로 쓰면 victnam의 것을 모두 가져온다.



#5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고,
# 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
if __name__=="__main__":
    print("모듈에서실행")
    #실행문
else:
    print("외부에서 실행")



#5-6.  travel 패키지(폴더) 안에
# vietnam.py 모듈(파일) 안의 VietnamPackage 클래스를 생성하고
# detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?


import travel.victnam
#< 가 >

# import travel.victnam
# a = travel.victnam.VietnamPackage()
# a.detail()


#=====================================
from travel import victnam
#< 나 >

# from travel import victnam
# a = victnam.VietnamPackage()
# a.detail()

#=====================================
from travel.victnam import VietnamPackage
#< 다 >
from travel.victnam import VietnamPackage
a = VietnamPackage()
a.detail()