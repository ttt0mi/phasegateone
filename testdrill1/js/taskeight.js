

let total = o;

for(let digit = 2; digit < 11; digit+=2){
	

	if(digit % 4 == 0){
	
		for(let i = 1; i < 6; i++) total += digit ** i;

	}
	
}

console.log(total);

