import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """6
1 3 -4 2 2 -2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
1 -1 1 -1 1 -1 1"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
1 -2 3 -4 5"""
        output = """0"""
        self.assertIO(input, output)

from collections import Counter

def resolve():
  # 累積和を取って同じ値の個数を数えて、同じ値の組み合わせの個数 (同じ値が N 個あるなら N*(N-1)//2パターン) を数える。
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  integral_A = [0]*(N+1)
  for i in range(N):
    integral_A[i+1] = integral_A[i]+A[i]

  collectionA = Counter(integral_A)
  ans = 0
  for key, value in collectionA.items():
    ans += (value*(value-1))//2

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
