
const prompt = require("prompt-sync")();


function numCheck(num){


	
	if(num.length == 0 || num < 1) return false;
	else
	if(isNaN(Number(num))) return false;
	else
	if(Number.isInteger(Number(num))) return true;
	else return false

}




function scoreCheck(score){

	if(score.length == 0 || score == 0) return false;
	else
	if(isNaN(Number(score))) return false;
	else
	if(!Number.isInteger(Number(score))) return false;
	else
	if(score >= 0 && score <= 100) return true;
	else return false;

}




function dSort(numbers){

	let sortedNumber = 0;

	for(let index = 0; index < numbers.length; index++){
		for(let index1 = 0; index1 < numbers.length; index1++){
	
			if(numbers[index1] < numbers[index]){
				sortedNumber = numbers[index1];
				numbers[index1] = numbers[index];
				numbers[index] = sortedNumber;
			}
		}
	}
	return numbers;
}




function studentDetails(outerSize, innerSize){

	const grades = {};
	
	for(let count = 1; count <= outerSize; count++){
		
		let i = 1, total = 0;
		const scores = [];
		
		while(i <= innerSize){
			console.log(`entering score for student ${count}`);
			let score = prompt(`score in subject ${i}: `);
		
			if(!scoreCheck(score)){
				console.log("invalid, try again");
				continue;
			}

			console.log("saving >>>>>>>>>>>>>>");
			console.log("saved successfully\n");

			total += Number(score);
			scores.push(Number(score));
			i++;
		}

		scores.push(total);

		let average = Number((total / scores.length).toFixed(2));
		scores.push(average);

		grades[`student ${count}`] = scores;
	}

	let averages = [];
	for(const item of Object.values(grades)) averages.push(item[item.length - 1]);
	averages = dSort(averages);

	for(const item of Object.values(grades)){
		for(let [index, avg] of Object.entries(averages)){

			index = Number(index);
			if(item[item.length - 1] == avg) item.push(index + 1);
		}
	}
		
	return grades;
}




function table(grades){

	let columns = grades["student 1"].length;

	console.log("==================================");

	process.stdout.write("STUDENT\t\t");
	for(let i = 1; i < columns - 2; i++) process.stdout.write(`SUB ${i}\t`);
	console.log("TOTAL\tAVG\tPOS");

	console.log("==================================");

	for(const [student, details] of Object.entries(grades)){

		process.stdout.write(`${student}\t`);
		for(let i = 0; i < details.length; i++) process.stdout.write(`${details[i]}\t`);
		console.log();
	}

	console.log("==================================");
	console.log("==================================");

}




function subjectSummary(grades){

	let subjectColumns = grades["student 1"].length - 3;

	let highestPasses = 0, highestPassesSubj = " ", lowestFails = 0, lowestFailsSubj = " ";

	for(let i = 0; i < subjectColumns; i++){

		let max = 0, maxName = " ", min = Number.MAX_VALUE, minName = " "; 
		let sum = 0, passes = 0, fails = 0;

		for(const [student, details] of Object.entries(grades)){
			if(details[i] > max){
				max = details[i];
				maxName = student;
			}

			else if(details[i] == max) maxName = maxName + " & " + student;

			if(details[i] < min){
				min = details[i];
				minName = student;
			}

			else if(details[i] == min) minName = minName + " & " + student;

			sum += details[i];

			details[i] > 49 ? passes++ : fails++;
		}

		let average = sum/Object.keys(grades).length;
		let hss = `${maxName} scoring ${max}`;
		let lss = `${minName} scoring ${min}`;

		console.log(`
subject ${i + 1}
highest scoring student is: ${hss}
lowest scoring student is: ${lss}
total score is: ${sum}
average score is: ${average}
number of passes : ${passes}
number of fails : ${fails}
		`);

		if(passes > highestPasses){
			highestPasses = passes;
			highestPassesSubj = `subject ${i + 1}`;
		}
		else if(passes == highestPasses) highestPassesSubj = highestPassesSubj + " & " + `subject ${i + 1}`

		if(fails > lowestFails){
			lowestFails = fails
			lowestFailsSubj = `subject ${i + 1}`
		}
		else if(fails == lowestFails) lowestFailsSubj = lowestFailsSubj + " & " + `subject ${i + 1}`

	}

	const array = [highestPasses, highestPassesSubj, lowestFails, lowestFailsSubj];

	return array

}






function classSummary(grades, array){

	let subjectColumns = grades["student 1"].length - 3;

	let max = 0, maxName = " ", min = Number.MAX_VALUE, minName = " "; 
	let maxSubj = " ", minSubj = " ";
	let total = 0, average = 0;
	let highest = 0, highestName = " ", lowest = Number.MAX_VALUE, lowestName = " ";


	for(const [student, details] of Object.entries(grades)){
		let sum = 0;
		for(let i = 0; i < subjectColumns; i++){

			if(details[i] > max){
				max = details[i];
				maxName = student;
				maxSubj = `subject ${i + 1}`;
			}
			else if(details[i] == max){
				maxName = maxName + " & " + student;
				maxSubj = maxSubj + " & "+`subject ${i + 1}`;
			}

			if(details[i] < min){
				min = details[i];
				minName = student;
				minSubj = `subject ${i + 1}`;
			}
			else if(details[i] == min){
				minName = minName + " & " + student;
				minSubj = minSubj + " & "+`subject ${i + 1}`;
			}

			sum += details[i];
		}

		average += sum/Object.keys(grades).length;
		total += sum;

		if(sum > highest){
			highest = sum;
			highestName = student;
		}
		else if(sum == highest) highestName = highestName + " & " + student;

		if(sum < lowest){
			lowest = sum;
			lowestName = student;
		}
		else if(sum == lowest) lowestName = lowestName + " & " + student;	

	}

	highestPasses = array[0];
	highestPassesSubj = array[1];
	lowestFails = array[2];
	lowestFailsSubj = array[3];

	console.log(`
The hardest subject is ${lowestFailsSubj} with a failure count of ${lowestFails} 
The easiest subject is ${highestPassesSubj} with a pass count of ${highestPasses} 
The overall highest score is scored by ${maxName} in ${maxSubj} scoring ${max}
The overall lowest score is scored by ${minName} in ${minSubj} scoring ${min}
========================================

CLASS SUMMARY
========================================
best graduating student is: ${highestName} scoring ${highest}
========================================

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
worst graduating student is: ${lowestName} scoring ${lowest} 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

========================================
class total score is: ${total}
class average score is: ${average}
========================================
		`)

}







console.log("welcome to hell");

while(true){
	let studentNo = prompt("How many students you got? ");
	
	if(!numCheck(studentNo)){
		console.log("invalid, try again");
		continue;
	}

	let subjectNo = prompt("How many subjects each of 'em got? ");

	if(!numCheck(subjectNo)){
		console.log("invalid, try again");
		continue;
	}

	studentNo = Number(studentNo);
	subjectNo = Number(subjectNo);

	const grades = studentDetails(studentNo, subjectNo);

	table(grades);
	const results = subjectSummary(grades);

	classSummary(grades, results);

	break;
}








