
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

    def test_入力例_1(self):
        input = """5 3"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """99999 1000000000000000000"""
        output = """84563"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """0 1000000000000000000"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # K <= 10**18 なのでシミュレーションは TLE する。
  # mod 10**5 内での単調増加
  # 同じ数字が出てきたら、そこからはずっと一緒。
  # 鳩の巣原理から、必ず 10**5 回の操作を行うまでに同じ数字が出てくる。
  # 10**5 の長さの配列 "step" を準備して step[i] : i が何手目で出てきたか？というように記録していくことで楽に実装できる。
  # (K- step[i])%(ループ 1 週分の長さ) 回の操作を継続すると答えが出る。
  # 途中で 0 が出てきたらそこで計算を ~~打ち切る。~~ 打ち切らなくていい。
  # 打ち切らなくてもループ 1 週分の長さが 1 になるので残りの手数は 0 回になって正しい答えが出る。
  MOD = 10**5
  N, K = map(int, input().split(" "))
  step = [-1]*MOD
  step[N] = 0

  ans = N
  count = 0
  while count < K:
    # 操作をシミュレート
    count+=1
    ans = (ans + sum(map(int, str(ans))))%MOD
    if step[ans] >= 0:
      # ループが見つかったら、残りの操作回数を計算してリセットする。
      K = (K-count)%(count-step[ans])
      count = 0
      step = [-1]*MOD
    step[ans] = count

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
