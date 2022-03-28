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
        input = """1"""
        output = """a
b
c"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2"""
        output = """aa
ab
ac
ba
bb
bc
ca
cb
cc"""
        self.assertIO(input, output)

def resolve():
  from itertools import product

  N = int(input())
  ans = []
  for tar in  product("abc", repeat=N):
    ans.append("".join(tar))
  print(*sorted(ans), sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()