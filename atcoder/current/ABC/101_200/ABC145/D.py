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
        input = """3 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """999999 999999"""
        output = """151840682"""
        self.assertIO(input, output)

def factorial_mod(r, mod):
  # R の階乗の結果の mod をとる
  ans = 1
  for n in range(2, r+1):
    ans*=n
    if ans>mod: ans%=mod
  return ans


def resolve():
  mod = 10**9+7
  X, Y = map(int, input().split(" "))
  # X、Yが共に 10**6 なのでO(XY)だと間に合わない。
  # X と Y は独立して考えることができる？できたら O(X+Y) で多分間に合う
  # A操作 = (+2, +1) と B操作 = (+1, +2) が何個取れるか計算して、それの取る順番が何通りあるか計算する。
  # A操作とB操作の個数をそれぞれ A, B と置くと、2A+B=X、A+2B=Y なので、連立方程式を解けば A, B が求まる。
  # パターンは O(1) でいける。<= いけなかった。
  if (2*X-Y)%3 != 0 or (2*Y-X)%3 != 0 or 2*Y-X < 0 or 2*X-Y < 0:
    print(0)
    return

  A = (2*X-Y)//3
  B = (2*Y-X)//3
  ans = 1
  for n in range(2, A+B+1):
    ans*=n
    if ans>mod: ans%=mod

  # 逆元をかける。 
  ans*=pow(factorial_mod(A, mod), mod-2, mod)
  ans*=pow(factorial_mod(B, mod), mod-2, mod)

  print(ans%mod)

resolve()

if __name__ == "__main__":
    unittest.main()
