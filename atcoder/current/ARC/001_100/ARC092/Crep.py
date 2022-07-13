import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3
2 0
3 1
1 3
4 2
0 4
5 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
0 0
1 1
5 2
2 3
3 4
4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
2 2
3 3
0 0
1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
0 0
7 3
2 2
4 8
1 6
8 5
6 9
5 4
9 1
3 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """5
0 0
1 1
5 5
6 6
7 7
2 2
3 3
4 4
8 8
9 9"""
        output = """4"""
        self.assertIO(input, output)

import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

class SortedMultiset(Generic[T]):
  BUCKET_RATIO = 50
  REBUILD_RATIO = 170

  def _build(self, a=None) -> None:
    "Evenly divide `a` into buckets."
    if a is None: a = list(self)
    size = self.size = len(a)
    bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
    self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
  
  def __init__(self, a: Iterable[T] = []) -> None:
    "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
    a = list(a)
    if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
        a = sorted(a)
    self._build(a)

  def __iter__(self) -> Iterator[T]:
    for i in self.a:
      for j in i: yield j

  def __reversed__(self) -> Iterator[T]:
    for i in reversed(self.a):
      for j in reversed(i): yield j
  
  def __len__(self) -> int:
    return self.size
  
  def __repr__(self) -> str:
    return "SortedMultiset" + str(self.a)
  
  def __str__(self) -> str:
    s = str(list(self))
    return "{" + s[1 : len(s) - 1] + "}"

  def _find_bucket(self, x: T) -> List[T]:
    "Find the bucket which should contain x. self must not be empty."
    for a in self.a:
      if x <= a[-1]: return a
    return a

  def __contains__(self, x: T) -> bool:
    if self.size == 0: return False
    a = self._find_bucket(x)
    i = bisect_left(a, x)
    return i != len(a) and a[i] == x

  def count(self, x: T) -> int:
    "Count the number of x."
    return self.index_right(x) - self.index(x)

  def add(self, x: T) -> None:
    "Add an element. / O(√N)"
    if self.size == 0:
      self.a = [[x]]
      self.size = 1
      return
    a = self._find_bucket(x)
    insort(a, x)
    self.size += 1
    if len(a) > len(self.a) * self.REBUILD_RATIO:
      self._build()

  def discard(self, x: T) -> bool:
    "Remove an element and return True if removed. / O(√N)"
    if self.size == 0: return False
    a = self._find_bucket(x)
    i = bisect_left(a, x)
    if i == len(a) or a[i] != x: return False
    a.pop(i)
    self.size -= 1
    if len(a) == 0: self._build()
    return True

  def lt(self, x: T) -> Union[T, None]:
    "Find the largest element < x, or None if it doesn't exist."
    for a in reversed(self.a):
      if a[0] < x:
        return a[bisect_left(a, x) - 1]

  def le(self, x: T) -> Union[T, None]:
    "Find the largest element <= x, or None if it doesn't exist."
    for a in reversed(self.a):
      if a[0] <= x:
        return a[bisect_right(a, x) - 1]

  def gt(self, x: T) -> Union[T, None]:
    "Find the smallest element > x, or None if it doesn't exist."
    for a in self.a:
      if a[-1] > x:
        return a[bisect_right(a, x)]

  def ge(self, x: T) -> Union[T, None]:
    "Find the smallest element >= x, or None if it doesn't exist."
    for a in self.a:
      if a[-1] >= x:
        return a[bisect_left(a, x)]

  def __getitem__(self, x: int) -> T:
    "Return the x-th element, or IndexError if it doesn't exist."
    if x < 0: x += self.size
    if x < 0: raise IndexError
    for a in self.a:
      if x < len(a): return a[x]
      x -= len(a)
    raise IndexError

  def index(self, x: T) -> int:
    "Count the number of elements < x."
    ans = 0
    for a in self.a:
      if a[-1] >= x:
        return ans + bisect_left(a, x)
      ans += len(a)
    return ans

  def index_right(self, x: T) -> int:
    "Count the number of elements <= x."
    ans = 0
    for a in self.a:
      if a[-1] > x:
        return ans + bisect_right(a, x)
      ans += len(a)
    return ans


def resolve():
  inf = 10**18+1
  N = int(input())

  RED = [[int(x) for x in input().split(" ")]+[0] for _ in range(N)]
  BLUE = [[int(x) for x in input().split(" ")]+[1] for _ in range(N)]
  POINTS = sorted(RED + BLUE)

  sorted_multi_set = SortedMultiset([])
  ans = 0
  for i in range(2*N):
    _, y, c = POINTS[i]
    # 青点だったら
    if c == 1:
      val = sorted_multi_set.lt(y)
      if val is not None:
        ans+=1
        sorted_multi_set.discard(val)
    else:
      sorted_multi_set.add(y)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()