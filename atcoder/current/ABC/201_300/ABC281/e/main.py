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
  inf = 10**18+1
  N, M, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")] + [inf]

  sms = SortedMultiset([])
  for i in range(M):
    sms.add(A[i])

  val = 0
  for i in range(K):
    val += sms[i]

  ans = []
  for i in range(N-M+1):
    # print(sms)
    ans.append(val)
    a = A[i]
    if sms.index_right(a) <= K:
      val -= a
      if len(sms) >= K+1:
        val += sms[K]

    sms.discard(a)

    new_a = A[i+M]

    sms.add(new_a)
    # print(a, new_a, sms.index_right(new_a))
    if sms.index_right(new_a) <= K:
      val += new_a
      if len(sms) >= K+1:
        val -= sms[K]
  print(*ans)

resolve()
