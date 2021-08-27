#모듈
# import theater_module
# theater_module.price(3) #3명이서 영화보러갔을때 가격
# theater_module.price_morning(4)
# theater_module.price_soldier(5)
#
# import theater_module as mv
# mv.price(3)

# from theater_module import *
# price(3)
# price_morning(4)

# from theater_module import price, price_morning
# price(5)
#
#
# from theater_module import price_soldier as price
# price(5)



# #패키지
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
# #
# # from travel.thailand import ThailandPackage #가능!
# from travel import victnam
# trip_to = victnam.VietnamPackage()
# trip_to.detail()

from travel import *
trip_to = victnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()