import java.util.Scanner;


public class MBTI{

	public static String[][] testQuestions(){

		String[][] questions = {

			{"expand energy, enjoy groups", "conserve energy, enjoy one-on-ones"},
			{"Interpret literally", "look for meaning and possibilities"},
			{"logical, thinking, questioning", "empathetic, feeling, accommodating"},
			{"organised, orderly", "flexible, adaptable"},
			{"more outgoing, think out loud", "more reserved, think to yourself"},
			{"practical, realistic, experiential", "imaginative, innovative, theoretical"},
			{"candid, straight forward, frank", "tactful, kind, encouraging"},
			{"plan, schedule", "unplanned, spontaneous"},
			{"seek many tasks, public activities, interaction with others", "seek private, solitary activities with quiet to concentrate"},
			{"standard, usual, conventional", "different, novel, unique"},
			{"firm, tend to criticise, hold the line", "gentle, tend to appreciate, conciliate"},
			{"regulated, structured", "easy-going, live and let live"},
			{"external, communicative, express yourself", "internal, reticent, keep to yourself"},
			{"focus on here-and-now", "look to the future, global perspective, big picture"},
			{"tough-minded, just", "tender-hearted, merciful"},
			{"preparation, plan ahead", "go with the flow, adapt as you go"},
			{"active, initiate", "reflective, deliberate"},
			{"facts, things, what is", "ideas, dreams, what could be, philosophical"},
			{"matter of fact, issue-oriented", "sensitive, people-oriented, compassionate"},
			{"control, govern", "latitude, freedom"}
		};

	return questions;

	}



	public static String energyStyleQuestions(String[][] questions, String[] energyStyleAnswers, int selection){

		Scanner input = new Scanner(System.in);

		String choice = "";

		switch(selection){
			case 1:{
				while(true){
					System.out.printf("%nA. %s%n", questions[0][0]);;
					System.out.printf("B. %s%n", questions[0][1]);;

		
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				energyStyleAnswers[0] = "%s. %s".formatted(choice, questions[0][choice.equals("A") ? 0 : 1]);
				return choice;

			}
	
			case 2:{
				while(true){
					System.out.printf("%nA. %s%n", questions[4][0]);
					System.out.printf("B. %s%n", questions[4][1]);
				
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				energyStyleAnswers[1] = "%s. %s".formatted(choice, questions[4][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 3:{
				while(true){
					System.out.printf("%nA. %s%n", questions[8][0]);
					System.out.printf("B. %s%n", questions[8][1]);
				
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				energyStyleAnswers[2] = "%s. %s".formatted(choice, questions[8][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 4:{
				while(true){
					System.out.printf("%nA. %s%n", questions[12][0]);
					System.out.printf("B. %s%n", questions[12][1]);

					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				energyStyleAnswers[3] = "%s. %s".formatted(choice, questions[12][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 5:{
				while(true){
					System.out.printf("%nA. %s%n", questions[16][0]);;
					System.out.printf("B. %s%n", questions[16][1]);;

					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				energyStyleAnswers[4] = "%s. %s".formatted(choice, questions[16][choice.equals("A") ? 0 : 1]);
				return choice;

			}
			default: return choice;

		}
	}



	public static String cognitiveStyleQuestions(String[][] questions, String[] cognitiveStyleAnswers, int selection){

		Scanner input = new Scanner(System.in);

		String choice = "";

		switch(selection){
			case 1:{
				while(true){
					System.out.printf("%nA. %s%n", questions[1][0]);;
					System.out.printf("B. %s%n", questions[1][1]);;

		
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				cognitiveStyleAnswers[0] = "%s. %s".formatted(choice, questions[1][choice.equals("A") ? 0 : 1]);
				return choice;

			}
	
			case 2:{
				while(true){
					System.out.printf("%nA. %s%n", questions[5][0]);
					System.out.printf("B. %s%n", questions[5][1]);
				
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				cognitiveStyleAnswers[1] = "%s. %s".formatted(choice, questions[5][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 3:{
				while(true){
					System.out.printf("%nA. %s%n", questions[9][0]);
					System.out.printf("B. %s%n", questions[9][1]);
				
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				cognitiveStyleAnswers[2] = "%s. %s".formatted(choice, questions[9][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 4:{
				while(true){
					System.out.printf("%nA. %s%n", questions[13][0]);
					System.out.printf("B. %s%n", questions[13][1]);

					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				cognitiveStyleAnswers[3] = "%s. %s".formatted(choice, questions[13][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 5:{
				while(true){
					System.out.printf("%nA. %s%n", questions[17][0]);;
					System.out.printf("B. %s%n", questions[17][1]);;

					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				cognitiveStyleAnswers[4] = "%s. %s".formatted(choice, questions[17][choice.equals("A") ? 0 : 1]);
				return choice;

			}	
			default: return choice;

		}
	}



	public static String valuesStyleQuestions(String[][] questions, String[] valuesStyleAnswers, int selection){

		Scanner input = new Scanner(System.in);

		String choice = "";

		switch(selection){
			case 1:{
				while(true){
					System.out.printf("%nA. %s%n", questions[2][0]);;
					System.out.printf("B. %s%n", questions[2][1]);;

		
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				valuesStyleAnswers[0] = "%s. %s".formatted(choice, questions[2][choice.equals("A") ? 0 : 1]);
				return choice;

			}
	
			case 2:{
				while(true){
					System.out.printf("%nA. %s%n", questions[6][0]);
					System.out.printf("B. %s%n", questions[6][1]);
				
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				valuesStyleAnswers[1] = "%s. %s".formatted(choice, questions[6][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 3:{
				while(true){
					System.out.printf("%nA. %s%n", questions[10][0]);
					System.out.printf("B. %s%n", questions[10][1]);
				
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				valuesStyleAnswers[2] = "%s. %s".formatted(choice, questions[10][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 4:{
				while(true){
					System.out.printf("%nA. %s%n", questions[14][0]);
					System.out.printf("B. %s%n", questions[14][1]);

					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				valuesStyleAnswers[3] = "%s. %s".formatted(choice, questions[14][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 5:{
				while(true){
					System.out.printf("%nA. %s%n", questions[18][0]);;
					System.out.printf("B. %s%n", questions[18][1]);;

					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				valuesStyleAnswers[4] = "%s. %s".formatted(choice, questions[18][choice.equals("A") ? 0 : 1]);
				return choice;

			}	
			default: return choice;

		}
	}




	public static String lifeStyleQuestions(String[][] questions, String[] lifeStyleAnswers, int selection){

		Scanner input = new Scanner(System.in);

		String choice = "";

		switch(selection){
			case 1:{
				while(true){
					System.out.printf("%nA. %s%n", questions[3][0]);
					System.out.printf("B. %s%n", questions[3][1]);

		
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				lifeStyleAnswers[0] = "%s. %s".formatted(choice, questions[3][choice.equals("A") ? 0 : 1]);
				return choice;

			}
	
			case 2:{
				while(true){
					System.out.printf("%nA. %s%n", questions[7][0]);
					System.out.printf("B. %s%n", questions[7][1]);
				
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				lifeStyleAnswers[1] = "%s. %s".formatted(choice, questions[7][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 3:{
				while(true){
					System.out.printf("%nA. %s%n", questions[11][0]);
					System.out.printf("B. %s%n", questions[11][1]);
				
					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				lifeStyleAnswers[2] = "%s. %s".formatted(choice, questions[11][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 4:{
				while(true){
					System.out.printf("%nA. %s%n", questions[15][0]);
					System.out.printf("B. %s%n", questions[15][1]);

					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				lifeStyleAnswers[3] = "%s. %s".formatted(choice, questions[15][choice.equals("A") ? 0 : 1]);
				return choice;

			}

			case 5:{
				while(true){
					System.out.printf("%nA. %s%n", questions[19][0]);
					System.out.printf("B. %s%n", questions[19][1]);

					System.out.print("A or B: ");
					choice = input.nextLine().toUpperCase();

					switch(choice){
						case "A", "B": break;
						default:{
							System.out.println("invalid choice");
							continue;
						}
					}break;
				}
				lifeStyleAnswers[4] = "%s. %s".formatted(choice, questions[19][choice.equals("A") ? 0 : 1]);
				return choice;

			}
			default: return choice;
		}
	}




	public static String type(String energy, String cognitive, String value, String life){

		String personality = energy + cognitive + value + life;

		switch(personality){

			case "INFP":{
				String pType = """
				your personality type: INFP
				known as The Healer,
				The Thoughtful Idealist (MBTI),
				The Mediator (16Personalities), etc
	
				read more about your personality here:
				www.truity.com/blog/personality-type/infp
					""";

				return pType;
			}


			case "INTJ":{
				String pType = """
				your personality type: INTJ

				known as The Mastermind,
				The Conceptual Planner (MBTI)
				The Architect (16Personalities), etc
	
				read more about your personality here:
				www.truity.com/blog/personality-type/intj
					""";
				return pType;
			}


			case "INFJ":{
				String pType = """
				your personality type: INFJ

				known as The Counsellor,
				The Insightful Visionary (MBTI)
				The Advocate (16Personalities), etc
	
				read more about your personality here:
				www.truity.com/blog/personality-type/infj
					""";
				return pType;
			}


			case "INTP":{
				String pType = """
				your personality type: INTP

				known as The Architect,
				The Objective Analyst (MBTI)
				The Logician (16Personalities)
	
				read more about your personality here:
				www.truity.com/blog/personality-type/intp
					""";
				return pType;
			}


			case "ENFP":{
				String pType = """
				your personality type: ENFP

				known as The Champion,
				The Imaginative Motivator (MBTI)
				The Campaigner (16Personalities)
	
				read more about your personality here:
				www.truity.com/blog/personality-type/enfp
					""";
				return pType;
			}


			case "ENTJ":{
				String pType = """
				your personality type: ENTJ

				known as The Commander
	
				read more about your personality here:
				www.truity.com/blog/personality-type/entj
					""";
				return pType;
			}


			case "ENTP":{
				String pType = """
				your personality type: ENTP

				known as The Visionary
	
				read more about your personality here:
				www.truity.com/blog/personality-type/entp
					""";
				return pType;
			}


			case "ENFJ":{
				String pType = """
				your personality type: ENFJ

				known as The Teacher
	
				read more about your personality here:
				www.truity.com/blog/personality-type/enfj
					""";
				return pType;
			}


			case "ISFJ":{
				String pType = """
				your personality type: ISFJ

				known as The Protector
	
				read more about your personality here:
				www.truity.com/blog/personality-type/isfj
					""";
				return pType;
			}


			case "ISFP":{
				String pType = """
				your personality type: ISFP

				known as The Composer
	
				read more about your personality here:
				www.truity.com/blog/personality-type/isfp
					""";
				return pType;
			}


			case "ISTJ":{
				String pType = """
				your personality type: ISTJ

				known as The Inspector
	
				read more about your personality here:
				www.truity.com/blog/personality-type/istj
					""";
				return pType;
			}


			case "ISTP":{
				String pType = """
				your personality type: ISTP

				known as The Craftsperson
	
				read more about your personality here:
				www.truity.com/blog/personality-type/istp
					""";
				return pType;
			}


			case "ESFJ":{
				String pType = """
				your personality type: ESFJ

				known as The Provider
	
				read more about your personality here:
				www.truity.com/blog/personality-type/esfj
					""";
				return pType;
			}


			case "ESFP":{
				String pType = """
				your personality type: ESFP

				known as The Performer
	
				read more about your personality here:
				www.truity.com/blog/personality-type/esfp
					""";
				return pType;
			}


			case "ESTJ":{
				String pType = """
				your personality type: ESTJ

				known as The Supervisor
	
				read more about your personality here:
				www.truity.com/blog/personality-type/estj
					""";
				return pType;
			}


			case "ESTP":{
				String pType = """
				your personality type: ESTP

				known as The Dynamo
	
				read more about your personality here:
				www.truity.com/blog/personality-type/estp
					""";
				return pType;
			}

			default: return "unknown error";

		}

	}




/*
	public static void main(String... args){
		Scanner input = new Scanner(System.in);

		String[][] questions = testQuestions();
		String[] energyStyleAnswers = new String[5]; 
		String[] cognitiveStyleAnswers = new String[5]; 
		String[] valuesStyleAnswers = new String[5]; 
		String[] lifeStyleAnswers = new String[5]; 

		int[] counters = {0, 0, 0, 0, 0, 0, 0, 0};

		System.out.println("Welcome to the terrorism test");
		System.out.print("what is your name? ");
		String name = input.nextLine();


		System.out.println("Choose below what option most describes you.");

		for(int selection = 1; selection < 6; selection++){

			String EI = energyStyleQuestions(questions, energyStyleAnswers, selection);
			counters[EI.equals("A") ? 0 : 1]++;

			String SN = cognitiveStyleQuestions(questions, cognitiveStyleAnswers, selection);
			counters[SN.equals("A") ? 2 : 3]++;

			String TF = valuesStyleQuestions(questions, valuesStyleAnswers, selection);
			counters[TF.equals("A")? 4 : 5]++;

			String JP = lifeStyleQuestions(questions, lifeStyleAnswers, selection);
			counters[JP.equals("A")? 6 : 7]++;

		}


		System.out.printf("%nhello %s. you selected:%n", name);

		for(String item : energyStyleAnswers) System.out.println(item);
		System.out.println("No of As selected: " + counters[0]);
		System.out.println("No of Bs selected: " + counters[1] + "\n");

		for(String item : cognitiveStyleAnswers) System.out.println(item);
		System.out.println("No of As selected: " + counters[2]);
		System.out.println("No of Bs selected: " + counters[3] + "\n");

		for(String item : valuesStyleAnswers) System.out.println(item);
		System.out.println("No of As selected: " + counters[4]);
		System.out.println("No of Bs selected: " + counters[5] + "\n");

		for(String item : lifeStyleAnswers) System.out.println(item);
		System.out.println("No of As selected: " + counters[6]);
		System.out.println("No of Bs selected: " + counters[7] + "\n");


		String energy = counters[0] > counters[1] ? "E" : "I";
		String cognitive = counters[2] > counters[3] ? "S" : "N";
		String value = counters[4] > counters[5] ? "T" : "F";
		String life = counters[6] > counters[7] ? "J" : "P";

		System.out.print(type(energy, cognitive, value, life));

	}
*/
}