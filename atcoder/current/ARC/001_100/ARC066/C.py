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
2 4 4 0 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
6 4 0 2 4 0 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
7 5 1 1 7 3 5 3"""
        output = """16"""
        self.assertIO(input, output)

from collections import Counter

def resolve():
  mod = 10**9+7
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  # N だけ聞けば組み合わせの個数はわかるので、0 を出力するかどうかを判定して、最後にそれを出力する。
  # 人数が奇数の場合、0 の出現が必ず 1 になる。 
  count = Counter(A)
  if N%2 and count[0] != 1:
      print(0)
      return

  # 人数が奇数の場合、0 の出現が 1 で、それ以降の偶数が N-1 まで 2 人ずつ存在する。
  # 人数が偶数の場合、N-1 までの奇数が 2 人ずつ存在する。
  for n in range(N%2+1, N, 2):
    if count[n] != 2:
      print(0)
      return

  # 全員が正しい情報を記憶していた場合。
  print(pow(2, N//2, mod))

resolve()

if __name__ == "__main__":
    unittest.main()
