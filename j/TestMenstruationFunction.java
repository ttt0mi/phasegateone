import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class TestMenstruationFunction{

	String[] months = {"january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"};


	@Test
	public void testFunctionExistence(){
		String month = "may";
		int periodStart = 13;
		int cycle = 28;
		int ovulationDay = periodStart + cycle / 2;
		int daysInMonth = 31;

		Menstruation.getPeriodInfo(month, periodStart, ovulationDay, daysInMonth, months);

	}


	@Test
	public void testGetDaysInMonth(){
		String pMonth = "may";
		int actual = Menstruation.getDaysInMonth(pMonth, months);
		int expected = 31;
		assertEquals(expected, actual);

	}


	@Test
	public void testGetDaysInMonthError(){
		String pMonth = "somethingdumb";
		int actual = Menstruation.getDaysInMonth(pMonth, months);
		int expected = 0;
		assertEquals(expected, actual);

	}

	
	@Test
	public void testGetOvulation(){
		String month = "may";
		int periodStart = 13;
		int cycle = 28;
		int ovulationDay = periodStart + cycle / 2;
		int daysInMonth = 31;

		String actual = Menstruation.getPeriodInfo(month, periodStart, ovulationDay, daysInMonth, months);
		String expected = "27 may";
		assertEquals(expected, actual);

	}


	@Test
	public void testGetFertileWindowStart(){
		String month = "may";
		int periodStart = 13;
		int cycle = 28;
		int fertileWindowStart = (periodStart + cycle / 2) - 5;
		int daysInMonth = 31;

		String actual = Menstruation.getPeriodInfo(month, periodStart, fertileWindowStart, daysInMonth, months);
		String expected = "22 may";
		assertEquals(expected, actual);
	
	}


	@Test
	public void testGetFertileWindowEnd(){
		String month = "may";
		int periodStart = 13;
		int cycle = 28;
		int fertileWindowEnd = (periodStart + cycle / 2) + 1;
		int daysInMonth = 31;

		String actual = Menstruation.getPeriodInfo(month, periodStart, fertileWindowEnd, daysInMonth, months);
		String expected = "28 may";
		assertEquals(expected, actual);

	}


	@Test
	public void testGetNextPeriodStart(){
		String month = "may";
		int periodStart = 13;
		int cycle = 28;
		int nextPeriodStart = periodStart + cycle;
		int daysInMonth = 31;

		String actual = Menstruation.getPeriodInfo(month, periodStart, nextPeriodStart, daysInMonth, months);
		String expected = "10 june";
		assertEquals(expected, actual);
	
	}


	@Test
	public void testGetNextPeriodEnd(){
		String month = "may";
		int periodStart = 13;
		int periodDuration = 4;
		int cycle = 28;
		int nextPeriodEnd = (periodStart + cycle) + periodDuration;
		int daysInMonth = 31;

		String actual = Menstruation.getPeriodInfo(month, periodStart, nextPeriodEnd, daysInMonth, months);
		String expected = "14 june";
		assertEquals(expected, actual);
	
	}









}