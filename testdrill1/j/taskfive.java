public class taskfive{

	public static void main(String... args){

		for(int digit = 1; digit < 11; digit++){

			if(digit % 4 == 0){

				for(int i = 0; i < 5; i++) System.out.println(digit);
			}
		}
	}
}