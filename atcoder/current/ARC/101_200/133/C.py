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
        input = """2 4 3
0 2
1 2 2 0"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 4
0 1 2
1 2 3"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  # できるだけ K - 1 を置きたい。
  inf = 10**18+1
  H, W, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]

  # 全てのマス目の総和%K は同じ。
  # なので、sum(A)%K と sum(B)%K は一致している必要がある。
  if sum(A)%K != sum(B)%K:
    print(-1)
    return

  # sum(A)%K == sum(B)%K の場合について考える。
  # 一旦全てのマス目に K-1 を置いた場合、一行分のマス目の数の和は (K-1)*W となる。
  # そこから A[i] を満たすように数を減らす場合、

  # 1 行の総和の最大値
  A_base = ((K-1)*W)%K
  # それぞれの行からいくつ減らせば Ai に一致させることができるかを考える。
  C = sum((A_base-a)%K for a in A)

  # 列でも上記と同じことをする。
  B_base = ((K-1)*H)%K
  D = sum((B_base-b)%K for b in B)

  ans = (K-1)*(H*W) - max(C, D)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()