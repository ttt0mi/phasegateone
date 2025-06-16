import datetime


def name_check(name):

	if not name or name.isspace():
		return "Name cannot be empty"

	if name.startswith(" ") or name.endswith(" "):
		return "Invalid space present"

	new_name = name.replace("-", "").replace(" ", "")

	if len(new_name) < 2 or len(new_name) > 30:
		return "Character limit error"

	if any(char == " " for char in name[:2]):
		return "Invalid name"

	if new_name.isalpha():
		return True
	else:
		return "Invalid name"



def item_check(item):

	if not item or item.isspace():
		return "Space cannot be empty"

	if item.startswith(" ") or item.endswith(" "):
		return "Invalid space present"

	temp = item.replace(" ","")

	if len(temp) < 2 or len(temp) > 30:
		return "Character limit error"

	if any(char == " " for char in item[:2]):
		return "Invalid item"

	if temp.isalnum():
		return True
	else:
		return "Invalid character"





def customer_details(catalogue):

	while True:
		item = str(input("What did the user buy? "))
		if item_check(item) != True:
			print(item_check(item))
			continue
		break

	while True:
		try:
			units = int(input("how many units were purchased? "))
			if units < 1: raise ValueError("units purchased must be positive")

			price = float(input("how much per unit: "))
			if price < 1: raise ValueError("price must be positive")
			if price != round(price, 2): raise ValueError("invalid price")


		except ValueError as e:
			print(e)
			continue


		total = round(units * price, 2)

		catalogue.append([item, units, price, total])
		break


def cashier_details():
	
	while True:
		cash_name = str(input("What is your name: "))
		if name_check(cash_name) != True:
			print(name_check(cash_name))
			continue
		break

	while True:
		try:
			discount = float(input("what percentage discount is being offered? "))

			if discount < 0 or discount > 100: raise ValueError("invalid discount")

		except ValueError as e:
			print(e)
			continue

		return (cash_name, discount)
		


def customer_payment(cost):
	while True:
		try:
			payment = float(input("Your Payment: "))
		
			if payment < 0: raise ValueError("payment cannot be negative")
			if payment < cost: raise ValueError("This will not cover the bill")

		except ValueError as e:
			print(e)
			continue

		return payment




def product_list(catalogue):

	item_width = max(len(purchase[0]) for purchase in catalogue)
	unit_width = max(len(str(purchase[1])) for purchase in catalogue)
	price_width = max(len(str(purchase[2])) for purchase in catalogue)
	total_width = max(len(str(purchase[3])) for purchase in catalogue)

	for purchase in catalogue:
		print(f"\t\t{purchase[0]:>{item_width}}\t{purchase[1]:>{unit_width}}\t{purchase[2]:>{price_width}.2f}\t\t{purchase[3]:>{total_width}.2f}\n")




def invoice(catalogue, customer_name, cashier_info):

	cashier_name, discount = cashier_info

	today = datetime.datetime.now()
	date = today.strftime("%d-%b-%y %-I:%M:%S%p")

	bill = 0
	for purchase in catalogue:
		bill += purchase[3]

	bill_discount = round(bill * (discount / 100), 2)
	VAT_discount = round(bill * 0.175, 2)
	new_bill = round(bill - (bill_discount + VAT_discount), 2)

	

	print(f"""

	Al-Qaeda Auctions
	MAIN BRANCH
	LOCATION: secret
	TEL: those who need to know, know
	Date: {date}
	Cashier: {cashier_name}
	Customer's Name: {customer_name}

	=======================================================
		ITEM	QTY	PRICE(£)	TOTAL(£)
	-------------------------------------------------------
	""")

	product_list(catalogue)

	print(f"""
	-------------------------------------------------------
				Sub Total:	{bill:>7.2f}
				Discount:	{bill_discount:>7.2f}
				VAT @17.5%:	{VAT_discount:>7.2f}
	=======================================================
				Bill Total:	{new_bill:>7.2f}
	=======================================================
		THIS IS NOT A RECEIPT KINDLY PAY {new_bill:.2f}
	=======================================================

	""")

	return new_bill




def receipt(catalogue, customer_name, cashier_info, payment):

	cashier_name, discount = cashier_info

	today = datetime.datetime.now()
	date = today.strftime("%d-%b-%y %-I:%M:%S%p")

	bill = 0
	for purchase in catalogue:
		bill += purchase[3]

	bill_discount = round(bill * (discount / 100), 2)
	VAT_discount = round(bill * 0.175, 2)
	new_bill = round(bill - (bill_discount + VAT_discount), 2)
	balance = round(payment - new_bill, 2)


	print(f"""

	Al-Qaeda Auctions
	MAIN BRANCH
	LOCATION: secret
	TEL: those who need to know, know
	Date: {date}
	Cashier: {cashier_name}
	Customer's Name: {customer_name}

	=======================================================

		ITEM	QTY	PRICE(£)	TOTAL(£)
	--------------------------------------------------------
	""")
	
	product_list(catalogue)
	print(f"""
	--------------------------------------------------------
				Sub Total:	{bill:>7.2f}
				Discount:	{bill_discount:>7.2f}
				VAT @17.5%:	{VAT_discount:>7.2f}
	=======================================================
				Bill Total:	{new_bill:>7.2f}
				Payment:	{payment:>7.2f}
				Balance:	{balance:>7.2f}
	=======================================================
				HAPPY BOMBING
	=======================================================

	""")

	return balance





catalogue = []
proceed = True

while True:
	customer_name = str(input("What is the customer's name: "))

	if name_check(customer_name) != True:
		print(name_check(customer_name))
		continue

	while proceed:
		customer_details(catalogue)

		while proceed:
			choice = str(input("Enter yes to add more items, no to get invoice: "))
			choice = choice.upper()

			match choice:
				case "YES":
					break

				case "NO":
					proceed = False
					break

				case _:
					print("invalid choice, try again")
					continue 


	cashier_info = cashier_details()

	cost = invoice(catalogue, customer_name, cashier_info)
	
	payment = customer_payment(cost)

	receipt(catalogue, customer_name, cashier_info, payment)
	break




#fix alignment issues for all variables in invoice & receipt functions
#round all values to 2 d.p in invoice & receipt functions



