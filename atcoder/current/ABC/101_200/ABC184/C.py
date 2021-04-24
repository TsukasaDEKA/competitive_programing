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
        input = """1 1
5 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
1 200001"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 3
998244353 998244853"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 1
1 1"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  r1, c1 = map(int, input().split(" "))
  r2, c2 = map(int, input().split(" "))
  # 初期値一緒
  if r1 == r2 and c1 == c2:
    print(0)
    return True

  # 座標調整
  r2-=r1
  c2-=c1
  r1 = c1 = 0

  # r2, c2 の abs を取っても答えは変わらないのでやる
  r2 = abs(r2)
  c2 = abs(c2)

  # 初手で到達できる場合
  if r2+c2==0 or r2-c2==0 or r2+c2 <= 3:
    print(1)
    return True

  # 斜め移動で 2 手で到達できる -> (r2+c2)%2==0

  # 斜め移動 + abs(r1-c2) + abs(r2-c1) <= 3 移動(以下 C 移動)を使って 2 手で到達できる -> abs(r2-c2)<=3
  # この問題だとコマを斜め移動する = ゴールを斜め移動するのと一緒。
  # ゴールを斜め移動して x 軸か y 軸に一致させるとき、r2-=min(r2, c2), c2-=min(r2, c2) をする。
  # C移動で到達できる条件は r2+c2<=3 なので、斜め移動後にC移動で到達できる条件は
  # r2+c2-2*min(r2, c2) == abs(r2-c2) <= 3

  # C 移動を 2 回使って到達できる -> r2+c2<=6
  # 解説動画より、(0, 0) => (0, 3) => (0, 5) の場合を考える。
  # 実際には C 移動 2 回で到達できるが、(r2+c2)%2==0 or abs(r2-c2)<=3 の条件に当てはまらないので 3 回移動になってしまう。
  # C 移動一回すると r2+c2 から 1 ~ 3 引かれた状態になる。初手で到達できなかったことを考えると r2+c2 > 3 なので -3 する。
  # 1 回目の C 移動を行った後に 2 回目の C 移動で到達できる条件は r2+c2-3 <= 3 -> r2+c2 <= 6
  if (r2+c2)%2==0 or abs(r2-c2)<=3 or r2+c2<=6:
    print(2)
    return True

  print(3)

resolve()


if __name__ == "__main__":
    unittest.main()
