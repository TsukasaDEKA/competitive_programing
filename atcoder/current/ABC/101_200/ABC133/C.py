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
        input = """2020 2040"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 5"""
        output = """20"""
        self.assertIO(input, output)

def resolve():
  mod = 2019

  L, R = map(int, input().split(" "))
  if R-L+1 >= 2019:
    print(0)
    return
  
  ans = 2020
  for i in range(L, R):
    i_ = i%mod
    for j in range(i+1, R+1):
      j %= mod
      temp = (i_*j)%mod
      if temp < ans:
        ans = temp
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()