total = int(input('Enter money amount: '))
if total < 0:
	print('Error: money amount cannot be negative!')
elif total == 0:
	print('Money amount is 0 - no need to solve!')
else:
	bank_th = total // 1000
	total %= 1000
	
	bank_hun = total // 100
	total %= 100
	
	coin_ten = total // 10
	total %= 10
	
	coin_one = total
	
	print('1000:', bank_th)
	print('100:', bank_hun)
	print('10:', coin_ten)
	print('1:', coin_one)
