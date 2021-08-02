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

#     def test_Sample_Input_1(self):
#         input = """4
# 0 3 0 0"""
#         output = """5.0644951022459797"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
0 1 2 3 4 5 0"""
        output = """10.3245553203367599"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
0 1 2 3 4 10 0"""
        output = """10.3245553203367599"""
        self.assertIO(input, output)

def resolve():
  from math import sqrt
  # 可能な限り平均をとる。
  # 曲線が最短？
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  if N == 2:
    print(1)
    return

  sum_A = sum(A)
  avr = sum_A//(N-2)
  dist = sum_A%(N-2)
  B = [avr for i in range(N)]
  B[0] = B[-1] = 0

  for i in range(2, 2+dist):
    B[i]+=1
  
  ans = 0
  for i in range(N-1):
    diff = B[i]-B[i+1]
    ans += sqrt(1+(diff**2))

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()