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
        input = """15"""
        output = """192"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100"""
        output = """824552442"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10000000000000000"""
        output = """824552442"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  mod = 998244353
  cache = defaultdict(int)
  X = int(input())
  def f(x):
    if x <= 4:
      return x
    else:
      if cache[x//2] == 0:
        cache[x//2] = f(x//2)%mod
      if cache[(x+1)//2] == 0:
        cache[(x+1)//2] = f((x+1)//2)%mod
      return (cache[x//2]*cache[(x+1)//2])%mod
  
  print(f(X))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()