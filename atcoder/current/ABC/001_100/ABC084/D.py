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
        input = """1
3 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
13 13
7 11
7 11
2017 2017"""
        output = """1
0
0
1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
1 53
13 91
37 55
19 51
73 91
13 49"""
        output = """4
4
1
1
1
2"""
        self.assertIO(input, output)

def resolve():
  # 最初に (2 ~ 10**5) の範囲で 「2017 に似た数」の累積和(integral_2017_like) を作って、
  # integral_2017_like[r] - integral_2017_like[l-1]を求める。
  # 計算量は N=10**5 O(log(N) + N + Q) なので間に合う
  Q = int(input())

  N = 10**5

  # 素数対応表
  prime_numbers = [True]*(N+1)
  prime_numbers[0] = prime_numbers[1] = False
  to = int(-(-N**0.5//1))
  for i in range(2, to+1):
    if not prime_numbers[i]: continue
    target = 2*i
    while target <= N:
      prime_numbers[target] = False
      target+=i

  # 「2017 に似た数」の累積和
  integral_2017_like = [0]*(N+2)
  for i in range(2, N+1):
    integral_2017_like[i] = integral_2017_like[i-1]
    if i%2 and prime_numbers[i] and prime_numbers[(i+1)//2]:
      integral_2017_like[i] += 1

  # クエリから答えを出す。
  for _ in range(Q):
    l, r = map(int, input().split(" "))
    print(integral_2017_like[r]-integral_2017_like[l-1])
# resolve()


if __name__ == "__main__":
    unittest.main()
