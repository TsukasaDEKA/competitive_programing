export

// type Node<T> = {
//   previous: Node<T>|null|undefined,
//   value: T,
//   next: Node<T>|null|undefined,
// }

// interface Node<T>{
//   previous: Node<T>|null|undefined,
//   value: T,
//   next: Node<T>|null|undefined,
// }


class Deque<T> {
  private head: Node<T>|null = null;
  private tail: Node<T>|null = null;
  private size: number = 0;

  constructor(values: T[]){
    values.forEach((v)=>{
      this.push(v)
    })
  }

  public get length(){
    return this.size;
  };

  public push(value: T){
    if(this.size == 0){
      this.tail = this.head = {
        previous: null,
        value: value,
        next: null,
        hoge: null
      };
    }else{
      // 末尾に繋げていく
      const prev_tail = this.tail!;
      this.tail = {
        previous: prev_tail,
        value: value,
        next: null,
      };
      prev_tail.next = this.tail;
    };
    this.size++;
  }

  public pop(){
    if(this.size == 0) return null;

    this.size--;
    const value = this.tail!.value;
    this.tail = this.tail?.previous ?? null;
    if(this.tail != null){
      this.tail.next = null;
    }
    if(this.tail?.previous == null){
      this.head = null;
    }

    return value;
  }
}

// TEST
let deque = new Deque([1, 2, 3, 4, 5])

console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());

console.log(deque.pop());
console.log(deque.pop());

deque.push(10);
deque.push(20);
console.log(deque.pop());
console.log(deque.pop());
console.log(deque)
