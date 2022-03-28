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
        input = """42"""
        output = """Not Prime"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """49"""
        output = """Prime"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3"""
        output = """Prime"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1000000000"""
        output = """Not Prime"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """1"""
        output = """Not Prime"""
        self.assertIO(input, output)

def resolve():
  def count_fact(n):
    count = 0
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
      if temp%i==0:
        cnt=0
        while temp%i==0:
          cnt+=1
          temp //= i
        count+=cnt
    if temp!=1: count+=1
    return max(1, count)

  N = int(input())
  if N == 1:
    print("Not Prime")
    return
  if count_fact(N) == 1:
    print("Prime")
    return

  if (N%10)%2 != 0 and (N%10) != 5:
    sum_ = 0
    n = N
    while n > 0:
      sum_+=n%10
      n//=10
    if sum_%3:
      print("Prime")
      return
  print("Not Prime")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()