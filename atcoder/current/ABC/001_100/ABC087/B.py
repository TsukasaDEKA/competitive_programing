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
        input = """2
2
2
100"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1
0
150"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """30
40
50
6000"""
        output = """213"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A = int(input())
  B = int(input())
  C = int(input())
  X = int(input())
  ans = 0
  for a in range(A+1):
    for b in range(B+1):
      for c in range(C+1):
        if 500*a+100*b+50*c == X:
          ans+=1

  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()