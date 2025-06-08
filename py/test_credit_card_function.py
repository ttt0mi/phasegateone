import credit_card
from credit_card import *
import unittest
from unittest import TestCase


class TestCardValidationFunction(TestCase):

	def test_credit_card_existence(self):
		cardno = "5399831619690403"
		validity = {}
		checker = credit_card_validator(cardno)
		cardIssuer(validity, cardno, checker)


	def test_credit_card_visa_actions(self):
		cardno = "4003600000000014"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'Visa', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'valid'}

		self.assertEqual(actual, expected)

		cardno = "4003600000000015"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'Visa', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'invalid'}

		self.assertEqual(actual, expected)




	def test_credit_card_mastercard_actions(self):
		cardno = "5399831619690403"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'MasterCard', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'valid'}

		self.assertEqual(actual, expected)


		cardno = "5399831619690404"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'MasterCard', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'invalid'}

		self.assertEqual(actual, expected)





	def test_credit_card_discover_actions(self):
		cardno = "6539983161969047"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'Discover', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'valid'}

		self.assertEqual(actual, expected)


		cardno = "6539983161969048"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'Discover', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'invalid'}

		self.assertEqual(actual, expected)






	def test_credit_card_AE_actions(self):
		cardno = "3753998316196904"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'American Express', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'valid'}

		self.assertEqual(actual, expected)

		
		cardno = "3753998316196905"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'American Express', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'invalid'}

		self.assertEqual(actual, expected)






	def test_credit_card_invalid_card(self):
		cardno = "5399831619690403"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'MasterCard', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'valid'}

		self.assertEqual(actual, expected)




	def test_credit_card_invalid_card_issuer(self):
		cardno = "2399831619690403"
		validity = {}
		checker = credit_card_validator(cardno)
	
		actual = cardIssuer(validity, cardno, checker)
		expected = {'Credit Card Type': 'Invalid Card', 'Credit Card Number': cardno, 'Credit Card Length': len(cardno), 'Credit Card Status': 'invalid'}

		self.assertEqual(actual, expected)

