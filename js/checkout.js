const prompt = require("prompt-sync")();



function unitCheck(unit){

	if(isNaN(Number(unit))) return false
	else return true

}


function priceCheck(price){

	if(isNaN(Number(price))) return false
	else return true

}


function discountCheck(discount){

	if(isNaN(Number(discount))) return false

	discount = Number(discount)
	if(discount > 0 && discount < 100) return true
	else return false

}


function paymentCheck(payment, bill){

	if(isNaN(Number(payment))) return false

	payment = Number(payment)
	if(payment < 0 || payment < bill) return false
	else return true

}




function invoice(cart, customerName, cashierName, discount){

	const date = new Date().toLocaleString();
	

	let bill = 0;
	for(const item of cart){
		bill += item[3];
	}

	let billDiscount = Number(bill * (discount / 100));
	let VATDiscount = Number(bill * 0.175);
	let newBill = Number(bill - billDiscount);

	console.log(`

	Al-Qaeda Auctions
	MAIN BRANCH
	LOCATION: secret
	TEL: those who need to know, know
	Date: ${date}
	Cashier: ${cashierName}
	Customer's Name: ${customerName}

	=======================================================
		ITEM	QTY	PRICE(£)	TOTAL(£)
	--------------------------------------------------------
	`);

	for(const item of cart){
		console.log(`\t\t${item[0]}\t${item[1]}\t${item[2]}\t\t${item[3]}\n`)
	}

	console.log(`
	--------------------------------------------------------
				Sub Total:	${bill}
				Discount:	${billDiscount}
				VAT @17.5%:	${VATDiscount}
	=======================================================
				Bill Total:	${newBill}
	=======================================================
	THIS IS NOT A RECEIPT KINDLY PAY ${newBill}
	=======================================================

	`);

	return newBill;

}



function receipt(cart, customerName, cashierName, discount, payment){

	const date = new Date().toLocaleString();

	let bill = 0;
	for(const item of cart){
		bill += item[3];
	}

	let billDiscount = Number(bill * (discount / 100));
	let VATDiscount = Number(bill * 0.175);
	let newBill = Number(bill - billDiscount);
	let balance = Number(payment - newBill);
	

	console.log(`

	Al-Qaeda Auctions
	MAIN BRANCH
	LOCATION: secret
	TEL: those who need to know, know
	Date: ${date}
	Cashier: ${cashierName}
	Customer's Name: ${customerName}

	=======================================================
		ITEM	QTY	PRICE(£)	TOTAL(£)
	--------------------------------------------------------
	`);

	for(const item of cart){
		console.log(`\t\t${item[0]}\t${item[1]}\t${item[2]}\t\t${item[3]}\n`)
	}

	console.log(`
	--------------------------------------------------------
				Sub Total:	${bill}
				Discount:	${billDiscount}
				VAT @17.5%:	${VATDiscount}
	=======================================================
				Bill Total:	${newBill}
				Payment:	${payment}
				Balance:	${balance}
	=======================================================
					HAPPY BOMBING
	=======================================================


	`);

}





const cart = [];
let proceed = true;


while(true){

	let customerName = prompt("What is the customer's name: ");

	while(proceed){
		let item = prompt("What did the user buy? ");

		let units = prompt("how many units were purchased? ");
		if(!unitCheck(units)){
			console.log("Invalid");
			continue;
		}

		let price = prompt("how much per unit: ")
		if(!priceCheck(price)){
			console.log("Invalid");
			continue;
		}


		units = Number(units);
		price = Number(price);
		let total = units * price;

		cart.push([item, units, price, total]);

		
		while(proceed){
			let choice = prompt("Enter yes to add more items, no to get invoice: ");
			choice = choice.toUpperCase();

			switch(choice){
				case "YES": break;

				case "NO": {
					proceed = false;
					break;
				}

				default: print("invalid choice, try again");

			}
		} 
	}	

	while(true){
		let cashierName = prompt("What is your name: ");

		let discount = prompt("what percentage discount is being offered? ")
		if(!discountCheck(discount)){
			console.log("Invalid");
			continue;
		}

		discount = Number(discount);

		let bill = invoice(cart, customerName, cashierName, discount);

		while(true){
			let payment = prompt("Your Payment: ");
			if(!paymentCheck(payment, bill)){
				console.log("Invalid");
				continue;
			}

			receipt(cart, customerName, cashierName, discount, payment);
			break;
		}
		break;

	}
	break;

}













