# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
#
# print(summa(1,2))
# print(summa(10,11,28,1,28,28,23,34))
#
# def summa(*sonlar):
#     return sum(sonlar)
#
# print(summa(4,3,2,1,3,4,5,4,3,2,1))
#
#
# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)
#
# print(summa(4,10,3838838383))
#
# def avto_info(komponiya, model, **malumotlar):
#     malumotlar['komponiya']=komponiya
#     malumotlar['model']=model
#     return malumotlar
#
# avto1 = avto_info("gm", 'malibu', rang='qora', yil=2018)
# avto2 = avto_info('kia', 'k5', rang='oq', narh=350000 , karopka='avto')
#
# print(avto1)
# print(avto2)
#
