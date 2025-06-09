const prompt = require("prompt-sync")();



function unitCheck(unit){

	if(isNaN(Number(unit))) return false;
	else
	if(Number.isInteger(Number(unit))) return true;
	else return false

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




function invoice(catalogue, customerName, cashierName, discount){

	const date = new Date().toLocaleString();

	let bill = 0;
	for(const item of catalogue){
		bill += item[3];
	}

	discount = Number(discount);
	let billDiscount = Number(bill * (discount / 100));
	let VATDiscount = Number(bill * 0.175);
	let newBill = Number(bill - (billDiscount + VATDiscount);

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

	for(const item of catalogue){
		console.log(`\t\t${item[0]}\t${item[1]}\t${item[2].toFixed(2)}\t\t${item[3].toFixed(2)}\n`)
	}

	console.log(`
	--------------------------------------------------------
				Sub Total:	${bill.toFixed(2)}
				Discount:	${billDiscount.toFixed(2)}
				VAT @17.5%:	${VATDiscount.toFixed(2)}
	=======================================================
				Bill Total:	${newBill.toFixed(2)}
	=======================================================
	THIS IS NOT A RECEIPT KINDLY PAY ${newBill.toFixed(2)}
	=======================================================

	`);

	return newBill;

}



function receipt(catalogue, customerName, cashierName, discount, payment){

	const date = new Date().toLocaleString();

	let bill = 0;
	for(const item of catalogue){
		bill += item[3];
	}

	discount = Number(discount)
	payment = Number(payment)

	let billDiscount = Number(bill * (discount / 100));
	let VATDiscount = Number(bill * 0.175);
	let newBill = Number(bill - (billDiscount + VATDiscount);
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

	for(const item of catalogue){
		console.log(`\t\t${item[0]}\t${item[1]}\t${item[2].toFixed(2)}\t\t${item[3].toFixed(2)}\n`)
	}

	console.log(`
	--------------------------------------------------------
				Sub Total:	${bill.toFixed(2)}
				Discount:	${billDiscount.toFixed(2)}
				VAT @17.5%:	${VATDiscount.toFixed(2)}
	=======================================================
				Bill Total:	${newBill.toFixed(2)}
				Payment:	${payment.toFixed(2)}
				Balance:	${balance.toFixed(2)}
	=======================================================
					HAPPY BOMBING
	=======================================================


	`);

}





const catalogue = [];
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

		catalogue.push([item, units, price, total]);

		
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

		let bill = invoice(catalogue, customerName, cashierName, discount);

		while(true){
			let payment = prompt("Your Payment: ");
			if(!paymentCheck(payment, bill)){
				console.log("Invalid");
				continue;
			}

			receipt(catalogue, customerName, cashierName, discount, payment);
			break;
		}
		break;

	}
	break;

}













