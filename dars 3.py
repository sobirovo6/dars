ism0 = {
'ism': 'Abu ali inin sinona',
'yil': 810,
 'shahar': 'buxoro',
 'umir': 60,

}

ism1 = {
'ism': 'abdla qodiriy',
'yil': 1894,
 'shahar': 'toshkent',
 'umir': 44,

}
ism2 = {
'ism': 'alisher',
'yil': 1441,
 'shahar': 'xirotda',
 'umir': 60,
}
cars =[ism0,ism1,ism2]
for car in cars:
 print(f"{car['ism'].title()},"
 f"{car['yil'] }-yilda tugilgan, "
 f"{car['shahar']}-tugilgan, {car['umir'] }-umir korgan"
 )
