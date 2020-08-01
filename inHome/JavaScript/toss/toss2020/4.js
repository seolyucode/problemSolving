function formatToKoreanNumber(num) {
	/* 이 함수를 구현해주세요 */
	// let money = parseInt(String(num).length / 4);
	let money = String(num).length / 4;
    let answer = 0;
	if(money > 2) {
		if(String(num).length === 12) {
			answer = String(Number(String(num).substring(0,4)).toLocaleString())+'억 '+String(Number(String(num).substring(4,8)).toLocaleString())+'만 '+String(Number(String(num).substring(8,12)).toLocaleString())
		} else if(String(num).length === 11) {
			answer = String(Number(String(num).substring(0,3)).toLocaleString())+'억 '+String(Number(String(num).substring(3,7)).toLocaleString())+'만 '+String(Number(String(num).substring(7,11)).toLocaleString())
		} else if(String(num).length === 10) {
			answer = String(Number(String(num).substring(0,2)).toLocaleString())+'억 '+String(Number(String(num).substring(2,6)).toLocaleString())+'만 '+String(Number(String(num).substring(6,10)).toLocaleString())
		} else if(String(num).length === 9) {
			answer = String(Number(String(num).substring(0,1)).toLocaleString())+'억 '+String(Number(String(num).substring(1,5)).toLocaleString())+'만 '+String(Number(String(num).substring(5,9)).toLocaleString())}
	} else if(money === 2) {
		answer = String(Number(String(num).substring(0,4)).toLocaleString())+'만 '+String(Number(String(num).substring(4,8)).toLocaleString())
	} else if(money < 2 && money > 1) {
		if(String(num).length === 7) {
			answer = String(Number(String(num).substring(0,3)).toLocaleString())+'만 '+String(Number(String(num).substring(3,7)).toLocaleString())
		} else if(String(num).length === 6) {
			answer = String(Number(String(num).substring(0,2)).toLocaleString())+'만 '+String(Number(String(num).substring(2,6)).toLocaleString())
		} else if(String(num).length === 5) {
			answer = String(Number(String(num).substring(0,1)).toLocaleString())+'만 '+String(Number(String(num).substring(1,5)).toLocaleString())
		}
	} else {
		if(String(num).length === 4) {
			answer = String(Number(String(num).substring(0,4)).toLocaleString())
		} else if(String(num).length === 3) {
			answer = String(Number(String(num).substring(0,3)).toLocaleString())
		} else if(String(num).length === 2) {
			answer = String(Number(String(num).substring(0,2)).toLocaleString())
		} else if(String(num).length === 1) {
			answer = String(Number(String(num).substring(0,1)).toLocaleString())
		}
    }

    let result = answer.replace(' 0만', '');
    let result1 = result.replace(' 0', '');
    return result1;
}
console.log(formatToKoreanNumber(100000001))
console.log(formatToKoreanNumber(100000000001))
console.log(formatToKoreanNumber(10000))
console.log(formatToKoreanNumber(100000))
console.log(formatToKoreanNumber(0))