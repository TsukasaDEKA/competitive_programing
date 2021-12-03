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
        input = """1 2
10 10
12 4"""
        output = """1"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """100 1
# 101 101
# 102 1"""
#         output = """infinity"""
#         self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """12000 15700
3390000000 3810000000
5550000000 2130000000"""
        output = """113"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  # A を 0 に固定して、B が相対的にどのように動くか観測する。
  # 最大で 10**10 回程度のループになるので、TLE する。
  inf = 10**18+1
  T = [int(x) for x in input().split(" ")]
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  if A[0]*T[0] + A[1]*T[1] == B[0]*T[0] + B[1]*T[1]:
    print("infinity")
    return

  g = gcd(*T)
  T[0], T[1] = T[0]//g, T[1]//g

  # B の方が常に遠くにいるようにしておく。
  if A[0]*T[0] + A[1]*T[1] > B[0]*T[0] + B[1]*T[1]: A, B = B, A

  diff = [(B[0]-A[0])*T[0], (B[1]-A[1])*T[1]]
  if diff[0] > 0:
    print(0)
    return

  # diff[0] が初期値
  # 折り返しのタイミングで 1 回しかカウントできなかったりとか色々めんどくさい。
  ans = 2*((-diff[0])//(diff[1]+diff[0]))+1
  if diff[0]%(diff[1]+diff[0])==0:
    ans-=1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()