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

    def test_入力例_1(self):
        input = """100 4
30 40 120
30 40 30
30 40 1500
30 40 40"""
        output = """1660"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 4
13 15 31415
12 13 92653
29 33 58979
95 98 32384"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5000 5
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10000 20
4539 6002 485976
1819 5162 457795
1854 2246 487643
1023 4733 393530
1052 6274 289577
1874 2436 167747
1457 4248 452660
2103 4189 174955
3057 5061 319316
4898 4953 394627
1313 2880 154687
1274 1364 259598
3866 5844 233027
1163 5036 386223
1234 4630 155972
2845 4978 442858
3168 5368 171601
3708 4407 394899
3924 4122 428313
2112 4169 441976"""
        output = """2727026"""
        self.assertIO(input, output)

def resolve():
  # DP っぽいけどちょっと上限加減があるのでちょっと難しい？
  # 選んだ料理の内、L と R の累計が L <= W <= R の関係になっていれば作成できる。
  # 価値の高い順から愚直？
  # 香辛料 1 g あたりの価値が高い順に愚直？
  # N と W がまぁまぁ小さいので、 O(N*W) だったらできる。
  # dp[w][n] = n 番目までの料理を使って香辛料を丁度 w 使用する場合の価値の最大値
  # 全探索すると 2**500 とかになって間に合わない。
  # imos 的にできたりする？
  # 例1だと、1 番目をとる場合は 30 ~ 40 に + 120 する。2 番目をとる場合は 30 ~ 40 に + 30, 60 ~ 80 に  +30 する。
  # W 以上の部分に関しては考える必要が無い。
  W, N = map(int, input().split(" "))
  A = sorted([list(map(int, input().split(" "))) for _ in range(N)])
  dp = [[-1]*W for _ in range(N+1)]

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
