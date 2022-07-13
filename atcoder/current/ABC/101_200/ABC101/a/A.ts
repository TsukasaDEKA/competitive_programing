import * as fs from 'fs';

const input = fs.readFileSync("/dev/stdin", "utf8").split("\n");
const S = input[0].split("").map(x => x);

const main = () => {
  let count = 0;
  S.forEach(s => {
    if(s === "+"){
      count+=1;
    }else{
      count-=1
    }
  })
  console.log(count);
};

main();