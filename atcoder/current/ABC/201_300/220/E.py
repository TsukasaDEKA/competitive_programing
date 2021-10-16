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
        input = """3 2"""
        output = """14"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """14142 17320"""
        output = """11284501"""
        self.assertIO(input, output)

def resolve():
  # D == 1 の時、明らかに 2**N-2
  # D == 2 の時、
  mod = 998244353
  inf = 10**18+1
  N, D = map(int, input().split(" "))


  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()