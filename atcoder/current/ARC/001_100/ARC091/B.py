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
        input = """5 2"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 0"""
        output = """100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """31415 9265"""
        output = """287927211"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  # b > K and b <= N で。、a は a >= K and a <= N になる。
  # また、 b を定めた時の a の個数は、(b-K)*((N//b)+max(0, N%b-K+1) で求まる。
  # b を K < b <= N の間で動かすので、O(N-K)
  # バグらせて訳わからんくなった。
  ans = 0
  for b in range(K+1, N+1):
    temp=(b-K)*(N//b) + max(0, N%b-K+1)
    if K==0: temp-=1
    ans+=temp
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
