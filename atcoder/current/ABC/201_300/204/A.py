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
        input = """0 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  X = set([int(x) for x in input().split(" ")])

  if len(list(X))==1:
    print(list(X)[0])
    return

  for i in range(3):
    if i not in X:
      print(i)
      return

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
