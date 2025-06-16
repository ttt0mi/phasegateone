import phonebook
from phonebook import *

import unittest
from unittest import TestCase


class TestPhoneBookFunctionSuccess(TestCase):

	contacts = [
		{"first name" : "mao", "last name" : "mussolini", "telephone 1" : "07061828302"},
		{"first name" : "adolf", "last name" : "nero", "telephone 1" : "09056689421"}
	]

	def test_phonebook_name_check(self):

		self.assertTrue(name_check("tom"))
		self.assertTrue(name_check("mary-anne"))
		self.assertTrue(name_check("tom99"))

		self.assertFalse(name_check("-tom"))
		self.assertFalse(name_check("tom56%4"))
		self.assertFalse(name_check(""))

	def test_phonebook_phone_check(self):
		
		self.assertTrue(phone_check(self.contacts, "09011520288"))
		self.assertTrue(phone_check(self.contacts, "07061828302"))
		self.assertTrue(phone_check(self.contacts, "08127035035"))

		self.assertFalse(phone_check(self.contacts, "     "))
		self.assertFalse(phone_check(self.contacts, "61828302"))
		self.assertFalse(phone_check(self.contacts, "070Z035035"))
		self.assertFalse(phone_check(self.contacts, "06027035035"))
		self.assertFalse(phone_check(self.contacts, "081$0350655"))

	def test_phonebook_a_add_contacts(self):
		self.assertEqual(add(self.contacts), "contact added")	

	def test_phonebook_b_edit_contacts(self):
		self.assertTrue(edit(self.contacts))

	def test_phonebook_c_remove_contacts(self):
		self.assertTrue(remove(self.contacts))

	def test_phonebook_d_find_contact_via_first_name(self):
		self.assertTrue(find_via_fn(self.contacts))

	def test_phonebook_e_find_contact_via_last_name(self):		
		self.assertTrue(find_via_ln(self.contacts))

	def test_phonebook_f_find_contact_via_phone_number(self):		
		self.assertTrue(find_via_pn(self.contacts))

	def test_phonebook_h_edit_contacts_failure(self):
		self.assertFalse(edit(self.contacts))

	def test_phonebook_i_remove_contacts_failure(self):	
		self.assertFalse(remove(self.contacts))

	def test_phonebook_j_find_contact_via_first_name_failure(self):	
		self.assertFalse(find_via_fn(self.contacts))

	def test_phonebook_k_find_contact_via_last_name_failure(self):		
		self.assertFalse(find_via_ln(self.contacts))

	def test_phonebook_l_find_contact_via_phone_number_failure(self):		
		self.assertFalse(find_via_pn(self.contacts))















