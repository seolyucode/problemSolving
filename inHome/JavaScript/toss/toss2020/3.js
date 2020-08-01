function commaizeNumber(num) {
    // let number = '';
    // let numLength = String(num).length;
    // let commaNum = parseInt(numLength / 3);
    // let commaPos = numLength - commaNum*3;

    // let numArray = String(num);


    
    // let nume = numArray.shift();
    

    // for(let i=0; i<numLength+commaNum; i++) {
    //     if(i==commaPos) {
    //     } else {
    //     }
    // }
    
    // console.log(nume)
    // return number;

    return num.toLocaleString();

}

// console.log(commaizeNumber('1234567'));
console.log(commaizeNumber(1234567));