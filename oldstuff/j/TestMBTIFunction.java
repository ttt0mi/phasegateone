import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class TestMBTIFunction{

	String[][] questions = MBTI.testQuestions();
	String[] energyStyleAnswers = new String[5]; 
	String[] cognitiveStyleAnswers = new String[5]; 
	String[] valuesStyleAnswers = new String[5]; 
	String[] lifeStyleAnswers = new String[5]; 
	int[] counters = {0, 0, 0, 0, 0, 0, 0, 0};	

	@Test
	public void testMBTIEnergyStyleQuestions(){

		for(int selection = 1; selection < 6; selection++){
			String EI = MBTI.energyStyleQuestions(questions, energyStyleAnswers, selection);
			counters[EI.equals("A") ? 0 : 1]++;
		}

		String actual =  counters[0] > counters[1] ? "E" : "I";
		String expected = "E";
		assertEquals(expected, actual, "answer A for all questions");
	}



	@Test
	public void testMBTICognitiveStyleQuestions(){

		for(int selection = 1; selection < 6; selection++){
			String SN = MBTI.cognitiveStyleQuestions(questions, cognitiveStyleAnswers, selection);
			counters[SN.equals("A") ? 2 : 3]++;
		}

		String actual =  counters[2] > counters[3] ? "S" : "N";
		String expected = "S";
		assertEquals(expected, actual, "answer A for all questions");
	}



	@Test
	public void testMBTIValuesStyleQuestions(){

		for(int selection = 1; selection < 6; selection++){
			String TF = MBTI.valuesStyleQuestions(questions, valuesStyleAnswers, selection);
			counters[TF.equals("A") ? 4 : 5]++;
		}

		String actual =  counters[4] > counters[5] ? "T" : "F";
		String expected = "T";
		assertEquals(expected, actual, "answer A for all questions");
	}



	@Test
	public void testMBTILifeStyleQuestions(){

		for(int selection = 1; selection < 6; selection++){
			String JP = MBTI.lifeStyleQuestions(questions, lifeStyleAnswers, selection);
			counters[JP.equals("A") ? 6 : 7]++;
		}

		String actual =  counters[6] > counters[7] ? "J" : "P";
		String expected = "J";
		assertEquals(expected, actual, "answer A for all questions");
	}



	@Test
	public void testPersonalityTypeINFP(){
		String energy = "I";
		String cognitive = "N";
		String value = "F";
		String life = "P";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: INFP
				known as The Healer,
				The Thoughtful Idealist (MBTI),
				The Mediator (16Personalities), etc
	
				read more about your personality here:
				www.truity.com/blog/personality-type/infp
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeINTJ(){
		String energy = "I";
		String cognitive = "N";
		String value = "T";
		String life = "J";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: INTJ

				known as The Mastermind,
				The Conceptual Planner (MBTI)
				The Architect (16Personalities), etc
	
				read more about your personality here:
				www.truity.com/blog/personality-type/intj
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeINFJ(){
		String energy = "I";
		String cognitive = "N";
		String value = "F";
		String life = "J";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: INFJ

				known as The Counsellor,
				The Insightful Visionary (MBTI)
				The Advocate (16Personalities), etc
	
				read more about your personality here:
				www.truity.com/blog/personality-type/infj
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeINTP(){
		String energy = "I";
		String cognitive = "N";
		String value = "T";
		String life = "P";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected ="""
				your personality type: INTP

				known as The Architect,
				The Objective Analyst (MBTI)
				The Logician (16Personalities)
	
				read more about your personality here:
				www.truity.com/blog/personality-type/intp
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeENFP(){
		String energy = "E";
		String cognitive = "N";
		String value = "F";
		String life = "P";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected =  """
				your personality type: ENFP

				known as The Champion,
				The Imaginative Motivator (MBTI)
				The Campaigner (16Personalities)
	
				read more about your personality here:
				www.truity.com/blog/personality-type/enfp
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeENTJ(){
		String energy = "E";
		String cognitive = "N";
		String value = "T";
		String life = "J";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: ENTJ

				known as The Commander
	
				read more about your personality here:
				www.truity.com/blog/personality-type/entj
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeENTP(){
		String energy = "E";
		String cognitive = "N";
		String value = "T";
		String life = "P";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: ENTP

				known as The Visionary
	
				read more about your personality here:
				www.truity.com/blog/personality-type/entp
					""";

		assertEquals(actual, expected);
	}




	@Test
	public void testPersonalityTypeENFJ(){
		String energy = "E";
		String cognitive = "N";
		String value = "F";
		String life = "J";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: ENFJ

				known as The Teacher
	
				read more about your personality here:
				www.truity.com/blog/personality-type/enfj
					""";

		assertEquals(actual, expected);
	}




	@Test
	public void testPersonalityTypeISFJ(){
		String energy = "I";
		String cognitive = "S";
		String value = "F";
		String life = "J";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: ISFJ

				known as The Protector
	
				read more about your personality here:
				www.truity.com/blog/personality-type/isfj
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeISFP(){
		String energy = "I";
		String cognitive = "S";
		String value = "F";
		String life = "P";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: ISFP

				known as The Composer
	
				read more about your personality here:
				www.truity.com/blog/personality-type/isfp
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeISTJ(){
		String energy = "I";
		String cognitive = "S";
		String value = "T";
		String life = "J";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: ISTJ

				known as The Inspector
	
				read more about your personality here:
				www.truity.com/blog/personality-type/istj
					""";

		assertEquals(actual, expected);
	}




	@Test
	public void testPersonalityTypeISTP(){
		String energy = "I";
		String cognitive = "S";
		String value = "T";
		String life = "P";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected =  """
				your personality type: ISTP

				known as The Craftsperson
	
				read more about your personality here:
				www.truity.com/blog/personality-type/istp
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeESFJ(){
		String energy = "E";
		String cognitive = "S";
		String value = "F";
		String life = "J";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: ESFJ

				known as The Provider
	
				read more about your personality here:
				www.truity.com/blog/personality-type/esfj
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeESFP(){
		String energy = "E";
		String cognitive = "S";
		String value = "F";
		String life = "P";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected =  """
				your personality type: ESFP

				known as The Performer
	
				read more about your personality here:
				www.truity.com/blog/personality-type/esfp
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeESTJ(){
		String energy = "E";
		String cognitive = "S";
		String value = "T";
		String life = "J";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected =  """
				your personality type: ESTJ

				known as The Supervisor
	
				read more about your personality here:
				www.truity.com/blog/personality-type/estj
					""";

		assertEquals(actual, expected);
	}



	@Test
	public void testPersonalityTypeESTP(){
		String energy = "E";
		String cognitive = "S";
		String value = "T";
		String life = "P";

		String actual = MBTI.type(energy, cognitive, value, life);
		String expected = """
				your personality type: ESTP

				known as The Dynamo
	
				read more about your personality here:
				www.truity.com/blog/personality-type/estp
					""";

		assertEquals(actual, expected);
	}

}


