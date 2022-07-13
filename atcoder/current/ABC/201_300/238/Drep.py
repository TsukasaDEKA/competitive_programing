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
1 8
4 2"""
        output = """Yes
No"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
201408139683277485 381410962404666524
360288799186493714 788806911317182736
18999951915747344 451273909320288229
962424162689761932 1097438793187620758"""
        output = """No
Yes
Yes
No"""
        self.assertIO(input, output)

def resolve():
  T = int(input())
  for _ in range(T):
    A, S = map(int, input().split(" "))
    # A の方の x と y は両方 1 である必要がある。=> S >= 2*A でないといけない。
    val = S-2*A
    if val < 0:
      print("No")
      continue
    if A&val:
      print("No")
      continue
    print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()