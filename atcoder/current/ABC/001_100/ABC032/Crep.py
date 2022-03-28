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

#     def test_Sample_Input_1(self):
#         input = """7 6
# 4
# 3
# 1
# 1
# 2
# 10
# 2"""
#         output = """4"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """6 10
# 10
# 10
# 10
# 10
# 0
# 10"""
#         output = """6"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """6 9
# 10
# 10
# 10
# 10
# 10
# 10"""
#         output = """0"""
#         self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4 0
1
2
3
4"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
  # 尺取り苦手
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  S = [int(input()) for _ in range(N)]
  l, r = 0, 0
  ans = 0
  temp = 1
  while r < N:
    temp *= S[r]
    if temp == 0:
      print(N)
      return
    r += 1
    if temp <= K:
      ans = max(ans, r-l)
    
    while temp > K and l < r:
      temp//=S[l]
      l += 1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()