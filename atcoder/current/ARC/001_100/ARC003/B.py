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
        input = """5
chokudai
kensho
imos
yuichirw
ao"""
        output = """chokudai
ao
kensho
imos
yuichirw"""
        self.assertIO(input, output)

    def test_2(self):
        input = """2
dart
art"""
        output = """art
dart"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N = int(input())
  S = sorted([input()[::-1] for _ in range(N)])

  for s in S: print(s[::-1])

resolve()

if __name__ == "__main__":
    unittest.main()
