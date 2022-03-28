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
2 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
3 3 3"""
        output = """26"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
100"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10
90 52 56 71 44 8 13 30 57 84"""
        output = """58921"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  ans = 0
  for bit in range(1, 1<<N):
    temp = 1
    for i in range(N):
      if ((bit>>i)&1)^((A[i]+1)%2): temp*=2
    
    ans+=temp
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()