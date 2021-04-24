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
        input = """127"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """44852"""
        output = """16"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """14"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
  # N < 100000 なので、探索範囲は狭い。
  # N = A*9 + B*6 + C で全探索して、A と B をそれぞれ 9, 6 進数表記に直した時の係数の合計最小値を求めれば良い。
  # 例 : 40*6 = 1*6**3+4*6 で 5 回
  # A は 0 ~ 11111、B は 0 ~ 16666 なので 185175926 < 10**9 で・・・間に合わない・・・・？
  # A を決めたら手順が最小になる B は自動的に求まるので、 B をループする必要はない。11112 回の計算なので間に合う
  inf = 10**10+1
  N = int(input())
  ans = inf
  for A in range(N//9+1):
    B=(N-A*9)//6
    C=N-A*9-B*6
    temp_ans = C
    for n in reversed(range(1, 5)):
      temp_ans+=A//9**n
      A%=9**n
    temp_ans+=A

    for n in reversed(range(1, 6)):
      temp_ans+=B//6**n
      B%=6**n
    temp_ans+=B
    ans=min(ans, temp_ans)
  print(ans)

resolve()


if __name__ == "__main__":
    unittest.main()
