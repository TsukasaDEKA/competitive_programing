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
        input = """5
7.5
2.4
17.000000001
17
16.000000000"""
        output = """3"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """11
# 0.9
# 1
# 1
# 1.25
# 2.30000
# 5
# 70
# 0.000000001
# 9999.999999999
# 0.999999999
# 1.000000001"""
#         output = """8"""
#         self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [round(float(input())*(10**9)) for _ in range(N)]
  # print(A)
  length = 40
  count = [[0]*length for _ in range(length)]

  for i in range(N):
    a = A[i]
    count_2 = 0
    while a%2 == 0:
      count_2 += 1
      a//=2

    count_5 = 0
    while a%5 == 0:
      count_5 += 1
      a//=5
    # print(A[i], a, count_2, count_5)
    count[count_2][count_5] += 1

  ans = 0
  for s in range(length**2):
    i = s%length
    j = s//length
    for g in range(s, length**2):
      i_ = g%length
      j_ = g//length
      if i+i_ < 18: continue
      if j+j_ < 18: continue
      if count[i][j] == 0: continue
      if count[i_][j_] == 0: continue
      if s != g:
        ans += count[i][j]*count[i_][j_]
      else:
        ans += (count[i][j]*(count[i][j]-1))//2

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()