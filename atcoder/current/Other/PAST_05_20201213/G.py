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
        input = """3 3
##.
.##
###"""
        output = """7
1 1
1 2
2 2
2 3
3 3
3 2
3 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 4
####
####
.#.."""
        output = """9
1 4
2 4
2 3
1 3
1 2
1 1
2 1
2 2
3 2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 3
.##
###
###"""
        output = """8
1 2
1 3
2 3
2 2
2 1
3 1
3 2
3 3"""
        self.assertIO(input, output)


def resolve():
  # 一筆書き経路を求める。
  # 全ての頂点から開始して一筆書きできる経路を見つけたら終わり。
  inf = 10**10+1
  H, W = map(int, input().split(" "))
  S = [list(input()) for _ in range(H)]

  # とりあえず経路長
  K = 0
  for h in range(H):
    for w in range(W):
      if S[h][w] == "#": K+=1

  

  print(K)

if __name__ == "__main__":
    unittest.main()
