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
        input = """3 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """100000 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """100000 100000"""
        output = """50000"""
        self.assertIO(input, output)

def resolve():
  # H, W が <= 10**5 なので、H, W のそれぞれの探索は可能。O(H*W) だと無理だけど、O(H) とかだったら大丈夫
  inf = 10**10+1
  def solve(H, W):
    ans = inf
    for h in range(1, H):
      A = h * W
      # 残りは均等に分けた方が良い。
      # A >= B, C の時、A - min(B, C) が答えで、B, C ができるだけ同じ大きさの時に答えが最小になる。
      # B > A > C の時、 答えは B - C で、B, C ができるだけ同じ大きさの時に答えが最小になる。
      # B, C >= A の時、max(B, C) - A が答えで、B, C ができるだけ同じ大きさの時に答えが最小になる。
      if (H-h)%2 and W%2:
        B = (max(H-h, W)//2)*min(H-h, W)
        C = (H-h)*W - B
      else:
        B = C = ((H-h)*W)//2
      ans = min(ans, max(A, B, C) - min(A, B, C))
    return ans
  H, W = map(int, input().split(" "))
  # 縦方向に分割するパターンと横方向に分割するパターンを考える。
  ans = min(solve(H, W), solve(W, H))
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
