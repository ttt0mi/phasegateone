const prompt = require("prompt-sync")();


function check(cardNumber){

	if(isNaN(Number(cardNumber))) return false;
	else
	if(Number.isInteger(Number(cardNumber))) return true;
	else return false

}


function validation(cardNumber){

	let sum = 0;

	for(let index = cardNumber.length - 2; index > -1; index-=2){

		let digit = Number(cardNumber.charAt(index));

		let num = digit * 2;
		if(num > 9) num = (num % 10) + 1;

		sum += num;
	}

	for(let index = cardNumber.length - 1; index > -1; index-=2){

		sum += Number(cardNumber.charAt(index));
	}
		
	if(sum % 10 == 0) return true;
	else return false;
}



function cardIssuer(cardNumber){

		if(cardNumber.length <= 13 || cardNumber.length > 16) return "Invalid Card Length";	

		else if(cardNumber.startsWith("4")) return "Visa";

		else if(cardNumber.startsWith("5")) return "MasterCard";
	
		else if(cardNumber.startsWith("6")) return "Discover";

		else if(cardNumber.startsWith("37")) return "American Express";

		else return "Invalid Card Issuer";

}


while(true){

	let cardNumber = prompt("what is your card number? ");

	if(!check(cardNumber)){
		console.log("Invalid characters present");
		continue;
	}

	let issuer = cardIssuer(cardNumber);
	let checker = validation(cardNumber);

	if(issuer == "Invalid Card Issuer" || issuer == "Invalid Card Length") checker = false;
		
	let validCheck = checker ? "valid" : "invalid";

	console.log("Credit Card Type: " + issuer);
	console.log("Credit Card Number: " + cardNumber);
	console.log("Credit Card Digit Length: " + cardNumber.length);
	console.log("Credit Card Status: " + validCheck);
	break;


}







