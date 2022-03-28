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
        input = """4
1
3
2
4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
3
2
5
1
4
6"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
6
3
1
2
7
4
8
5"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  # 最長の連続した部分数列の個数
  inf = 10**18+1
  N = int(input())
  P = [int(input())-1 for _ in range(N)]
  # i:P を逆転させて単調増加する最大区間を求める。
  revP = [0]*N
  for i in range(N):
    revP[P[i]] = i

  count = 1
  ans = 1
  for i in range(1, N):
    if revP[i-1] < revP[i]: count += 1
    else: count = 1
    ans = max(ans, count)
  print(N-ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()