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

    def test_1(self):
        input = """7 34"""
        output = """5"""
        self.assertIO(input, output)

    def test_2(self):
        input = """19 28"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  A, B = map(int, input().split(" "))
  last_10_deg_step = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 1]

  count = 0

  diff_b = abs(B - A)
  while diff_b != 0:
    if diff_b > 10:
      count += 1
      diff_b -= 10
    else:
      count += last_10_deg_step[diff_b]
      break
  print(count)

resolve()

if __name__ == "__main__":
    unittest.main()
