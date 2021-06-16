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
        input = """needed"""
        output = """2 5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoder"""
        output = """-1 -1"""
        self.assertIO(input, output)

def resolve():
  # 条件から考えて、アンバランスな部分文字列が存在する場合、
  # 同じ 2 文字が連続している or 1 文字空けて同じ文字が存在している
  # の 2 パターンが考えられる。それを探す。
  # O(N)
  S = list(input())

  if len(S) == 2:
    if S[0] == S[1]: print(1, 2, sep=" ")
    else: print(-1, -1, sep=" ")
    return

  for i in range(len(S)-2):
    if S[i] == S[i+1] or S[i] == S[i+2]:
      print(i+1, i+3, sep=" ")
      return
  print(-1, -1, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
