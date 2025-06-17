
total = 0
for digit in range(1, 11):
	if digit % 4 == 0:
		for i in range(1, 6):
			total += digit ** i

print(total ** 2)