ticket_price = int(input('Enter your ticket price: '))
if ticket_price <= 0:
	print('Error: Price cannot be negative or 0!')
else:
	bonus_points = int(input('How many bonus points you have?: '))
	if bonus_points < 0:
		print('Error: Amount of bonus points cannot be negative!')
	else:
		if bonus_points >= ticket_price:
			bonus_points_remain = bonus_points - ticket_price
			print('Congratulations! Your ticket is free!')
			if bonus_points_remain > 0:
				print('Bonus remaining:', bonus_points_remain)
		else:
			total_price = ticket_price - bonus_points
			print('Total ticket price:', total_price)
			if bonus_points > 0:
				print('All bonus points have been used')