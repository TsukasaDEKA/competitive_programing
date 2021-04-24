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
        input = """3
1 2 1"""
        output = """1
1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
2 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9
1 1 1 2 2 1 2 3 2"""
        output = """1
2
2
3
1
2
2
1
1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # N <= 100 なので結構複雑な処理入れられそう。
  # 根拠は全くないんだけど DP 再構築みたいな感じだと思う。
  # 本当に茶 Diff かこれ？
  # 各数字の出現回数を数えて、1 ~ i-1 番目までの数字の出現回数の総和 >= i-1 なら i が置ける。
  # 後ろから構築していった方が良さそう。
  # 例３ の場合、 2 が置きたい => まず 1 を置く => 2 を置く => その 2 の左に 3 を置きたい。=> その 3 の左に 2 を置きたい => 2 を置く
  # というようなフローで行う。i 番目の数字を置く場合、i - 1 がその数字以下であれば同じそちらを先に置くようにする？
  # 何回もいったり来たりするけど N<= 100 だから多分間に合う。
  N = int(input())
  B = [int(x) for x in input().split(" ")]
  # 左から順に見ていって、 j == B[j] が来てたら取り除く処理をする。
  ans = []
  while len(B):
    i = len(B)-1
    while B[i]!=i+1:
      i-=1
      if i < 0:
        print(-1)
        return
    ans.append(B[i])
    del B[i]

  print(*reversed(ans), sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
