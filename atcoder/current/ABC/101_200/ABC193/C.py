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
        input = """8"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100000"""
        output = """99634"""
        self.assertIO(input, output)

def resolve():
  # a**b と表せられる物を引く。
  N = int(input())
  count = 0
  checked = set()

  for i in range(2, int(-(-N**0.5//1))+1):
    temp = i*i
    while temp <= N:
      if temp not in checked:
        count+=1
      checked.add(temp)
      temp *= i

  ans = N - count
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
