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
        input = """2 3 1"""
        output = """1.0000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 180707 0"""
        output = """0.0001807060"""
        self.assertIO(input, output)

def resolve():
  # 愚直にやっていったら間に合わないのでちょっと考える。
  # 美しさの総和を出して、それを n**m で割れば良さそう。
  # 美しさの総和を全て求める方法を考える。
  # 1桁目を 1 とした時、2桁目は 1+D だった場合のみ美しさが +1 される。
  # 2桁目が  1+D だった場合、3桁目が 1-D, 1+D だった場合のみ、美しさが +1
  # ・・・と繰り返していけば美しさの総和を O(1) で出せないか？
  # 美しさが 1 ~ M-1 までの数列をそれぞれ O(1) で出せても N  <= 10**9 なので間に合わない。
  # 
  N, M, D = map(int, input().split(" "))

  print(N)

# resolve()

if __name__ == "__main__":
    unittest.main()
