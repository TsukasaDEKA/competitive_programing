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
        input = """5
1
2
1
2
2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
4
2
5
4
2
4"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
1
3
1
2
3
3
2"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  # 独立して使用できるペアとそうでないペアが存在する。
  # 12122 だと、例えば先に 212 の部分を実行した場合、
  # 121 の部分を実行することはできない。
  # 重なっている区間同士は同時に実行できない。
  # 重なっている区間かどうかを最初に集計する？
  # 隣接している石が同色だった場合、その区間は使っても使わなくても色が同じなので、
  # 一つにまとめることができる。
  # mod = 10**9+7 から考えると、幅優先探索すると時間が間に合わなさそう？
  # 
  mod = 10**9+7

  N = int(input())
  C = [int(input())-1 for _ in range(N)]


  print()

# resolve()

if __name__ == "__main__":
    unittest.main()
