const prompt = require("prompt-sync")();

function testQuestions(){

	const questions = [
	{"A": "expand energy, enjoy groups", "B": "conserve energy, enjoy one-on-ones"},
	{"A": "Interpret literally", "B": "look for meaning and possibilities"},
	{"A": "logical, thinking, questioning", "B": "empathetic, feeling, accommodating"},
	{"A": "organised, orderly", "B": "flexible, adaptable"},
	{"A": "more outgoing, think out loud", "B": "more reserved, think to yourself"},
	{"A": "practical, realistic, experiential", "B": "imaginative, innovative, theoretical"},
	{"A": "candid, straight forward, frank", "B": "tactful, kind, encouraging"},
	{"A": "plan, schedule", "B": "unplanned, spontaneous"},
	{"A": "seek many tasks, public activities, interaction with others", "B": "seek private, solitary activities with quiet to concentrate"},
	{"A": "standard, usual, conventional", "B": "different, novel, unique"},
	{"A": "firm, tend to criticise, hold the line", "B": "gentle, tend to appreciate, conciliate"},
	{"A": "regulated, structured", "B": "easy-going, live and let live"},
	{"A": "external, communicative, express yourself", "B": "internal, reticent, keep to yourself"},
	{"A": "focus on here-and-now", "B": "look to the future, global perspective, big picture"},
	{"A": "tough-minded, just", "B": "tender-hearted, merciful"},
	{"A": "preparation, plan ahead", "B": "go with the flow, adapt as you go"},
	{"A": "active, initiate", "B": "reflective, deliberate"},
	{"A": "facts, things, what is", "B": "ideas, dreams, what could be, philosophical"},
	{"A": "matter of fact, issue-oriented", "B": "sensitive, people-oriented, compassionate"},
	{"A": "control, govern", "B": "latitude, freedom"}
	
	];

	return questions;

}


function energyStyleQuestions(questions, ESAnswers, selection){

	let choice = "";

	switch(selection){
		case 1:{
			while(true){
				console.log(`\nA. ${questions[0]['A']}`);
				console.log(`B. ${questions[0]['B']}`);

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			ESAnswers.push(`${choice}. ${questions[0][choice]}`);
			return choice;

		}

		case 2:{
			while(true){
				console.log(`\nA. ${questions[4]['A']}`)
				console.log(`B. ${questions[4]['B']}`)
				
				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			ESAnswers.push(`${choice}. ${questions[4][choice]}`)
			return choice

		}

		case 3:{
			while(true){
				console.log(`\nA. ${questions[8]['A']}`)
				console.log(`B. ${questions[8]['B']}`)
				
				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			ESAnswers.push(`${choice}. ${questions[8][choice]}`)
			return choice

		}

		case 4:{
			while(true){
				console.log(`\nA. ${questions[12]['A']}`)
				console.log(`B. ${questions[12]['B']}`)

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			ESAnswers.push(`${choice}. ${questions[12][choice]}`)
			return choice

		}

		case 5:{
			while(true){
				console.log(`\nA. ${questions[16]['A']}`);
				console.log(`B. ${questions[16]['B']}`);

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			ESAnswers.push(`${choice}. ${questions[16][choice]}`);
			return choice;

		}

		default: pass;

	}
}


		
function cognitiveStyleQuestions(questions, CSAnswers, selection){

	let choice = "";

	switch(selection){
		case 1:{
			while(true){
				console.log(`\nA. ${questions[1]['A']}`);
				console.log(`B. ${questions[1]['B']}`);

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			CSAnswers.push(`${choice}. ${questions[1][choice]}`);
			return choice;

		}

		case 2:{
			while(true){
				console.log(`\nA. ${questions[5]['A']}`)
				console.log(`B. ${questions[5]['B']}`)
				
				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			CSAnswers.push(`${choice}. ${questions[5][choice]}`)
			return choice

		}

		case 3:{
			while(true){
				console.log(`\nA. ${questions[9]['A']}`)
				console.log(`B. ${questions[9]['B']}`)
				
				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			CSAnswers.push(`${choice}. ${questions[9][choice]}`)
			return choice

		}

		case 4:{
			while(true){
				console.log(`\nA. ${questions[13]['A']}`)
				console.log(`B. ${questions[13]['B']}`)

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			CSAnswers.push(`${choice}. ${questions[13][choice]}`)
			return choice

		}

		case 5:{
			while(true){
				console.log(`\nA. ${questions[17]['A']}`);
				console.log(`B. ${questions[17]['B']}`);

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			CSAnswers.push(`${choice}. ${questions[17][choice]}`);
			return choice;

		}

		default: pass;

	}
}




function valuesStyleQuestions(questions, VSAnswers, selection){

	let choice = "";

	switch(selection){
		case 1:{
			while(true){
				console.log(`\nA. ${questions[2]['A']}`);
				console.log(`B. ${questions[2]['B']}`);

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			VSAnswers.push(`${choice}. ${questions[2][choice]}`);
			return choice;

		}

		case 2:{
			while(true){
				console.log(`\nA. ${questions[6]['A']}`)
				console.log(`B. ${questions[6]['B']}`)
				
				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			VSAnswers.push(`${choice}. ${questions[6][choice]}`)
			return choice

		}

		case 3:{
			while(true){
				console.log(`\nA. ${questions[10]['A']}`)
				console.log(`B. ${questions[10]['B']}`)
				
				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			VSAnswers.push(`${choice}. ${questions[10][choice]}`)
			return choice

		}

		case 4:{
			while(true){
				console.log(`\nA. ${questions[14]['A']}`)
				console.log(`B. ${questions[14]['B']}`)

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			VSAnswers.push(`${choice}. ${questions[14][choice]}`)
			return choice

		}

		case 5:{
			while(true){
				console.log(`\nA. ${questions[18]['A']}`);
				console.log(`B. ${questions[18]['B']}`);

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			VSAnswers.push(`${choice}. ${questions[18][choice]}`);
			return choice;

		}

		default: pass;

	}
}




function lifeStyleQuestions(questions, LSAnswers, selection){

	let choice = "";

	switch(selection){
		case 1:{
			while(true){
				console.log(`\nA. ${questions[3]['A']}`);
				console.log(`B. ${questions[3]['B']}`);

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			LSAnswers.push(`${choice}. ${questions[3][choice]}`);
			return choice;

		}

		case 2:{
			while(true){
				console.log(`\nA. ${questions[7]['A']}`)
				console.log(`B. ${questions[7]['B']}`)
				
				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			LSAnswers.push(`${choice}. ${questions[7][choice]}`)
			return choice

		}

		case 3:{
			while(true){
				console.log(`\nA. ${questions[11]['A']}`)
				console.log(`B. ${questions[11]['B']}`)
				
				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			LSAnswers.push(`${choice}. ${questions[11][choice]}`)
			return choice

		}

		case 4:{
			while(true){
				console.log(`\nA. ${questions[15]['A']}`)
				console.log(`B. ${questions[15]['B']}`)

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			LSAnswers.push(`${choice}. ${questions[15][choice]}`)
			return choice

		}

		case 5:{
			while(true){
				console.log(`\nA. ${questions[19]['A']}`);
				console.log(`B. ${questions[19]['B']}`);

				choice= prompt("A or B: ").toUpperCase();

				switch(choice){
					case "A":
					case "B":
						break;
					default:{
						console.log("invalid choice");
						continue;
					}
				}break;
			}
			LSAnswers.push(`${choice}. ${questions[19][choice]}`);
			return choice;

		}

		default: pass;

	}
}
	



function type(energy, cognitive, value, life){

	let personality = energy + cognitive + value + life;

	switch(personality){

		case "INFP":
			console.log(`
your personality type: INFP
known as The Healer,
The Thoughtful Idealist (MBTI),
The Mediator (16Personalities), etc
	
read more about your personality here:
www.truity.com/blog/personality-type/infp
			`);
			return "INFP";



		case "INTJ":
			console.log(`
your personality type: INTJ

known as The Mastermind,
The Conceptual Planner (MBTI)
The Architect (16Personalities), etc
	
read more about your personality here:
www.truity.com/blog/personality-type/intj
			`);
			return "INTJ";



		case "INFJ":
			console.log(`
your personality type: INFJ

known as The Counsellor,
The Insightful Visionary (MBTI)
The Advocate (16Personalities), etc
	
read more about your personality here:
www.truity.com/blog/personality-type/infj
			`);
			return "INFJ";



		case "INTP":
			console.log(`
your personality type: INTP

known as The Architect,
The Objective Analyst (MBTI)
The Logician (16Personalities)
	
read more about your personality here:
www.truity.com/blog/personality-type/intp
			`);
			return "INTP";



		case "ENFP":
			console.log(`
your personality type: ENFP

known as The Champion,
The Imaginative Motivator (MBTI)
The Campaigner (16Personalities)
	
read more about your personality here:
www.truity.com/blog/personality-type/enfp
			`);
			return "ENFP";



		case "ENTJ":
			console.log(`
your personality type: ENTJ

known as The Commander
	
read more about your personality here:
www.truity.com/blog/personality-type/entj
			`);
			return "ENTJ";



		case "ENTP":
			console.log(`
your personality type: ENTP

known as The Visionary
	
read more about your personality here:
www.truity.com/blog/personality-type/entp
			`);
			return "ENTP";



		case "ENFJ":
			console.log(`
your personality type: ENFJ

known as The Teacher
	
read more about your personality here:
www.truity.com/blog/personality-type/enfj
			`);
			return "ENFJ";



		case "ISFJ":
			console.log(`
your personality type: ISFJ

known as The Protector
	
read more about your personality here:
www.truity.com/blog/personality-type/isfj
			`);
			return "ISFJ";



		case "ISFP":
			console.log(`
your personality type: ISFP

known as The Composer
	
read more about your personality here:
www.truity.com/blog/personality-type/isfp
			`);
			return "ISFP";



		case "ISTJ":
			console.log(`
your personality type: ISTJ

known as The Inspector
	
read more about your personality here:
www.truity.com/blog/personality-type/istj
			`);
			return "ISTJ";



		case "ISTP":
			console.log(`
your personality type: ISTP

known as The Craftsperson
	
read more about your personality here:
www.truity.com/blog/personality-type/istp
			`);
			return "ISTP";



		case "ESFJ":
			console.log(`
your personality type: ESFJ

known as The Provider
	
read more about your personality here:
www.truity.com/blog/personality-type/esfj
			`);
			return "ESFJ";



		case "ESFP":
			console.log(`
your personality type: ESFP

known as The Performer
	
read more about your personality here:
www.truity.com/blog/personality-type/esfp
			`);
			return "ESFP";



		case "ESTJ":
			console.log(`
your personality type: ESTJ

known as The Supervisor
	
read more about your personality here:
www.truity.com/blog/personality-type/estj
			`);
			return "ESTJ";



		case "ESTP":
			console.log(`
your personality type: ESTP

known as The Dynamo
	
read more about your personality here:
www.truity.com/blog/personality-type/estp
			`);
			return "ESTP";

	}

}






const questions = testQuestions();

const ESAnswers = [];
const CSAnswers = [];
const VSAnswers = [];
const LSAnswers = []	;

const counters = { E: 0, I: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0 };

console.log("Welcome to the terrorism test");
let name = prompt("what is your name? ");
console.log("Choose below what option most describes you.");

for(let selection = 1; selection < 6; selection++){

	let EI = energyStyleQuestions(questions, ESAnswers, selection)
	counters[EI === "A" ? "E" : "I"]++;

	let SN = cognitiveStyleQuestions(questions, CSAnswers, selection)
	counters[SN === "A" ? "S" : "N"]++;

	let TF = valuesStyleQuestions(questions, VSAnswers, selection)
	counters[TF === "A" ? "T" : "F"]++;

	let JP = lifeStyleQuestions(questions, LSAnswers, selection)
	counters[JP === "A" ? "J" : "P"]++;

}


console.log(`\nhello ${name}. you selected:\n`);

for(let item of ESAnswers) console.log(item);
console.log(`No of As selected: ${counters.E}`);
console.log(`No of Bs selected: ${counters.I}\n`);

for(let item of CSAnswers) console.log(item);
console.log(`No of As selected: ${counters.S}`);
console.log(`No of Bs selected: ${counters.N}\n`);

for(let item of VSAnswers) console.log(item);
console.log(`No of As selected: ${counters.T}`);
console.log(`No of Bs selected: ${counters.F}\n`);

for(let item of LSAnswers) console.log(item);
console.log(`No of As selected: ${counters.J}`);
console.log(`No of Bs selected: ${counters.P}\n`);	


let energy = counters.E >= counters.I ? "E" : "I";
let cognitive = counters.S >= counters.N ? "S" : "N";
let value = counters.T >= counters.F ? "T" : "F";
let life = counters.J >= counters.P ? "J" : "P";

type(energy, cognitive, value, life);



