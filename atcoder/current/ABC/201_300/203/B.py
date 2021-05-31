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
        input = """1 2"""
        output = """203"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3"""
        output = """1818"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  N, K = map(int, input().split(" "))

  ans = 0
  for i in range(1, N+1):
    for j in range(1, K+1):
      ans += i*100 + j
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
