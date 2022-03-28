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
        input = """4
1 3 5 2
2 3 1 4"""
        output = """1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 2 3
4 5 6"""
        output = """0
0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
4 8 1 7 9 5 6
3 5 1 7 8 2 6"""
        output = """3
2"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  dict_B = defaultdict(set)
  for i in range(N):
    dict_B[B[i]].add(i)

  ans_1 = 0
  ans_2 = 0
  for i in range(N):
    if A[i] == B[i]:
      ans_1 += 1
      ans_2 += len(dict_B[A[i]])-1
    else:
      ans_2 += len(dict_B[A[i]])


  print(ans_1, ans_2, sep="\n")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()