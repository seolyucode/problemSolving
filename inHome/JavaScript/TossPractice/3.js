function calculate({ type, operands }) {
  //   const dictObject = {};

  // console.log(type)
  //   return "hellp";
  //   console.log(type[type]);
  let num1 = 0;
  let num2 = 1;
  if (type === "add") {
    // console.log("2");
    for (let i = 0; i < operands.length; i++) {
      //   console.log("2");
      num1 += operands[i];
    }
    return num1;
  } else if (type === "multiply") {
    // console.log("2");
    for (let i = 0; i < operands.length; i++) {
      //   console.log("2");
      num2 *= operands[i];
    }
    return num2;
  }
}

console.log(calculate({ type: "multiply", operands: [1, 2] }));
