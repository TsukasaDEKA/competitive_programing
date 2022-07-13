class Deque<T> {
  private head: number;
  private body: (T|undefined)[];

  constructor(body: T[]){
    const len = body.length;
    this.head = 3*len;
    this.body = Array(3*len).concat(body);
  }

  private get capacity(){
    return this.body.length;
  }

  public get length(){
    return this.body.length - this.head;
  };

  public slice(start: number, end=this.length){
    start += this.head;
    end += this.head;
    return this.body.slice(start, end) as T[];
  };

  public push(val: T){
    this.body.push(val);
  }

  public pop(){
    return this.body.pop();
  }

  public unshift(val: T){
    if(this.head == 0){
      this.head = 3*this.capacity;
      this.body = Array(3*this.capacity).concat(this.body);
    }
    this.head--;
    this.body[this.head] = val;
  }

  public shift(){
    if(this.head < this.capacity){
      const val = this.body[this.head];
      this.body[this.head] = undefined;
      this.head++;
      return val;
    }
    return undefined;
  }
}

import * as fs from "fs";
 
function Main(input: string) {
  const lines = input.split("\n");
  const [N, M] = lines[0].split(" ").map(Number);
  let EDGES = Array.from({length: N}, () => new Array());
  for(let i = 1; i <= M; i++){
    const [A, B] = lines[i].split(" ").map((x)=>Number(x)-1);
    EDGES[A].push(B);
  };

  // ここから BFS
  let ans = N;
  let deque = new Deque<number>([]);
  for(let i = 0; i < N; i++){
    deque.push(i);
    let checked: boolean[] = Array.from({length: N}, (_, j)=>j===i);
    while(deque.length > 0){
      let current = deque.shift();
      if(current == undefined) break;
      EDGES[current].forEach((n)=>{
        if(checked[n]) return;
        checked[n] = true;
        ans += 1;
        deque.push(n)
      });
    };
  };
  console.log(ans);
}
 
Main(fs.readFileSync("/dev/stdin", "utf8"));