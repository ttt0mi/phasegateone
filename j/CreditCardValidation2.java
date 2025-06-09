import java.util.Scanner;

public class CreditCardValidation{

	public static boolean validation(String number){

		int sum = 0;

		for(int index = number.length() - 2; index > -1; index-=2){

			int digit = Character.getNumericValue(number.charAt(index));

			int num = digit * 2;
			if(num > 9) num = (num % 10) + 1;

			sum += num;
		}

		for(int index = number.length() - 1; index > -1; index-=2){

			sum += Character.getNumericValue(number.charAt(index));
		}
		
		if(sum % 10 == 0) return true;
		else return false;
	}


	public static String cardIssuer(String cardNumber, boolean checker){

		if(cardNumber.length() <= 13 || cardNumber.length() > 16) return "Invalid Card Length";

		if(!checker) return "Invalid";

		else if(cardNumber.startsWith("4")) return "Visa";

		else if(cardNumber.startsWith("5")) return "MasterCard";
	
		else if(cardNumber.startsWith("6")) return "Discover";

		else if(cardNumber.startsWith("37")) return "American Express";

		else return "Invalid";

	}

/*
	public static void main(String... args){

		Scanner input = new Scanner(System.in);

		System.out.print("what is your card number? ");
		String cardNumber = input.next();

		boolean checker = validation(cardNumber);
		String issuer = cardIssuer(cardNumber, checker);

		if(issuer.equals("Invalid")) checker = false;
		
		String validCheck = checker ? "valid" : "invalid";

		System.out.println("Credit Card Type: " + issuer);
		System.out.println("Credit Card Number: " + cardNumber);
		System.out.println("Credit Card Digit Length: " + cardNumber.length());
		System.out.println("Credit Card Status: " + validCheck);


	}
*/
}