function getAmount(text) {
  // 이 함수를 구현해주세요.
  //   console.log(typeof Number(text[0]));
  //   console.log(text.length);
  //   console.log(typeof text[1]);
  //   let numArray = new Array();
  let numArray = "";

  for (let i = 0; i < text.length; i++) {
    if (!isNaN(Number(text[i]))) {
      numArray += text[i];
    }
  }
  return Number(numArray);
}

console.log(getAmount("$1,250"));
