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
        input = """yx
axy"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """ratcode
atlas"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """cd
abc"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """w
ww"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """zzz
zzz"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1

  S = "".join(sorted(list(input())))
  T = "".join(sorted(list(input()), reverse=True))
  print("Yes" if S < T else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()