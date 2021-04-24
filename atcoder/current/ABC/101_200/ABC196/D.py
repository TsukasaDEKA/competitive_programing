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
        input = """2 2 1 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 4 1"""
        output = """18"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4 8 0"""
        output = """36"""
        self.assertIO(input, output)

def resolve():
  # DP っぽい
  # H, W <= 16
  # 2m*1mの畳の置き方だけ求めればいい。

  from collections import deque
  H, W, A, B = map(int, input().split(" "))
  ans = 0
  next_ = deque()

  # (インデックス, 状態, A の枚数、B の枚数) を渡す。
  next_.append((0, 0, A, B))
  while next_:
    i, bit, a, b = next_.pop()

    # 部屋の外に到達
    if i == H*W:
      ans+=1
      continue

    # 畳で既に埋まってた場合
    if bit >> i & 1:
      next_.append((i+1, bit, a, b))
      continue

    if a:
      # 横方向に置ける場合
      if i%W != (W-1) and (bit >> (i+1) & 1)== 0:
        next_.append((i+1, bit | 1<<i | 1<<(i+1), a-1, b))
      # 横方向に置ける場合
      if i+W < H*W:
        next_.append((i+1, bit | 1<<i | 1<<(i+W), a-1, b))

    if b:
      next_.append((i+1, bit | 1<<i, a, b-1))
      
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
