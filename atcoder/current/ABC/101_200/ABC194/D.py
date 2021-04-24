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
        input = """2"""
        output = """2.00000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3"""
        output = """4.50000000000"""
        self.assertIO(input, output)

def resolve():
  # ガチャの DP と同じ
  N = int(input())
  ans = 0
  # 最初の 1 個が既に埋めてあるので、1 ~ N-1 までを計算する。N*(1+1/2+・・・+1/(N-1))
  for n in range(1, N): ans+=1/n
  print(ans*N)

# resolve()

if __name__ == "__main__":
    unittest.main()
