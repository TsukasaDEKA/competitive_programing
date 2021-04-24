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
        input = """3 2"""
        output = """0"""
        self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """45108 2571593"""
    #     output = """224219544"""
    #     self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 100"""
        output = """224219544"""
        self.assertIO(input, output)

def resolve():
  def comb(N, R, mod):
    ans = 1
    for n in range(N-R+1, N+1):
      ans*=n
      if ans > mod: ans%=mod

    for r in range(1, R+1):
      ans*=pow(r, mod-2, mod)
      if ans > mod: ans%=mod

    return ans

  mod = 10**9+7
  # 和なので厄介。
  # 長さ N の、和が P の倍数になる数列の個数を考えて、(P-1)**n から引く。

  N, P = map(int, input().split(" "))

  dist = 0

  # print(dist)
  ans = (pow(P-1, N, mod) - dist)%mod

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
