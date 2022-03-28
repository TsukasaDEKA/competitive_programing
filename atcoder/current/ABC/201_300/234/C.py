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
        input = """3"""
        output = """22"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """11"""
        output = """2022"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """923423423420220108"""
        output = """220022020000202020002022022000002020002222002200002022002200"""
        self.assertIO(input, output)

def resolve():
  K = int(input())
  ans = []
  while K > 0:
    if K%2:
      ans.append("2")
    else:
      ans.append("0")
    K//=2
  print("".join(ans[::-1]))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()