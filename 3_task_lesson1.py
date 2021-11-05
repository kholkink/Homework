for i in range(1, 11):
	if i == 1:
		print(i, 'процент')
	elif i == 2 or i == 3 or i == 4:
		print(i, 'процента')
	else:
		print(i, 'процентов')
for i in range(11, 20):
	print(i, 'процентов')
for i in range(21, 101):
	if i%10 == 1:
		print(i, 'процент')
	elif i%10 == 2 or i%10 == 3 or i%10 == 4:
		print(i, 'процента')
	else:
		print(i, 'процентов')


'''
for i in range(11, 101):
	if i % 10 == 1:
		print(i, 'процент')
	if i % 10 == 2 or 3 or 4:
		print(i, 'процента')
	if i % 10 == 5 or 6 or 7 or 8 or 9 or 10:
		print(i, 'процентов')
'''
