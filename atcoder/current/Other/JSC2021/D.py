import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """45108 2571593"""
        output = """224219544"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  N, P = map(int, input().split(" "))
  ans = P-1
  ans *= pow(P-2, N-1, mod)

  print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
