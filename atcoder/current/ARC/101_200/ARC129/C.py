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
        input = """2"""
        output = """142"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3"""
        output = """77"""
        self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """11"""
    #     output = """7777272"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """100"""
    #     output = """7777272"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """1000000"""
    #     output = """7777272"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_5(self):
    #     input = """983503"""
    #     output = """7777272"""
    #     self.assertIO(input, output)

debug = False
def resolve():
  from bisect import bisect_left

  N = int(input())
  table = [0, 1]
  for n in range(2, 1000):
    n_ = n+1
    combo = (table[-1]*n_)//(n_-2)
    table.append(combo)
    if combo >= N: break

  ans = ""
  n = N
  while n > 0:
    i = bisect_left(table, n)
    if len(table) == i: i-=1
    if table[i] > n: i-=1

    ans+="8"+("7"*i)+"6"
    n-=table[i]
  
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  # debug = True
  unittest.main()