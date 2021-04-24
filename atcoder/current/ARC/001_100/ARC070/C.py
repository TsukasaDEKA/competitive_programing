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
        input = """6"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """11"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # カンガルーが家に辿りつくのが i = 1 の時だとすると、X = 1 になる。
  # カンガルーが家に辿りつくのが i = 2 の時だとすると、X = 2, 3 になる。(X = 1 の時、答えは i なので)
  # カンガルーが家に辿りつくのが i = 3 の時だとすると、X = 4, 5, 6 になる。
  # 「何もしない」ができるので、負の方向に進む必要がない。 1 秒間に進める範囲が i ずつ増えるので、X < i*(i+1)/2 になる最小の i を探す。
  # i の範囲は sqrt(maxX) <= 10**5 くらいなので間に合いそう。sqrt(2*X) から開始しても良さそう。
  X = int(input())

  for i in range(int(-(-(2*X)**0.5//1))-1, X+1):
    if i*(i+1)>=2*X:
      print(i)
      return

resolve()

if __name__ == "__main__":
    unittest.main()
