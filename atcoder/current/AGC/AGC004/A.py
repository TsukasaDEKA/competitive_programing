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
        input = """3 3 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 3 5"""
        output = """15"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A = [int(x) for x in input().split(" ")]
  ans = min(A[0]*A[1]*((A[2]+1)//2-A[2]//2), A[1]*A[2]*((A[0]+1)//2-A[0]//2), A[2]*A[0]*((A[1]+1)//2-A[1]//2))
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()