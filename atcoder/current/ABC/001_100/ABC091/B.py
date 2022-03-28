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
        input = """3
apple
orange
apple
1
grape"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
apple
orange
apple
5
apple
apple
apple
apple
apple"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
voldemort
10
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6
red
red
blue
yellow
yellow
red
5
red
red
yellow
green
blue"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  inf = 10**18+1
  N = int(input())
  target = set()
  BLUE = defaultdict(int)
  for _ in range(N):
    s = input()
    target.add(s)
    BLUE[s]+=1

  M = int(input())
  RED = defaultdict(int)
  for _ in range(M):
    s = input()
    target.add(s)
    RED[s]+=1

  ans = 0
  for t in target:
    ans = max(ans, BLUE[t]-RED[t])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()