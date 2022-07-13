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
        input = """4 3 3 6 2 5 10"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 1 4 1 5 9 2"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1 1 1 1 1 1"""
        output = """Draw"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A,B,C,D,E,F,X = map(int, input().split(" "))

  t = (X//(A+C))*(A*B) + min(X%(A+C), A)*B
  a = (X//(D+F))*(D*E) + min(X%(D+F), D)*E
  if t > a:
    print("Takahashi")
  elif t < a:
    print("Aoki")
  else:
    print("Draw")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()