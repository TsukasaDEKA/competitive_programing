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
        input = """12"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """963761198400"""
        output = """1920"""
        self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """24"""
    #     output = """4"""
    #     self.assertIO(input, output)
def resolve():
  def make_odd_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
      if n % i == 0:
        if i%2: lower_divisors.append(i)
        if i != n // i and (n // i)%2:
          upper_divisors.append(n//i)
      i += 1
    return lower_divisors + upper_divisors[::-1]
  # 平均 a で長さ l 数列を考えた時、a*l = N になるものを考える。
  # l が偶数の時、a は必ず x + 0.5 の形になる。(x は自然数)
  # l が奇数の時、a は必ず整数になる。

  N = int(input())
  print(len(make_odd_divisors(N)*2))
  
resolve()

if __name__ == "__main__":
    unittest.main()
