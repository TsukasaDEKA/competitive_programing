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
        input = """1 4 3"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 6 4"""
        output = """6"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  A, B, C = map(int, input().split(" "))
  ans = 21-A-B-C

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
