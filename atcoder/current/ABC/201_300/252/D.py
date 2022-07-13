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
        input = """4
3 1 4 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
99999 99998 99997 99996 99995 99994 99993 99992 99991 99990"""
        output = """120"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """15
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9"""
        output = """355"""
        self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """9
# 1 1 1 2 2 2 3 3 3"""
#         output = """27"""
#         self.assertIO(input, output)

def resolve():
  from collections import Counter
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  agg = Counter(A)
  values = list(agg.values())

  ans = 0
  count = values[0]
  for i in range(1, len(values)-1):
    ans += count*values[i]*(N-count-values[i])
    count+=values[i]
  
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()