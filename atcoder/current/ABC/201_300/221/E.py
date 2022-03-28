import collections
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
1 2 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 2 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
3 2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10
198495780 28463047 859606611 212983738 946249513 789612890 782044670 700201033 367981604 302538501"""
        output = """830"""
        self.assertIO(input, output)


class BIT:
  def __init__(self, n):
    self.n = n
    self.data = [0]*(n+1)
    self.el = [0]*(n+1)

  def sum(self, i):
    s = 0
    while i > 0:
        s += self.data[i]
        i -= i & -i
    return s

  def add(self, i, x):
    # assert i > 0
    self.el[i] += x
    while i <= self.n:
        self.data[i] += x
        i += i & -i

  def get(self, i, j=None):
    if j is None:
        return self.el[i]
    return self.sum(j) - self.sum(i)

def resolve():
  from collections import defaultdict
  # 座標圧縮 BIT
  mod = 998244353
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  compA = sorted(list(set(A)))

  to_i = defaultdict(int)
  for i in range(len(compA)):
    to_i[compA[i]] = i

  ans = 0
  bit = BIT(len(compA))
  for i in range(N):
    index = to_i[A[i]]+1

    ans += pow(2, i, mod)*(bit.get(0, index) % mod)
    # print(bit.get(0, index))

    if ans >= mod: ans%=mod

    bit.add(index, pow(pow(2, mod-2, mod), i+1, mod))
  print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()