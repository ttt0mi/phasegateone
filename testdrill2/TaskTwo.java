import java.util.Scanner;

public class TaskTwo{
	public static void main(String... args){
		Scanner scan = new Scanner(System.in);

		double sum = 0;
		for(int input = 0; input < 10; input++){
			System.out.print("enter a score: ");
			double score = scan.nextDouble();
			sum += score;
		}

		System.out.printf("average of scores is %.2f", sum/10);
	}
}