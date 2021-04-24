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
4 8"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
4 2 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4
-100 -100 -100 -100"""
        output = """0"""
        self.assertIO(input, output)

from statistics import mean

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  # 平均
  mean_A = round(mean(A))
  ans = 0
  for a in A: ans += (a-mean_A)**2

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
