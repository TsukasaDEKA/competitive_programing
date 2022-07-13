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
        input = """2 2"""
        output = """00
02
11
12
20
21"""
        self.assertIO(input, output)

def resolve():
  from itertools import product
  # 長さ L で文字の数が 3 種類の文字列は 3**L 種類である。
  # 大きい順から 3**(L-1) - N 個を除外対象にして N 個とってくる。
  inf = 10**18+1
  N, L = map(int, input().split(" "))
  ignore_N = 3**(L-1) - N
  temp = []

  count = 0
  for p in product(list(range(3))[::-1], repeat=L):
    count+=1
    if count <= ignore_N: continue
    temp.append(list(p))
    if len(temp) >= N: break
  
  ans = []
  for t in temp:
    ans.append("".join([str(x) for x in t]))
    for _ in range(2):
      for j in range(L):
        t[j] = (t[j]+1)%3
      ans.append("".join([str(x) for x in t]))
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()