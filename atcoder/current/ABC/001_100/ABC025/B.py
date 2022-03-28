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
        input = """3 5 10
East 7
West 3
West 11"""
        output = """West 8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 8
West 6
East 3
East 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 25 25
East 1
East 1
West 1
East 100
West 1"""
        output = """East 25"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, A, B = map(int, input().split(" "))
  current = 0
  for _ in range(N):
    s, d = input().split(" ")
    d = max(A, min(B, int(d)))
    if s == "West": d *= -1
    current+=d
  
  if current == 0:
    print(0)
    return
  if current > 0:
    print("East", current)
  else:
    print("West", -current)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()