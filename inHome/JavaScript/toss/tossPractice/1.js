function printAgeGroup(age) {
  // 이 함수를 구현해주세요.
  console.log(age);
  if (10 <= age && age < 90) {
    let num = String(age)[0];
    return num + "0대";
  } else if (age < 10) {
    return "10대 미만";
  } else if (age >= 90) {
    return "90대 이상";
  }
}

console.log(printAgeGroup(20));
console.log(printAgeGroup(99));
console.log(printAgeGroup(8));
