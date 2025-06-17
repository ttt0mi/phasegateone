public class taskseven{

	public static void main(String... args){

		for(int digit = 1; digit < 11; digit++){

			if(digit % 4 == 0){

				int multiple = 1, total = 0;
 
				for(int i = 1; i < 6; i++){
					multiple *= digit;
					total += multiple;
				}
				System.out.println(total);

			}
		}
	}
}