

def phone_check(contacts, phone_number):

	if not phone_number or phone_number.isspace(): return False
	if not all(digit.isdigit() for digit in phone_number): return False
	if len(phone_number)!= 11: return False
	if not phone_number.startswith(("070", "080", "081", "090")): return False
	return True




def name_check(name):

	invalids = (" ", "-", "'")
	temp = name.replace("-", "").replace(" ", "").replace("'", "")

	if not name or name.isspace(): return False
	if name.startswith(invalids) or name.endswith(invalids): return False
	if len(temp) not in range(1, 41): return False
	if temp.isalnum(): return True
	else: return False




def add(contacts):

	contact = {}
	proceed = True

	while True:
		try:
			f_name = str(input("first name: "))
			if not name_check(f_name):
				raise ValueError("invalid first name")
				continue
			
			l_name = str(input("last name: "))
			if not name_check(l_name):
				raise ValueError("invalid last name")
				continue

			contact['first name'] = f_name
			contact['last name'] = l_name

			address = str(input("address(press enter to skip): "))
			if len(address) != 0: contact['address'] = address

			i = 1
			while proceed:
				phone = str(input("phone number: "))

				if not phone_check(contacts, phone):
					print("invalid nigerian phone number")
					continue

				if any(phone in contacts[i].values() for i in range(len(contacts))):
					print("phone number already exists")
					continue

				contact[f'telephone {i}'] = phone
				i += 1

				while proceed:
					choice = str(input("enter another number(yes/no): ")).lower()

					if choice == "yes": break
					elif choice == "no":
						proceed = False
						break
					else: print("invalid")
						

		except ValueError as e:
			print(f"{e}, try again")


		contacts.append(contact)
		return "contact added"
		



def remove(contacts):

	if len(contacts) == 0: return False

	all_contacts(contacts)
	proceed = True
	index = 0

	while True:
		try:
			choice = int(input("\nenter contact number to delete: "))
			if choice > len(contacts): raise ValueError
			
			index = choice - 1
		except ValueError:
			print("invalid")
			while proceed:
				my_choice = str(input("do you want to try again(yes/no): ")).lower()

				if my_choice == "yes": break
				elif my_choice == "no": return False
				else: print("invalid")
			
			continue	

		contacts.pop(index)
		return True
	




def edit(contacts):

	if len(contacts) == 0: return False

	all_contacts(contacts)
	index = 0

	while True:
		try:
			choice = int(input("\nenter contact number to edit: "))
			if choice > len(contacts): raise ValueError
			
			index = choice - 1
		except ValueError:
			print("invalid")
			while True:
				my_choice = str(input("do you want to try again(yes/no): ")).lower()

				if my_choice == "yes": break
				elif my_choice == "no": return False
				else: print("invalid")
			
			continue
		else: break

	
	proceed = True
	while True:
		try:
			f_name = str(input("edit first name(press enter to leave): "))

			if len(f_name) != 0:
				if not name_check(f_name):
					raise ValueError("invalid first name")
					continue
				contacts[index]['first name'] = f_name


			l_name = str(input("edit last name(press enter to leave): "))

			if len(l_name) != 0:
				if not name_check(l_name):
					raise ValueError("invalid last name")
					continue
				contacts[index]['last name'] = l_name

			address = str(input("edit address(press enter to leave): "))
			if len(address) != 0: contacts[index]['address'] = address

			i = 1
			while proceed:
				phone = str(input("edit phone number(press enter to leave): "))

				if len(phone) != 0:
					if not phone_check(contacts, phone):
						print("invalid nigerian phone number")
						continue

					contacts[index].pop(f'telephone {i}')

					if any(phone in contacts[i].values() for i in range(len(contacts))):
						print("phone number already exists")
						continue

					contacts[index][f'telephone {i}'] = phone
				i += 1

				while proceed:
					choice = str(input("edit another number(yes/no): ")).lower()

					if choice == "yes": break
					elif choice == "no":
						proceed = False
						break
					else: print("invalid")
						

		except ValueError as e:
			print(f"{e}, try again")

		return True





def find_via_fn(contacts):

	if len(contacts) == 0: return False

	while True:
		name = str(input("enter first name to find contact: ")).lower()

		if all(name != contacts[i]['first name'].lower() for i in range(len(contacts))):
			return False

		for idx, contact in enumerate(contacts, 1):
			if name == contact['first name'].lower():
				print(f"\nContact {idx}")
				for iden, info in contact.items(): print(f"{iden}: {info}")

		while True:
			choice = str(input("find another name(yes/no): ")).lower()

			if choice == "yes": break
			elif choice == "no": return True
			else: print("invalid")

					



def find_via_ln(contacts):

	if len(contacts) == 0: return False
	
	while True:
		name = str(input("enter last name to find contact: ")).lower()

		if all(name != contacts[i]['last name'].lower() for i in range(len(contacts))):
			return False

		for idx, contact in enumerate(contacts, 1):
			if name == contact['last name'].lower():
				print(f"\nContact {idx}")
				for iden, info in contact.items(): print(f"{iden}: {info}")

		while True:
			choice = str(input("find another name(yes/no): ")).lower()

			if choice == "yes": break
			elif choice == "no": return True
			else: print("invalid")




def find_via_pn(contacts):
	
	if len(contacts) == 0: return False

	while True:
		phone = str(input("enter phone number to find contact: "))

		if not phone_check(contacts, phone): return False
		elif all(phone not in contacts[i].values() for i in range(len(contacts))):
			return False

		for idx, contact in enumerate(contacts, 1):
			if phone in contact.values():
				print(f"\nContact {idx}")
				for iden, info in contact.items(): print(f"{iden}: {info}")

		while True:
			choice = str(input("find another number(yes/no): ")).lower()

			if choice == "yes": break
			elif choice == "no": return True
			else: print("invalid")
		




def all_contacts(contacts):
	
	for idx, contact in enumerate(contacts, 1):
		print(f"\nContact {idx}")
		for iden, info in contact.items(): print(f"{iden}: {info}")













