mass = []
number = 0
full_number = 0
for i in range(2, 1000, 2):
	mass.append(i**3)
for i in range(len(mass)):
	print(mass[i])
	while mass[i] / 10 >= 0.1:
		number = number + mass[i] % 10
		mass[i] = mass[i] // 10
	if number == 17:
		full_number = full_number + number
		print(full_number)
	number = 0
print(full_number)


