import java.util.Scanner;

public class TaskEight{
	public static void main(String... args){
		Scanner scan = new Scanner(System.in);

		double sum = 0;
		int validCount = 0;

		while(validCount < 10){
			System.out.print("enter a score: ");
			double score = scan.nextDouble();
			if(score > -1 && score < 101){
				sum += score;
				validCount++;
			}
			else System.out.println("invalid, re-try");
		}

		System.out.printf("sum of valid scores is %.2f", sum);
	}
}