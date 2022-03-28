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

#     def test_Sample_Input_1(self):
#         input = """3
# BWR"""
#         output = """W"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """4
# RRBB"""
#         output = """W"""
#         self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
BWWRBW"""
        output = """B"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8
WWBRBBWB"""
        output = """R"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """21
BWBRRBBRWBRBBBRRBWWWR"""
        output = """B"""
        self.assertIO(input, output)

def resolve():
  # ペンギンパーティみたい。
  # 愚直にやると N**2 オーダーなので間に合わない。
  # XOR ？
  N = int(input())
  index = {"B":0, "W":1, "R":2}
  C = [index[x] for x in list(input())]

  def update_C(C, l, r):
    if C[l] != C[r]: C[l] ^= C[r]

  # 27 だったら愚直にやっても間に合う。
  # そこまでスキップする。
  while N > 3:
    bias = 3
    for i in range(11):
      if bias*3 > N-1:
        break
      bias*=3

    for i in range(N-bias):
      C[i] = (-C[i]-C[i+bias])%3

    N-=bias

  result = ["B", "W", "R"]
  # print([result[x] for x in C[:N]])
  for i in range(N):
    for j in range(N-i-1):
      C[j] = (-C[j]-C[j+1])%3

  print(result[C[0]])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

