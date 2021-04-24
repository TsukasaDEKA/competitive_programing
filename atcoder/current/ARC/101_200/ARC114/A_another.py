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
4 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
47"""
        output = """47"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
3 4 6 7 8 9 10"""
        output = """42"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1
8"""
        output = """2"""
        self.assertIO(input, output)




def resolve():
  inf = 10**18+1

  from math import gcd
  primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
  N = int(input())
  X = [int(x) for x in input().split(" ")]

  ans = inf
  for i in range(1, 2**15):
    facts = 1
    for j in range(15):
      if ((i>>j)&1): facts *= primes[j]

    # print(facts)
    is_ans = True
    for x in X:
      if gcd(facts, x)==1:
        is_ans = False
        break

    if is_ans: ans = min(ans, facts)
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
