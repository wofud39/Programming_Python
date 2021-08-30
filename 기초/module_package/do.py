# import my_module
# my_module.나라친구()





# from tour.jeonnam import 채리
# 채리()
# import tour.jeonnam as tj
# tj.채리()
#
# from tour import jeonnam as je  #tour >jeonnam
# je.채리()
#
# from tour.jeonnam import 채리 as cherry
# cherry()
# #채리()  NameError: name '채리' is not defined



from tour import *
jeonnam.채리() #__all__ = ['jeonnam']     *tour>__init__.py 에서 만들어두면됨.
#jeonnam.채리() >>자바에선 됨/ 파이썬에선 안됨

gp = gangwondo.GangwondoPackage()  #__init__에서 __all__리스트에 gwaondo를 써주면된다.
print(gp)