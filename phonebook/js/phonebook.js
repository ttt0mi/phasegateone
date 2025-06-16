
const prompt = require("prompt-sync")();


function phoneCheck(contacts, phone){

	if(contacts.length > 0){
		for(let i = 0; i < contacts.length; i++){
			if(phone == contacts[i]['Phone Number']) return false;
		}
	}
	
	if(isNaN(Number(phone))) return false;
	
	if(phone.length != 11) return false;

	if(!Number.isInteger(Number(phone))) return false;	

	const codes = ["070","080","081","090"];

	for(let code of codes){	
		if(phone.startsWith(code)) return true;
	}
	
	return false;

}



function add(contacts, firstName, lastName, phone){

	contact = {}

	contact['First Name'] = firstName;
	contact['Last Name'] = lastName;
	contact['Phone Number'] = phone;

	contacts.push(contact);
	return "contact added";

}



function edit(contacts, choice){

	if(!Number.isInteger(Number(choice))) return "invalid choice";

	choice = Number(choice);
//broken
	if(choice > contacts.length) return "invalid choice mate";

	choice = choice - 1;

	for(let index = 0; index < contacts.length; index++){
		if(choice == index){
			delete contacts[index];
			while(true){
				let firstName = prompt("first name: ");
				if(firstName.length == 0){
					console.log("invalid");
					continue;
				}		

				let lastName = prompt("last name: ");
				if(lastName.length == 0){
					console.log("invalid");
					continue;
				}	
				
				let phone = prompt("phone number: ");
				if(!phoneCheck(contacts, phone)){
					console.log("invalid nigerian phone number");
					continue;
				}
	
				contacts[index] = {'First Name': firstName, 'Last Name': lastName, 'Phone Number': phone};
				return "contact edited"
			}
		}
	}

}



function remove(contacts, choice){

	if(!Number.isInteger(Number(choice))) return "invalid choice";

	choice = Number(choice);
//broken
	if(choice > contacts.length) return "invalid choice mate";

	choice = choice - 1;

	if(choice >= contacts.length) return "invalid choice";

	for(let index = 0; index < contacts.length; index++){
		
		if(choice == index){
			contacts.splice(choice, 1);
			return "contact removed";
		}
	}

}



function findViaFirstName(contacts, firstName){

	for(let i = 0; i < contacts.length; i++){

		if(firstName == contacts[i]['First Name']){
			for(const [iden, info] of Object.entries(contacts[i])) console.log(`${iden}: ${info}`);
			return true;
		}
	}

	return false;

}



function findViaLastName(contacts, lastName){

	for(let i = 0; i < contacts.length; i++){

		if(lastName == contacts[i]['Last Name']){
			for(const [iden, info] of Object.entries(contacts[i])) console.log(`${iden}: ${info}`);
			return true;
		}
	}

	return false;

}



function findViaPhoneNumber(contacts, phone){

	for(let i = 0; i < contacts.length; i++){

		if(phone == contacts[i]['Phone Number']){
			for(const [iden, info] of Object.entries(contacts[i])) console.log(`${iden}: ${info}`);
			return true;
		}
	}

	return false;

}



function all_contacts(contacts){

	for(let i = 0; i < contacts.length; i++){
		console.log(`\ncontact ${i + 1}`);
		for(const [iden, info] of Object.entries(contacts[i])) console.log(`${iden}: ${info}`);
	}
}




const contacts = [];
let proceed = true;

while(proceed){

	console.log(`
phone book for a nigerian

1 >>> add contact
2 >>> edit contact
3 >>> remove contact
4 >>> find contact by first name
5 >>> find contact by last name
6 >>> find contact by phone number
0 >>> Exit
	`);

	let choice = Number(prompt("pick a number: "));

	switch(choice){

		case 1:{
			while(true){
				let firstName = prompt("first name: ");
				if(firstName.length == 0){
					console.log("invalid");
					continue;
				}		

				let lastName = prompt("last name: ");
				if(lastName.length == 0){
					console.log("invalid");
					continue;
				}	
				
				let phone = prompt("phone number: ");
				if(!phoneCheck(contacts, phone)){
					console.log("invalid nigerian phone number");
					continue;
				}

				console.log(add(contacts, firstName, lastName, phone));
				break;			
			}
			break;
		}

		case 2:{
			all_contacts(contacts);

			let input = prompt("pick contact number to edit: ");

			console.log(edit(contacts, choice));
			break;
		}

		case 3:{
			all_contacts(contacts);

			let input = prompt("pick contact number to remove: ");

			console.log(edit(contacts, choice));
			break;
		}

		case 4:{
			while(true){
				
				let input = prompt("enter first name to find contact: ");
				if(input.length == 0){
					console.log("invalid");
					continue;
				}	

				let fn = findViaFirstName(contacts, input);

				if(!fn) console.log("contact not found");
				break;
			}
			break;
		}

		case 5:{
			while(true){
				
				let input = prompt("enter last name to find contact: ");
				if(input.length == 0){
					console.log("invalid");
					continue;
				}

				let ln = findViaLastName(contacts, input);

				if(!ln) console.log("contact not found");
				break;
			}
			break;
		}

		case 6:{
			while(true){
				
				let input = prompt("enter phone number to find contact: ");
				if(input.length == 0){
					console.log("invalid");
					continue;
				}

				let pn = findViaPhoneNumber(contacts, input);

				if(!pn) console.log("contact not found");
				break;
			}
			break;
		}

		case 0:{
			console.log("bye");
			proceed = false;
			break;
		}

		default:{
			console.log("invalid choice");
			continue;
		}
	}
}


















