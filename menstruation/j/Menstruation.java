import java.util.Scanner;

public class Menstruation{

	public static int getDaysInMonth(String month, String[] months){

		for(int index = 0; index < months.length; index++){

			if(month.equalsIgnoreCase(months[index])){
				if(index == 1) return 28;
				else if(index == 3) return 30;
				else if(index == 5) return 30;
				else if(index == 8) return 30;
				else if(index == 10) return 30;
				else return 31;
			}
		}
		return 0;
	}



	public static String getPeriodInfo(String month, int periodStart, int days, int daysInMonth, String[] months){

		if(days < daysInMonth) return String.format("%d %s", days, month);

		else{
			days = (days - 1) % daysInMonth + 1;

			for(int index = 0; index < months.length; index++){

				if(month.equalsIgnoreCase(months[index])){

					if(index == 11) return String.format("%d %s", days, months[0]);
					else return String.format("%d %s", days, months[index + 1]);
				}
			}
			return "something went wrong";		
		}
	}

/*

	public static void main(String... args){
		Scanner input = new Scanner(System.in);

		String[] months = {"january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"};


		while(true){
			System.out.print("what month did your last period occur? ");
			String pMonth = input.next();

			int dayInaMonth = getDaysInMonth(pMonth, months);

			if(dayInaMonth == 0){
				System.out.println("Invalid month");
				continue;
			}


			System.out.print("what day did it start?(in days): ");
			int pDay = input.nextInt();

			if(pDay < 1 || pDay > dayInaMonth ){
				System.out.println("Invalid day");
				continue;
			}


			System.out.print("On average, How long does it last(in days): ");
			int pDuration = input.nextInt();

			if(pDuration < 1){
				System.out.println("Invalid days length");
				continue;
			}

			if(pDuration < 3 || pDuration > 7) System.out.println("Abnormal period, Please consult your doctor");

			System.out.print("On average, how long is your menstrual cycle(in days): ");
			int cycle = input.nextInt();

			if(cycle < 1){
				System.out.println("Invalid cycle length");
				continue;
			}

			if(pDuration < 21 || pDuration > 35) System.out.println("Abnormal cycle length, Please consult your doctor");


			int ovulationDay = pDay + cycle / 2;
			int fertileWindow = ovulationDay - 5;
			int fertileWindowEnd = fertileWindow + 6;
			int nextPeriod = pDay + cycle;
			int nextPeriodEnd = nextPeriod + pDuration;
	
			String day1 = getPeriodInfo(pMonth, pDay, ovulationDay, dayInaMonth, months);
			String day2 = getPeriodInfo(pMonth, pDay, fertileWindow, dayInaMonth, months);
			String day3 = getPeriodInfo(pMonth, pDay, fertileWindowEnd, dayInaMonth, months);
			String day4 = getPeriodInfo(pMonth, pDay, nextPeriod, dayInaMonth, months);
			String day5 = getPeriodInfo(pMonth, pDay, nextPeriodEnd, dayInaMonth, months);

			System.out.printf("we predict your ovulation day will be on %s\n", day1);
			System.out.printf("we predict your fertility window is between %s to %s\n", day2, day3);
			System.out.printf("we predict your next period will be between %s to %s\n", day4, day5);
			break;

		
		}

	}


*/
}






