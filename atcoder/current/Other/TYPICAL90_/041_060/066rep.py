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
        input = """2
1 2
1 2"""
        output = """0.250000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
3 3
1 1
4 4"""
        output = """1.000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
1 10
38 40
8 87
2 9
75 100
45 50
89 92
27 77
23 88
62 81"""
        output = """13.696758921226"""
        self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """3
# 2 4
# 3 5
# 2 4"""
#         output = """13.696758921226"""
#         self.assertIO(input, output)

def resolve():
  N = int(input())
  L_R = [[int(x) for x in input().split(" ")] for _ in range(N)]
  total_pattern = 1
  for i in range(N):
    l, r = L_R[i]
    total_pattern*=(r-l+1)

  turn = 0
  for i in range(N):
    l, r = L_R[i]
    pattern = total_pattern//(r-l+1)
    for k in range(l, r+1):
      for j in range(i):
        l_, r_ = L_R[j]
        pattern //= (r_-l_+1)
        turn += max(0, r_-max(k+1, l_)+1)*pattern
        pattern *= (r_-l_+1)

  print(turn/total_pattern)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()