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

    def test_Sample_Input_1(self):
        input = """2
1
2"""
        output = """first"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
100000
30000
20000"""
        output = """second"""
        self.assertIO(input, output)

def resolve():
  # ai <= 10**9 なので、素直にシミュレートすると間に合わない。
  # どちらも「1 種類のリンゴを 2 個残したい」と考える。 (結果的に全ての種類が 1 個になると、次の相手の番で終わってしまう。)
  # [1, 2] みたいな状況で手番が回ってきたら勝ち。[0, 2] にして相手に回したら [0, 1]で返ってくるので
  # [1, 3] でも勝ち。[0, 2] にして相手に回したら [0, 1]で返ってくるので
  # まとめると残り一種類にできる状況で手番がきたら勝ち。(ラストの一種類を偶数にして相手に手番を渡せば良い。)
  # 考察を進めると「全てが偶数個で手番が回ってきたら負け」
  # 相手は常にこちらの手番の時に各種類リンゴが偶数個になるように振る舞えるので、最終的に 「1 種類のリンゴを 2 個残す」という勝利条件を満たせる。
  N = int(input())
  A = [int(input()) for _ in range(N)]
  for a in A:
    if a%2:
      print("first")
      return

  print("second")

resolve()

if __name__ == "__main__":
    unittest.main()
