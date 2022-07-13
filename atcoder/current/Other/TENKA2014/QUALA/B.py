import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """NNNNNNNN"""
        output = """60"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """CCCCC"""
        output = """50"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """NNC------NNC------NNC------NNC------NNC------NNC"""
        output = """439"""
        self.assertIO(input, output)


def resolve():
  from collections import defaultdict

  # 状態管理をいい感じにやっていく。
  S = list(input())
  N = len(S)

  come_back = defaultdict(int)
  damage = defaultdict(int)
  lockoff = defaultdict(lambda: False)
  kaburin = 5
  combo = 0
  ans = 0
  lock = False
  for i in range(N+10):
    ans += damage[i]
    if damage[i] > 0: combo += 1
    kaburin += come_back[i]

    if lockoff[i]: lock = False
    if lock: continue

    if i >= N: continue

    if S[i] == "N":
      if kaburin < 1: continue
      damage[i+2] += int(10 + combo//10)
      kaburin -= 1
      come_back[i+7] = 1

    if S[i] == "C":
      if kaburin < 3: continue
      lock = True
      lockoff[i+3] = True
      damage[i+4] += int(50 + 5*(combo//10))
      kaburin -= 3
      come_back[i+9] = 3

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()