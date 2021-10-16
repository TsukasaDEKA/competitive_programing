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
        input = """mari
to
zzo
1321"""
        output = """marizzotomari"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """abra
cad
abra
123"""
        output = """abracadabra"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """a
b
c
1"""
        output = """a"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = [input() for _ in range(3)]
  T = [int(x)-1 for x in list(input())]
  ans = ""
  for t in T:
    ans += S[t]
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()