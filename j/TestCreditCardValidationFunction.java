import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class TestCreditCardValidationFunction{

	@Test
	public void testFunctionExistence(){
		String cardno = "5399831619690403";
		CreditCardValidation.validation(cardno);
	}

	@Test
	public void testValidCard(){
		String cardno = "5399831619690403";
		assertTrue(CreditCardValidation.validation(cardno));
	}
	
	@Test
	public void testInvalidCard(){
		String cardno = "9399831619690404";
		assertFalse(CreditCardValidation.validation(cardno));

		cardno = "5399831619690404";
		assertFalse(CreditCardValidation.validation(cardno));
	}



	@Test
	public void testValidVisa(){
		String cardno = "4003600000000014";

		assertTrue(CreditCardValidation.validation(cardno));

		String actual = CreditCardValidation.cardIssuer(cardno);
		String expected = "Visa";
		assertEquals(expected, actual);
	}

	@Test
	public void testInvalidVisa(){

		String cardno = "4003600000000015";
		assertFalse(CreditCardValidation.validation(cardno));
	}



	@Test
	public void testValidMastercard(){
		String cardno = "5399831619690403";
		
		assertTrue(CreditCardValidation.validation(cardno));

		String actual = CreditCardValidation.cardIssuer(cardno);
		String expected = "MasterCard";
		assertEquals(expected, actual);
	}

	@Test
	public void testInvalidMastercard(){

		String cardno = "5399831619690404";
		assertFalse(CreditCardValidation.validation(cardno));
	}



	@Test
	public void testValidDiscover(){
		String cardno = "6539983161969047";
		
		assertTrue(CreditCardValidation.validation(cardno));

		String actual = CreditCardValidation.cardIssuer(cardno);
		String expected = "Discover";
		assertEquals(expected, actual);
	}

	@Test
	public void testInvalidDiscover(){

		String cardno = "6539983161969048";
		assertFalse(CreditCardValidation.validation(cardno));
	}



	@Test
	public void testValidAE(){
		String cardno = "3753998316196904";
		
		assertTrue(CreditCardValidation.validation(cardno));

		String actual = CreditCardValidation.cardIssuer(cardno);
		String expected = "American Express";
		assertEquals(expected, actual);
	}

	@Test
	public void testInvalidAE(){

		String cardno = "3753998316196905";
		assertFalse(CreditCardValidation.validation(cardno));
	}



	@Test
	public void testInvalidCardIssuer(){
		String cardno = "2399831619690403";
		
		assertFalse(CreditCardValidation.validation(cardno));

		String actual = CreditCardValidation.cardIssuer(cardno);
		String expected = "Invalid Card Issuer";
		assertEquals(expected, actual);
	}

	@Test
	public void testInvalidCardLength(){
		String cardno = "831619690403";

		String actual = CreditCardValidation.cardIssuer(cardno);
		String expected = "Invalid Card Length";
		assertEquals(expected, actual);
	}



}