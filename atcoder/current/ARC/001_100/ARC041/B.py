import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """3 3
010
101
010"""
        output = """000
010
000"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 4
0230
2323
0230"""
        output = """0000
0230
0000"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5 5
00100
03040
20903
05060
00300"""
        output = """00000
00100
02030
00300
00000"""
        self.assertIO(input, output)

def resolve():
  inf = 10
  dn = [-1, 0, 1, 0]
  dm = [0, -1, 0, 1]

  N, M = map(int, input().split(" "))
  B = [[int(x) for x in list(input())] for _ in range(N)]

  ans = [[0]*M for _ in range(N)]
  for n in range(1, N-1):
    for m in range(1, M-1):
      min_amoeba = inf
      for i in range(4):
        n_ = n + dn[i]
        m_ = m + dm[i]
        min_amoeba = min(min_amoeba, B[n_][m_])
      ans[n][m] = min_amoeba
      for i in range(4):
        n_ = n + dn[i]
        m_ = m + dm[i]
        B[n_][m_] -= min_amoeba
      

  for a in ans:
    print(*a, sep="")

resolve()

if __name__ == "__main__":
    unittest.main()
