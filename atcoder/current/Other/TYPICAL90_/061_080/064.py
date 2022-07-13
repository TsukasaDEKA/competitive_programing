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
        input = """3 3
1 2 3
2 3 1
1 2 -1
1 3 2"""
        output = """3
4
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 10
61 51 92 -100 -89 -65 -89 -64 -74 7 87 -2 51 -39 -50 63 -23 36 74 37
2 2 -45
6 19 82
2 9 36
7 13 71
16 20 90
18 20 -24
14 17 -78
10 11 -55
7 19 -26
20 20 -7"""
        output = """1164
1328
1256
1350
1440
1416
1572
1482
1430
1437"""
        self.assertIO(input, output)


def resolve():
  # 全域を処理してると間に合わないので差分だけ管理することにする。
  # 地殻変動が発生する L ~ R の不便さは変動しない点に注意する。
  # 地殻変動のタイミングで境界部分だけ計算する。
  N, Q = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  diff = [A[i+1]-A[i] for i in range(N-1)]
  ans = sum([abs(x) for x in diff])

  for _ in range(Q):
    l, r, v = map(int, input().split(" "))
    l-=1
    r-=1
    if l > 0:
      new_diff = diff[l-1]+v
      ans+=abs(new_diff)-abs(diff[l-1])
      diff[l-1] = new_diff
    if r < N-1:
      new_diff = diff[r]-v
      ans+=abs(new_diff)-abs(diff[r])
      diff[r] = new_diff
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
