import sys
from io import StringIO
from tabnanny import verbose
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
6 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
1 2 2 2 3 3 4 6 7 8"""
        output = """62"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  aggA = defaultdict(int)
  for i in range(N):
    aggA[A[i]] += 1
  max_A = max(A)

  ans = 0
  A_keys = sorted(list(set(A)))
  N = len(A_keys)
  for i in range(N):
    A_i = A_keys[i]
    if A_i**2 > max_A: break

    for j in range(i, N):
      A_j = A_keys[j]
      A_k = A_i*A_j
      if A_k > max_A: break
      if A_k not in aggA: continue
      
      len_i = aggA[A_i]
      len_j = aggA[A_j]
      len_k = aggA[A_k]

      temp = len_i * len_j * len_k
      if A_i != A_j:
        temp *= 2

      ans += temp
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()