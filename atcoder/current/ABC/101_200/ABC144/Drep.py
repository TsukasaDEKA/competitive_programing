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
        input = """2 2 4"""
        output = """45.0000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """12 21 10"""
        output = """89.7834636934"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 1 8"""
        output = """4.2363947991"""
        self.assertIO(input, output)

def resolve():
  from math import degrees, atan

  inf = 10**18+1
  a, b, x = map(int, input().split(" "))
  x /= a
  if x <= (a*b/2):
    y = 2*x/b
    print(degrees(atan(b/y)))
  else:
    y = (2*x)/a-b
    print(degrees(atan((b-y)/a)))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()