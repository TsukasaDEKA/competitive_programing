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
        input = """25"""
        output = """17"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100"""
        output = """108"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2020"""
        output = """40812"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """200000"""
        output = """400000008"""
        self.assertIO(input, output)

def resolve():
  # N 以下の正の整数を集計する。二次元的に展開して、dist[i][j] = 先頭の数字が i で末尾の数字が j の個数。
  # sum(0<=i<=9, 0<=j<=9, dist[i][j]*dist[j][i]) でいけるはず。
  N = int(input())
  dist = [[0]*10 for _ in range(10)]

  for i in range(1, N+1):
    str_i = str(i)
    dist[int(str_i[0])][int(str_i[-1])]+=1
  ans=0
  for i in range(10):
    for j in range(10):
      ans += dist[i][j]*dist[j][i]
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
