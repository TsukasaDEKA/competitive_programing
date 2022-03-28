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
1 10 100"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 2 3 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
1 4 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2
1 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """6
2 7 1 8 2 8"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  N = int(input())
  A = [int(x) for x in input().split(" ")]
  agg = defaultdict(int)
  for a in A:
    if a%4==0:
      agg[4]+=1
    elif a%2==0:
      agg[2]+=1
    else:
      agg[0]+=1

  if agg[0] == 0:
    print("Yes")
    return
  if agg[2] == 0 and agg[4]+1 >= agg[0]:
    print("Yes")
    return
  if agg[4] >= agg[0]:
    print("Yes")
    return
  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()