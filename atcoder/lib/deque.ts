export class Deque<T> {
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

// TEST
let deque = new Deque([1, 2, 3, 4, 5])

console.log(deque.shift());
deque.unshift(10);
deque.unshift(20);
deque.unshift(30);
deque.unshift(40);
console.log(deque.shift());
console.log(deque.shift());
console.log(deque.shift());
console.log(deque.shift());
deque.push(40);
console.log(deque.shift());

console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.shift());
deque.unshift(10);
console.log(deque.pop());
console.log(deque);
console.log(deque.length);
deque.unshift(10);
console.log(deque);
console.log(deque.length);
