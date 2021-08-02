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
        input = """4 2
2 3
3 5"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 1
3 4"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  # 1 回の操作はペアを作る操作になる。
  # 互いに素であれば良い？
  # Ai 個のグループになる。
  # 小さい順
  N, M = map(int, input().split(" "))
  Q = sorted([[int(x) for x in input().split(" ")] for _ in range(M)], key=lambda x: x[1])
  # 互いに素であればそれだけで答えになる。
  g = gcd(N, Q[0][0])
  if g == 1:
    print(Q[0][1]*(N-1))
    return

  count = [N-g]
  # g 個の間を埋める必要がある。
  for i in range(1, M):
    a, _ = Q[i]
    if gcd(g, a) == g: continue
    count.append(g-gcd(g, a))
    g = gcd(g, a)
    if g == 1:
      ans = 0
      count.sort(reverse=True)
      for j in range(len(count)):
        ans += count[j]*Q[j][1]
      print(ans)
      return
  print(-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()