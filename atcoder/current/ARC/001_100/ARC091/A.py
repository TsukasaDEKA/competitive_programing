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
        input = """2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """314 1592"""
        output = """496080"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  N, M = min(N, M), max(N,M)
  
  if N == 2:
    print(0)
    return
  if N == 1:
    if M == 1:
      print(1)
    else:
      print(M-2)
    return

  print((N-2)*(M-2))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()