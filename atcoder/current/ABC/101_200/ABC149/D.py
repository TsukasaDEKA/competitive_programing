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
        input = """5 2
8 7 6
rsrpr"""
        output = """27"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 1
100 10 1
ssssppr"""
        output = """211"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr"""
        output = """4996"""
        self.assertIO(input, output)

def resolve():
  # ちょうど K 回前のじゃんけんで出した手と同じ手を出すことはできないという点に注意。
  # 負け or あいこ を選ぶ時に、K 個先の手が負けないように選ぶべき。
  # K 個前が同じ手で、 K 個先が同じ手ならばスコアを足さなければ良い。(T[i] を適当に書き換える)
  N, K = map(int, input().split(" "))
  R, S, P = map(int, input().split(" "))
  score = {
    "r": P,
    "s": R,
    "p": S
  }
  T = list(input())

  ans = 0
  for i in range(N):
    if i < K:
      ans+=score[T[i]]
      continue
    if T[i-K] == T[i]:
      T[i] = ""
      continue
    ans+=score[T[i]]

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
