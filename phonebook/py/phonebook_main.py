import phonebook
from phonebook import *

contacts = []

while True:
	print("""
phone book for a nigerian

1 >>> add contact
2 >>> remove contact
3 >>> edit contact
4 >>> find contact by first name
5 >>> find contact by last name
6 >>> find contact by phone number
0 >>> Exit
	""")

	try:
		choice = int(input("Choose a number: "))
	except ValueError:
		print("invalid input, try again")
		continue

	match choice:
		case 1: 
			added = add(contacts)
			print(added)

		case 2:
			if len(contacts) == 0: print("no contacts available")
				
			elif remove(contacts): print("contact removed")

		case 3:
			if len(contacts) == 0: print("no contacts available")
				
			elif edit(contacts): print("contact edited")

		case 4:
			if len(contacts) == 0: print("no contacts available")
	
			elif not find_via_fn(contacts): print("first name does not exist")

		case 5:
			if len(contacts) == 0: print("no contacts available")

			elif not find_via_ln(contacts): print("last name does not exist")

		case 6:
			if len(contacts) == 0: print("no contacts available")

			elif not find_via_pn(contacts): print("number does not exist")

		case 0: break

		case _:
			print("option does not exist, try again")
			continue


print("bye")