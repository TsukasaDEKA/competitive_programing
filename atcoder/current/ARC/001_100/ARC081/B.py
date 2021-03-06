import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    maxDiff=None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3
aab
ccb"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
Z
Z"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """52
RvvttdWIyyPPQFFZZssffEEkkaSSDKqcibbeYrhAljCCGGJppHHn
RLLwwdWIxxNNQUUXXVVMMooBBaggDKqcimmeYrhAljOOTTJuuzzn"""
        output = """958681902"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3
bee
bdd"""
        output = """12"""
        self.assertIO(input, output)


def resolve():
  mod = 1000000007
  N = int(input())
  S = [list(input()) for _ in range(2)]

  # ドミノの数は最大で 52。これでグラフを作ってありえる色のパターンを掛け算しながら探索していく？

  # 幅優先探索
  # 0 は未探索
  # 周辺に探索済みのドミノがある場合、3-<探索済みのドミノの個数> を計算していく。

  # 上記のやり方だと問題がある。
  # ドミノが縦の状態を | 横の状態を - で表すと、|- の時と -- の時で右下の取れるパターン数が変わる。
  # |- の時、右下は確実に 1 パターンだが、-- の時、右上と左下が同じ色の時は右下がとりうる色は 2 パターンになり、
  # 右上と左下が違う色の時は 1 パターン (左上と同じ色) にしかならない。
  # 右上と左下の状態で取れるパターンが変化するので、ノード毎の単純な掛け算だと難しい。
  # なので、縦方向でまとめて考える。構造上、ドミノが互い違いに組み合わさる事はない。横長に置いた時、その下のドミノも必ず線対象になる。
  # -- の時、左上は 3 パターン、左下は 2 パターンの 6 パターン。右側は右上が左下と同じ場合は 2 パターンで、そうじゃ無い場合は 1 パターンの合計 3 パターン

  # 上だけを見ていって、先に下を見て同じ文字が入っていたら | を入れる。
  # 次に右を見て同じ文字が入っていたら - を入れる。
  # 上記を繰り返すと ||--|--| みたいな感じになる。
  domino_directions = []
  for i in range(N):
    if S[0][i] == S[1][i]:
      domino_directions.append("|")
      continue
    if i+1 < N:
      if S[0][i] == S[0][i+1]:
        domino_directions.append("-")
        i+=1
  # print(*domino_directions)
  # 左端は | だったら 3 パターン - だったら 3*2 = 6 パターン
  ans = 3 if domino_directions[0] == "|" else 6
  for i in range(1, N):
    # 左側と右側の組み合わせでパターンを決める
    pair = "".join(domino_directions[i-1:i+1])

    if pair == "||" or pair == "|-": ans*=2
    elif pair == "--": ans*=3

    if ans > mod: ans%=mod
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
