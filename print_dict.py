cars = {'A':{'speed':70,
        'color':2},
        'B':{'speed':60,
        'color':3}}

for keys,values in cars.items():
	print keys
	for ikeys,ivalues in values.items():
		print ikeys,":",ivalues

for key in cars.keys():
	print key


for item in cars.items():
	print item

cars2 = cars.copy()
for key in car2.keys():
	print key

cars2.clear()
for key in car2.keys():
	print key

