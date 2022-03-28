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
        input = """2 2 2"""
        output = """7"""
        self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """3 3 10"""
    #     output = """7"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """1 1 100"""
    #     output = """100"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """31415 92653 58979"""
    #     output = """469486242"""
    #     self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """200000 200000 200000"""
        output = """469486242"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  # A の最大値が 3 の時、B に 2 以下の数字が含まれているのは矛盾 (B は全て 3 以上)
  # A に 3 が含まれている時、B が全て 3 以上であれば、それ以外は自由？？？？
  # A の最大値固定 (B の最小値固定)で計算？
  # 軸に対する自由度的な奴を考えないといけないっぽい
  # 単純に A の最大値を固定しちゃうと A のカウントが重複しちゃうので、固定するときはそれぞれ重複ぶんを削除する。
  N, M, K = map(int, input().split(" "))
  if N == 1 or M == 1:
    print(pow(K, N*M, mod))
    return
  A_p = [pow(a, N, mod) for a in range(K+1)]

  ans = 0
  for max_a in range(1, K+1):
    A = (A_p[max_a] - A_p[max_a-1])%mod
    B = pow(K-max_a+1, M, mod)
    ans += (A*B)%mod
    if ans >= mod: ans %= mod
  print(ans%mod)
 
# resolve()

if __name__ == "__main__":
    unittest.main()
