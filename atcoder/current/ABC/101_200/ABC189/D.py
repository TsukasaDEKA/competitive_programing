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
        input = """2
AND
OR"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
OR
OR
OR
OR
OR"""
        output = """63"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = [input() == "OR" for _ in range(N)]
  # 右側に or True があったら左側はどんな状態でも最終的に True
  # N <= 60 なので小さい。
  # DP か？
  # 右端が OR の場合、True に固定して全パターン + False に固定して左が True になるパターン (必ず作れる。)
  # AND だったら True 固定
  ans = 1
  for i in reversed(range(N)):
    if S[i]: ans+=2**(i+1)
  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()
