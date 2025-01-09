function reverseString(str) {
  let endResult = '';
  for (let i = str.length - 1; i >= 0; i--) {
    endResult += str[i];
  }
  return endResult;
}

const toReverse = "exemplo";
const reversedString = reverseString(toReverse);

console.log(reversedString);