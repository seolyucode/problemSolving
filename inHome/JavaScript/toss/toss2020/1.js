function getMaskedName(name) {
    // 함수를 작성해주세요
    let answer = '';
    for(let i=0; i<name.length; i++) {
        if (i<2) {
            answer += name[i]
        } else {
            answer += '*';
        }
    }
	return answer;
}

console.log(getMaskedName('문토스'));