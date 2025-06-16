const prompt = require("prompt-sync")();

function monthCheck(month, months){

	if(month in months) return true
	return false

}


function dayCheck(day, month){

	if(isNaN(Number(day))) return false;

	day = Number(day);

	const array31 = {"january" : 0, "march" : 2, "may" : 4, "july" : 6, "august" : 7, "october" : 9, "december" : 11};

	const array30 = {"april" : 3,  "june" : 5, "september" : 8, "november" : 10};

	const array28 = {"february" : 1};

	if(month in array31){
		if(day > 0 && day < 32) return true;
		return false;
	}
	else
	if(month in array30){
		if(day > 0 && day < 31) return true;
		return false;
	}
	else
	if(month in array28){
		if(day > 0 && day < 29) return true;
		return false;
	}
	else return false;

}



function cycleCheck(cycle){

	if(isNaN(Number(cycle))) return false;
	return true;

}



function getOvulation(month, day, duration, cycle){

	const periodStart = new Date(2025, month, day);
	periodStart.setDate(periodStart.getDate() + (cycle/2));
	
	return periodStart;

}



function getFertilityWindow(month, day, duration, cycle){

	const periodStart = new Date(2025, month, day);
	const start = new Date(periodStart.setDate(periodStart.getDate() + ((cycle/2) - 5)));
	const end = new Date (periodStart.setDate(periodStart.getDate() + ((cycle/2) - 8)));
	
	return [start, end];

}



function getNextPeriod(month, day, duration, cycle){

	const periodStart = new Date(2025, month, day);
	periodStart.setDate(periodStart.getDate() + cycle);
	
	return periodStart;

}






const months = {"january" : 0, "february" : 1, "march" : 2, "april" : 3, "may" : 4, "june" : 5, "july" : 6, "august" : 7, "september" : 8, "october" : 9, "november" : 10, "december" : 11};



while(true){

	let pMonth = prompt("what month did your last period occur? ");
	pMonth = pMonth.toLowerCase();

	if(!monthCheck(pMonth, months)){
		console.log("invalid input");
		continue;
	}

	let pDay = prompt("what day did it start?(in digits): ");

	if(!dayCheck(pDay, pMonth)){
		console.log("invalid input");
		continue;
	}

	let pDuration = prompt("On average, How long does it last(in days): ");
	
	if(!cycleCheck(pDuration)){
		console.log("invalid input");
		continue;
	}

	let cycle = prompt("On average, how long is your menstrual cycle(in days): ");

	if(!cycleCheck(cycle)){
		console.log("invalid input");
		continue;
	}

	let monthIndex = months[pMonth]
	pDay = Number(pDay);
	pDuration = Number(pDuration);
	cycle = Number(cycle)	;


	let ovulationDay = getOvulation(monthIndex, pDay, pDuration, cycle);
	const [windowStart, windowEnd] = getFertilityWindow(monthIndex, pDay, pDuration, cycle);
	let nextPeriodStart = getNextPeriod(monthIndex, pDay, pDuration, cycle);


	console.log(`your ovulation day is on ${ovulationDay.toString()}`);
	console.log(`your fertile window is between ${windowStart.toString()} and ${windowEnd.toString()}`);
	console.log(`your next period starts on ${nextPeriodStart.toString()}`);
	break



}



