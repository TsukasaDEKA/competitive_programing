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
        input = """5
1 3 3 3 3
3 3 2 2 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 1 1 2 2
3 2 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
1 3776 3776 8848 8848 8848 8848 8848 8848 8848
8848 8848 8848 8848 8848 8848 8848 8848 3776 5"""
        output = """884111967"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1
17
17"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 条件分岐がめんどくさそう。
  # 左右それぞれから見た時に固定、以下が考えられて、
  inf = 10**18+1
  mod = 10**9+7
  N = int(input())
  T = [int(x) for x in input().split(" ")]
  A = [int(x) for x in input().split(" ")]
  l2r_lt = [0]*N
  l2r_fixed = [0]*N
  l2r_fixed[0] = T[0]
  r2l_lt = [0]*N
  r2l_fixed = [0]*N
  r2l_fixed[-1] = A[-1]

  for i in range(N-1):
    if T[i+1] != T[i]:
      l2r_fixed[i+1] = T[i+1]
    else:
      l2r_lt[i+1] = T[i+1]

    j = N-1-i
    if A[j-1] != A[j]:
      r2l_fixed[j-1] = A[j-1]
    else:
      r2l_lt[j-1] = A[j-1]
  
  ans = 1
  for i in range(N):
    # ダメパターンを列挙していく。
    # 両方 fixed で一致しない。
    if l2r_fixed[i] and r2l_fixed[i]:
      if l2r_fixed[i] != r2l_fixed[i]:
        print(0)
        return
      # 一致してる場合は ans はそのまま
      continue

    if l2r_lt[i] and r2l_lt[i]:
      ans *= min(l2r_lt[i], r2l_lt[i])
      if ans >= mod: ans %= mod
      continue

    if l2r_lt[i] < r2l_fixed[i]:
      print(0)
      return
    
    if r2l_lt[i] < l2r_fixed[i]:
      print(0)
      return
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()