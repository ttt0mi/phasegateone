import java.util.Scanner;

public class TaskFour{
	public static void main(String... args){
		Scanner scan = new Scanner(System.in);

		double sum = 0;
		for(int input = 0; input < 10; input++){
			System.out.print("enter a score: ");
			double score = scan.nextDouble();
			if(input % 2 == 1) sum += score;
		}

		System.out.printf("sum of scores is %.2f", sum);
	}
}