import * as fs from "fs";
 
function Main(input: string) {
  const lines = input.split("\n");
  const N = Number(lines[0]);
  const A = lines.slice(1, N+1).map(x => Number(x)-1);

  let current = 0;
  console.error(A);
  for(let i = 0; i < N; i++){
    current = A[current];
    console.error(current);
    if(current === 1){
      console.log(i+1);
      return;
    }
  }
 
  console.log(-1);
}
 
Main(fs.readFileSync("/dev/stdin", "utf8"));