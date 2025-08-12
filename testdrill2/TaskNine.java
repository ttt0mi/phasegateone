import java.util.Scanner;

public class TaskNine{
	public static void main(String... args){
		Scanner scan = new Scanner(System.in);

		double sum = 0;
		for(int input = 0; input < 10; input++){
			System.out.print("enter a score: ");
			double score = scan.nextDouble();
			if(score > -1 && score < 101) sum += score;
		}

		System.out.printf("sum of valid scores is %.2f", sum);
	}
}