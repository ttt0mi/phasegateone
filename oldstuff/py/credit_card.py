def card_number_check(card_number):

	if len(card_number) not in range(13, 17): return False		

	if card_number.isdecimal(): return True
	else: return False



def credit_card_validator(card_number):
	
	sum = 0
	for index in range(len(card_number) - 2, -1, -2):

		digit = int(card_number[index])
		num = digit * 2
		if num > 9:
			num = (num % 10) + 1
		sum += num

	for index in range(len(card_number) - 1, -1, -2):

		digit = int(card_number[index])	
		sum += digit
	
	if sum % 10 == 0: return True
	else: return False



def cardIssuer(validity, card_number, checker):
	
	if checker:
		if card_number[:2] == "37":
			validity.update({'Credit Card Type': 'American Express', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'valid'})
			return validity

		elif card_number[0] == "4":
			validity.update({'Credit Card Type': 'Visa', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'valid'})
			return validity

		elif card_number[0] == "5":
			validity.update({'Credit Card Type': 'MasterCard', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'valid'})
			return validity

		elif card_number[0] == "6":
			validity.update({'Credit Card Type': 'Discover', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'valid'})
			return validity

		else:
			validity.update({'Credit Card Type': 'Invalid Card', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'invalid'})
			return validity


	else:
		if card_number[:2] == "37":
			validity.update({'Credit Card Type': 'American Express', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'invalid'})
			return validity

		elif card_number[0] == "4":
			validity.update({'Credit Card Type': 'Visa', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'invalid'})
			return validity

		elif card_number[0] == "5":
			validity.update({'Credit Card Type': 'MasterCard', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'invalid'})
			return validity

		elif card_number[0] == "6":
			validity.update({'Credit Card Type': 'Discover', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'invalid'})
			return validity

		else:
			validity.update({'Credit Card Type': 'Invalid Card', 'Credit Card Number': card_number, 'Credit Card Length': len(card_number), 'Credit Card Status': 'invalid'})
			return validity



"""

validity = {}
while True:

	card_number = str(input("what is your card number? "))
	
	if not card_number_check(card_number):
		print("Invalid, try again")
		continue

	
	checker = credit_card_validator(card_number)

	dict = cardIssuer(validity, card_number, checker)

	for key, value in dict.items():
		print(f"{key}: {value}")
	break

"""

	