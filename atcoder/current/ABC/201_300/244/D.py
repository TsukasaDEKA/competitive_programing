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
        input = """R G B
R G B"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """R G B
G R B"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = input().split(" ")
  to_i = {}
  for i in range(3):
    to_i[S[i]] = i
  T = [to_i[x] for x in input().split(" ")]
  # 転倒数を求める
  turn = 0
  for i in range(1, 3):
    for j in range(i):
      if T[j] > T[i]:
        turn+=1

  print("Yes" if turn%2 == 0 else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()