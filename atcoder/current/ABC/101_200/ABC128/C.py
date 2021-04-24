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
        input = """2 2
2 1 2
1 2
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 3
2 1 2
1 1
1 2
0 0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 2
3 1 2 5
2 2 3
1 0"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  # 貪欲でいける？
  # N <= 10 なので、スイッチの状態の組み合わせパターンは最大で 2**10 = 1024 しかない。
  # M は 10 以下。
  # 全てのスイッチの状態で全ての電球が点灯するかどうかを確認してみる。
  # 計算量は O((2**N)*M) なので多分間に合う。
  N, M = map(int, input().split(" "))
  k_s = [[int(x) for x in input().split(" ")] for _ in range(M)]
  P = [int(x) for x in input().split(" ")]

  ans = 0
  for i in range(2**N):
    is_correct = True
    for m in range(M):
      target_switches = 0
      for s in k_s[m][1:]: target_switches+=(1<<(s-1))
      # and マスクする。
      if bin(i&target_switches).count("1")%2 != P[m]:
        # 点灯していないランプを見つけたら break する。
        is_correct = False
        break
    if is_correct: ans+=1

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
