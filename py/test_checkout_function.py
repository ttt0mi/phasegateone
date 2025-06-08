import checkout
from checkout import *
import unittest
from unittest import TestCase


class TestCheckoutFunction(TestCase):

	def test_checkout_existence(self):
		customer_name = "tom"
		item = "candy"
		unit = 2
		price = 50
		total = 100
		catalogue = [[item, unit, price, total]]
		cashier_name = "fred"
		discount = 10
		cashier_info = (cashier_name, discount)

		invoice(catalogue, customer_name, cashier_info)


	def test_checkout_name_check(self):
		name = "tom"
		self.assertTrue(name_check(name))
		self.assertEqual(name_check("tom£9"), "Invalid name")
		self.assertEqual(name_check(" tom39"), "Invalid space present")
		self.assertEqual(name_check(""), "Name cannot be empty")
		self.assertEqual(name_check("   "), "Name cannot be empty")
		self.assertEqual(name_check("t omide"), "Invalid name")
		self.assertEqual(name_check("t"), "Character limit error")
		self.assertEqual(name_check("oluwatimilehin ifeoluwa tobiloba ebunoulwajesu"), "Character limit error")


	def test_checkout_item_check(self):
		item = "hydrogen bomb"
		self.assertTrue(item_check(item))
		self.assertEqual(item_check("gren@d£$"), "Invalid character")
		self.assertEqual(item_check(" grenade"), "Invalid space present")
		self.assertEqual(item_check(""), "Space cannot be empty")
		self.assertEqual(item_check("   "), "Space cannot be empty")
		self.assertEqual(item_check("g un"), "Invalid item")
		self.assertEqual(item_check("g"), "Character limit error")
		self.assertEqual(item_check("The greatest bomb ever constructed by man which uses hydrogen atoms"), "Character limit error")


	def test_checkout_invoice(self):
		customer_name = "tom"
		item = "candy"
		unit = 2
		price = 50
		total = 100
		catalogue = [[item, unit, price, total]]
		cashier_name = "fred"
		discount = 10
		cashier_info = (cashier_name, discount)

		actual = invoice(catalogue, customer_name, cashier_info)
		expected = 72.5
		self.assertEqual(actual, expected)


	def test_checkout_receipt(self):
		customer_name = "tom"
		item = "candy"
		unit = 2
		price = 50
		total = 100
		catalogue = [[item, unit, price, total]]
		cashier_name = "fred"
		discount = 10
		cashier_info = (cashier_name, discount)

		payment = 100
		bill = invoice(catalogue, customer_name, cashier_info)

		actual = receipt(catalogue, customer_name, cashier_info, payment)
		expected = payment - bill
		self.assertEqual(actual, expected)




	def test_checkout_cashier_details(self):

		name, discount = cashier_details()

		actual = name, discount
		expected = (name, discount)
		self.assertEqual(actual, expected)


	def test_checkout_customer_payment(self):
		customer_name = "tom"
		item = "candy"
		unit = 2
		price = 50
		total = 100
		catalogue = [[item, unit, price, total]]
		cashier_name = "fred"
		discount = 10
		cashier_info = (cashier_name, discount)

		bill = invoice(catalogue, customer_name, cashier_info)

		actual = customer_payment(bill)
		expected = 100
		self.assertEqual(actual, expected)





