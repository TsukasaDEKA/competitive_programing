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
        input = """10 1"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5"""
        output = """171"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1000000000"""
        output = """100999999999"""
        self.assertIO(input, output)

def resolve():
  # t の倍数による周期性がある。
  # a が 100 変化する毎に周期性がある。
  t, N = map(int, input().split(" "))

  A = (N//t)*100+(100*(N%t)+t-1)//t
  print(((100+t)*A)//100-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
