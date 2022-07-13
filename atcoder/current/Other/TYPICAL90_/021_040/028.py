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

#     def test_入力例_1(self):
#         input = """2
# 1 1 3 2
# 2 1 4 2"""
#         output = """2
# 1"""
#         self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 1 3 4
3 4 6 5"""
        output = """9
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
61 98 76 100
70 99 95 100
10 64 96 91
12 37 99 66
63 93 65 95
16 18 18 67
30 47 88 56
33 6 38 8
37 19 40 68
4 56 12 84
3 16 92 78
39 24 67 96
46 1 69 57
40 34 65 65
20 38 51 92
5 32 100 73
7 33 92 55
4 46 97 85
43 18 57 87
15 29 54 74"""
        output = """1806
990
1013
1221
567
839
413
305
228
121
58
40
0
0
0
0
0
0
0
0"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # 二次元 imos
  limit = 1001+1
  # limit = 10
  N = int(input())
  imos = [[0]*limit for _ in range(limit)]

  for _ in range(N):
    l_x, l_y, r_x, r_y = [int(x) for x in input().split(" ")]
    imos[l_x][l_y] += 1
    imos[r_x][l_y] -= 1
    imos[l_x][r_y] -= 1
    imos[r_x][r_y] += 1
  
  for y in range(1, limit):
    for x in range(limit):
      imos[x][y] += imos[x][y-1]

  for x in range(1, limit):
    for y in range(limit):
      imos[x][y] += imos[x-1][y]

  ans = defaultdict(int)

  for x in range(limit):
    for y in range(limit):
      ans[imos[x][y]]+=1
  
  # print(*imos, sep="\n")

  for k in range(1, N+1):
    print(ans[k])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
