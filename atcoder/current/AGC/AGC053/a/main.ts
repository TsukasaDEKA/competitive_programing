import * as fs from "fs";
 
function Main(input: string) {
  const lines = input.split("\n");
  const N = Number(lines[0]);
  const A = lines[2].split(" ").map(Number)
  const K =  Math.min(...Array.from({length: N}, (_, i) => Math.abs(A[i]-A[i+1])))

  let B = Array.from({length: K}, (_, i)=>[...Array.from({length: N+1}, (_, i) => Math.floor(A[i]/K))])
  
  for(let i = 0; i < N+1; i++){
    for(let j = 0; j < A[i]%K; j++){
      B[j][i] += 1
    }
  }
  console.log(K)
  for(let i = 0; i < K; i++) console.log(...B[i])
}
 
Main(fs.readFileSync("/dev/stdin", "utf8"));