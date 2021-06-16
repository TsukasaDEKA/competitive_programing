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

    def test_入力例_1(self):
        input = """5
RGBGB
GRGRB"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
RRR
BBB"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
BGGGRBBGRG
RGBBRGRGGG"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  # 三色しかないので、それで統計が取れそう。
  # 全てを計算する必要はない。
  N = int(input())
  CtN = {"R": 1, "G": 2, "B": 3}
  NtC = ["", "R", "G", "B"]
  S = [CtN[x] for x in list(input())]
  T = [CtN[x] for x in list(input())]

  R = [0]*N
  G = [0]*N
  B = [0]*N
  for i in range(N):
    R[i] = NtC[1^T[i]] if 1^T[i] else NtC[T[i]]
    G[i] = NtC[2^T[i]] if 2^T[i] else NtC[T[i]]
    B[i] = NtC[3^T[i]] if 3^T[i] else NtC[T[i]]

  print("", R, G, B, sep="\n")
import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
