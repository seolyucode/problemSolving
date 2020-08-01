function splitDutchPayAmount({peopleCount, amount}) {
    /* 이 함수를 구현해주세요. */

    let dutchArray = [];
    let dutch = parseInt(amount / peopleCount);
    let dutchRemainder = amount - (peopleCount*dutch);

    for(let i=0; i<peopleCount; i++) {
        if(i == 0) {
            console.log(dutch+dutchRemainder)
            dutchArray.push(dutch+dutchRemainder);
        } else {
            dutchArray.push(dutch);
        }
    }
    console.log(dutchArray)
	return dutchArray;
}

splitDutchPayAmount({"peopleCount":3,"amount":4})
