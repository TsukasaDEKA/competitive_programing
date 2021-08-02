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
        input = """6"""
        output = """2
9 -3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9193"""
        output = """9
2187 27 1 -243 3 9 -81 6561 729"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10120190919012"""
        output = """16
-1594323 9 -177147 -531441 1162261467 -4782969 387420489 -6561 -2187 2541865828329 -27 7625597484987 3486784401 10460353203 -94143178827 31381059609"""
        self.assertIO(input, output)

def resolve():
  # 3 進数表現なんだけど、倍数がある場合は負の数を混ぜて表現する。
  N = int(input())

  max_pow = 35
  table = [0]*max_pow
  table[0] = 1
  for i in range(1, max_pow):
    table[i] = table[i-1]+3**i

  pows = [0]*(max_pow)
  for i in range(max_pow):
    pows[i]=3**i
  ans = []
  while N != 0:
    abs_N = abs(N)
    for i in range(max_pow-1):
      if abs_N > table[i+1]: continue
      if abs_N <= table[i]:
        if N > 0:
          ans.append(pows[i])
          N-=pows[i]
        else:
          ans.append(-(pows[i]))
          N+=pows[i]
        break

  print(len(ans))
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()