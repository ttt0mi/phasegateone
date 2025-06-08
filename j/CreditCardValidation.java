import java.util.Scanner;

public class CreditCardValidation.java{

	public static boolean validation(String number){

		int sum = 0;

		for(int index = number.length - 2; index > -1; index-=2){

			int digit = Character.getNumericValue(number.charAt(index));

			int num = digit * 2;
			if(num > 9) num = (num % 10) + 1;

			sum += num;
		
		}


		for(int index = number.length - 1; index > -1; index-=2){

			int digit = Character.getNumericValue(number.charAt(index));
			sum += digit;
		
		}
		
		if(sum % 10 == 0) return true
		else return false
	}


	public static void main(){

		Scanner input = new Scanner(System.in);





	}

}