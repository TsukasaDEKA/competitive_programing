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
10 20 39"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
666 777 888 777 666"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  S = [int(x) for x in input().split(" ")]

  ops = set()
  for a in range(1, 200):
    for b in range(1, 200):
      ops.add(4*a*b+3*a+3*b)

  ans = 0
  for i in range(N):
    if S[i] not in ops:
      ans+=1
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()