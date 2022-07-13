import * as fs from "fs";
 
function Main(input: string) {
  const lines = input.split("\n");
  const S = lines[0].slice(0, -1);
  const N = S.length;

  for(let i = Math.floor(N/2); i >= 1; i--){
    if(S.slice(0, i) == S.slice(i, 2*(i))){
      console.log(2*(i));
      return;
    }
  }
 
  console.log(-1);
}
 
Main(fs.readFileSync("/dev/stdin", "utf8"));