import enum
import sys
from io import StringIO
from termios import B1800
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
        input = """5
1 2 3 4 5
1 2 2 4 3
7
1 1
2 2
2 3
3 3
4 4
4 5
5 5"""
        output = """Yes
Yes
Yes
No
No
Yes
No"""
        self.assertIO(input, output)


#     def test_Sample_Input_2(self):
#         input = """5
# 1 2 100 2 50
# 1 2 2 5 10000
# 1
# 5 5"""
#         output = """Yes"""
#         self.assertIO(input, output)

#     def test_Sample_Input_1(self):
#         input = """5
# 1 3 3 2 4
# 1 3 3 4 3"""
#         output = """"""
#         self.assertIO(input, output)

def resolve():
  from random import randint, seed
  from collections import defaultdict
  rand_min, rand_max = 10**2, 10**18
  N = int(input())
  seed(N)
  A = [int(x)-1 for x in input().split(" ")]
  B = [int(x)-1 for x in input().split(" ")]

  hash_table = defaultdict()
  used_hash = set()
  # 乱数に置き換える。
  for i in range(N):
    a = A[i]
    if a not in hash_table:
      hash_ = randint(rand_min, rand_max)
      while hash_ in used_hash:
        hash_ = randint(rand_min, rand_max)
      used_hash.add(hash_)
      hash_table[a] = hash_
    A[i] = hash_table[a]

  for i in range(N):
    b = B[i]
    if b not in hash_table:
      hash_ = randint(rand_min, rand_max)
      while hash_ in used_hash:
        hash_ = randint(rand_min, rand_max)
      used_hash.add(hash_)
      hash_table[b] = hash_
    
    B[i] = hash_table[b]
  
  # print(A)
  used = set([A[0]])
  for i in range(1, N):
    a = A[i]
    A[i] = A[i-1] if a in used else A[i-1]^A[i]
    used.add(a)
  # print(A)

  # print(B)
  used = set([B[0]])
  for i in range(1, N):
    b = B[i]
    B[i] = B[i-1] if b in used else B[i-1]^B[i]
    used.add(b)
  # print(B)
  for _ in range(int(input())):
    X, Y = [int(x)-1 for x in input().split(" ")]
    print("Yes" if A[X] == B[Y] else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()