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
        input = """1 2
2 1
12 14 8 2"""
        output = """6 4 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
100 1
10000 0 -1"""
        output = """100 -1"""
        self.assertIO(input, output)

def resolve():
  # 順番に計算していけば求めることはできる。
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  C = [int(x) for x in input().split(" ")]
  B = [inf]*(M+1)

  # 前からやってみる。（この時点では未確定の場合がある。）
  for c in range(N+M+1):
    c_val = C[c]
    for b in range(min(c+1, M+1)):
      for a in range(min(c, N), -1, -1):
        if a+b == c and B[b] != inf:
          c_val -= A[a]*B[b]
        elif a+b == c and B[b] == inf and A[a]:
          B[b] = c_val//A[a]

  for c in range(N+M+1):
    c_val = C[c]
    for b in range(min(c+1, M+1)):
      for a in range(min(c, N), -1, -1):
        if a+b == c and B[b] != inf:
          c_val -= A[a]*B[b]
        elif a+b == c and B[b] == inf:
          if A[a]:
            B[b] = c_val//A[a]
          else:
            B[b] = c_val

  print(*B)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()