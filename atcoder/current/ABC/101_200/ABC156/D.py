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
        input = """4 1 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 141421 173205"""
        output = """34076506"""
        self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """100 20 10"""
    #     output = """"""
    #     self.assertIO(input, output)


# 高速な組み合わせ計算
# 
def comb(N, R, mod):
  ans = 1
  for n in range(N-R+1, N+1):
    ans*=n
    if ans > mod: ans%=mod

  for r in range(1, R+1):
    ans*=pow(r, mod-2, mod)
    if ans > mod: ans%=mod

  return ans

def resolve():
  mod = 10**9+7
  N, A, B = map(int, input().split(" "))

  # 全部の花束の種類から A 本で作る花束と B 本で作る花束の種類を除外する。
  all_pattern = pow(2, (N), mod)-1
  A_pattern = comb(N, A, mod)
  B_pattern = comb(N, B, mod)
  ans = int(all_pattern - A_pattern - B_pattern)

  # print(ans%mod, all_pattern, A_pattern, B_pattern)
  print(ans%mod)

resolve()

if __name__ == "__main__":
    unittest.main()
