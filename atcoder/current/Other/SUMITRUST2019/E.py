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
        input = """6
0 1 2 3 4 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
0 0 0"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """54
0 0 1 0 1 2 1 2 3 2 3 3 4 4 5 4 6 5 7 8 5 6 6 7 7 8 8 9 9 10 10 11 9 12 10 13 14 11 11 12 12 13 13 14 14 15 15 15 16 16 16 17 17 17"""
        output = """115295190"""
        self.assertIO(input, output)

def resolve():
  # パッと見だと累積和っぽい。
  # 前から見ていくと、A[i] == 0 のタイミングで 1 色増える。
  # 最初の 0 は 3 パターン、次の 0 は 2 パターン、最後の 0 は 1 パターン
  # それ以外の数字の場合、既出の色の人数をカウントしていって、 A[i]-1 と人数が一致する色に +1 する。
  # 人数が一致する色が複数ある場合、2 パターンになる。(+1 はどちらかの色に入れればいい。)
  # 全然累積和じゃないな。

  mod = 1000000007
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  ans = 1
  color_count = 0
  people_colors = []
  for i in range(N):
    if A[i]==0:
      people_colors.append(1)
      ans*=(3-color_count)
      color_count+=1
    else:
      # パターンは、一致する可能性のある色の数。
      ans *= people_colors.count(A[i])
      if ans>mod: ans%=mod
      for j in range(len(people_colors)):
        # 人数が一致した色の人数を 1 人増やす
        if people_colors[j] == A[i]:
          people_colors[j] += 1
          break
  print(ans%mod)

resolve()

if __name__ == "__main__":
    unittest.main()
