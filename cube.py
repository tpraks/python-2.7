
cube_num = 0
while True:
	cube_num = raw_input("Enter Number to find if its a cube: ")
	if ( cube_num == 1 ):
		print ('It is ', str(cube_num), ' cube')
	num=2
	while (num**3 <= int(cube_num)):
		if ( num**3 == int(cube_num) ):
			print (str(cube_num), ' is ', str(num), ' cube')
			#quit()
			break
		else:
			num += 1
	print (str(cube_num), ' is not cube ')
