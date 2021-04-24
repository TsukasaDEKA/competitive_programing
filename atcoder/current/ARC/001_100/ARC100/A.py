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
0 2 3 3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9
1 2 3 4 5 6 7 8 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
6 5 4 3 2 1"""
        output = """18"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7
1 1 1 1 2 3 4"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  # 一旦 A[i] - i + 1 を計算する。
  for i in range(N): A[i]-=i+1
  A.sort()
  # 中央値を b とする。
  if len(A)%2:
    b=A[len(A)//2]
  else:
    center = len(A)//2
    b=round((A[center]+A[center-1])//2)

  # 答え
  ans = 0
  for i in range(N):ans += abs(A[i]-b)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
