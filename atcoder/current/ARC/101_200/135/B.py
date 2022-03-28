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
        input = """5
6 9 6 6 5"""
        output = """Yes
0 4 2 3 1 2 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
0 1 2 1 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
10"""
        output = """Yes
0 0 10"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = [int(x) for x in input().split(" ")]
  X = [0, 0]
  for i in range(N):
    X.append(S[i]-X[-2]-X[-1])
  
  a = -1*min(X[0::3])
  b = -1*min(X[1::3])
  if min(X[2::3]) - a - b < 0:
    print("No")
    return
  
  ans = []
  for i in range(N+2):
    if i%3 == 0: ans.append(X[i]+a)
    if i%3 == 1: ans.append(X[i]+b)
    if i%3 == 2: ans.append(X[i]-a-b)
  print("Yes")
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()