from os import sep
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
1 1 2 1 2"""
        output = """2
2
3
2
3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 2 3 4"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
3 3 3 3 3"""
        output = """6
6
6
6
6"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8
1 2 1 4 2 1 4 1"""
        output = """5
7
5
7
7
5
7
5"""
#         self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  agg = defaultdict(int)
  for a in A:
    agg[a]+=1
  
  pattern = 0
  for v in agg.values():
    pattern += v*(v-1)//2

  ans = [0]*N
  for i in range(N):
    ans[i] = pattern - (agg[A[i]]*(agg[A[i]]-1))//2 + ((agg[A[i]]-2)*(agg[A[i]]-1))//2
  print(*ans, sep="\n")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()