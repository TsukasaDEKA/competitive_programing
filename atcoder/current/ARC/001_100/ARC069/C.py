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
        input = """1 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """12345 678901"""
        output = """175897"""
        self.assertIO(input, output)

def resolve():
  # 優先的に S を使っていく。
  S, C = map(int, input().split(" "))
  ans = 0
  temp = min(S, C//2)
  S -= temp
  C -= 2*temp
  ans += temp
  ans += C//4

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()