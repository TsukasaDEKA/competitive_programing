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
        input = """2"""
        output = """2.00000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3"""
        output = """4.50000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 確率 DP コンプガチャと一緒
  N = int(input())

  ans = N
  for i in range(2, N):
    ans += N/i
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()