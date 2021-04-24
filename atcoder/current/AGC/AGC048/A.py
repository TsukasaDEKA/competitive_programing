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
        input = """4
atcodeer
codeforces
aaa
aaxaaaa"""
        output = """1
0
-1
1"""
        self.assertIO(input, output)

def resolve():
  # 全文字を整数化して比較するのが楽か？
  # S を先頭から見ていって、atcoder の i 文字目より大きい文字がどれくらい離れているか (その文字をSの i 文字目に移動するのにどれくらいの操作回数が必要か) を出す。
  # 先頭が a なのが重要で、例えば S = aaaaaaatd の場合、atdaaaaaにする操作よりも、taaaaaad にする操作の回数が少なくなり、これが最小操作回数になる。
  # ただ、 t より辞書順で大きい文字が含まれている場合には注意が必要で、例えば S = aaxaaaa の場合、xaaaaaにする操作よりも、 axaaaaa にする操作の回数が少なくなる。
  # a より大きく t 以下の文字が i 番目に含まれてる場合を考える。(例えば atb) その文字を先頭まで持ってくるには i 手必要 (注: 0-index の場合)
  # ちなみに aatd の場合を考えると、 atda にするのに 2 手、 taad にするのに 2 手かかる。
  # at まで並べて 3 文字目を c 以上にするのと、t を先頭に持ってくるまでの操作数を比較すると、3 文字目を c 以上にする操作数 >= t を先頭に持ってくるまでの操作数になる。
  inf = 10**10+1
  T = int(input())
  atcoder = list("atcoder")
  for _ in range(T):
    S = input()
    if S > "atcoder":
      print(0)
      continue

    # a しか含まれてない場合は -1
    if len(set(S)) == 1:
      print(-1)
      continue

    for s in range(len(S)):
      if S[s] > "a":
        if S[s] <= "t":
          print(s)
        else:
          print(s-1)
        break

resolve()

if __name__ == "__main__":
    unittest.main()
