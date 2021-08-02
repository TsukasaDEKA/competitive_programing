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
        input = """180"""
        output = """Yay!"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """200"""
        output = """:("""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """191"""
        output = """so-so"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())

  if (N*108)//100 < 206:
    print("Yay!")
  elif (N*108)//100 == 206:
    print("so-so")
  else:
    print(":(")

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
