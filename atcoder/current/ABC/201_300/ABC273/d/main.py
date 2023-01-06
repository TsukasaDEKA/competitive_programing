import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
# product('ABCD', repeat=2) => AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
from itertools import product
# permutations('ABCD', 2) => AB AC AD BA BC BD CA CB CD DA DB DC
from itertools import permutations
# combinations('ABCD', 2) => AB AC AD BC BD CD
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_left
# 0埋めされた二進数表現
f'{9:05b}'

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]
dh8 = [-1, -1, -1,  0,  0,  1,  1,  1]
dw8 = [-1,  0,  1, -1,  1, -1,  0,  1]

# https://github.com/tatyam-prime/SortedSet
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
# multiset
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
  from collections import defaultdict
  inf = 10**18+1
  H, W, R, C = map(int, input().split(" "))
  R, C = R-1, C-1

  columns = {}
  rows = {}

  N = int(input())
  for _ in range(N):
    r, c = [int(x)-1 for x in input().split(" ")]
    if c in columns:
      columns[c].add(r)
    else:
      columns[c] = SortedMultiset([r])

    if r in rows:
      rows[r].add(c)
    else:
      rows[r] = SortedMultiset([c])

  Q = int(input())
  for _ in range(Q):
    d, l = input().split(" ")
    l = int(l)
    if d == "L":
      if R not in rows:
        # print(d, l)
        C = max(0, C-l)
      else:
        v = rows[R].lt(C)
        # print(d, l, v)
        if v is not None:
          C = max(0, v+1, C-l)
        else:
          C = max(0, C-l)

    if d == "R":
      if R not in rows:
        C = min(C+l, W-1)
      else:
        v = rows[R].gt(C)
        if v is not None:
          C = min(v-1, C+l, W-1)
        else:
          C = min(C+l, W-1)

    if d == "U":
      if C not in columns:
        R = max(0, R-l)
      else:
        v = columns[C].lt(R)
        if v is not None:
          R = max(0, v+1, R-l)
        else:
          R = max(0, R-l)

    if d == "D":
      if C not in columns:
        R = min(R+l, H-1)
      else:
        v = columns[C].gt(R)
        if v is not None:
          R = min(v-1, R+l, H-1)
        else:
          R = min(R+l, H-1)
    print(R+1, C+1)
   
resolve()
