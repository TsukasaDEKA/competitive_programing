import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """0"""
        output = """1371"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3"""
        output = """722502"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10"""
        output = """1111355571"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  t = int(input())
  def f(t):
    return t**2+2*t+3

  print(f(f(f(t)+t)+f(f(t))))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()