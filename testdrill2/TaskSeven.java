import java.util.Scanner;

public class TaskSeven{
	public static void main(String... args){
		Scanner scan = new Scanner(System.in);

		double evenSum = 0;
		int evenCount = 0;

		for(int input = 0; input < 10; input++){
			System.out.print("enter a score: ");
			double score = scan.nextDouble();
			if(score % 2 == 0){
				evenSum += score;
				evenCount++;
			}
		}

		System.out.printf("sum of even scores is %.2f%n", evenSum);
		System.out.printf("average of even scores is %.2f", evenSum/evenCount);
	}
}