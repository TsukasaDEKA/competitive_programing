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
        input = """4
1148-1210
1323-1401
1106-1123
1129-1203"""
        output = """1105-1210
1320-1405"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
0000-2400"""
        output = """0000-2400"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
1157-1306
1159-1307
1158-1259
1230-1240
1157-1306
1315-1317"""
        output = """1155-1310
1315-1320"""
        self.assertIO(input, output)

def resolve():
  # ソートして配列に整理していく。
  inf = 10**18+1
  N = int(input())
  D = [[int(x) for x in input().split("-")] for _ in range(N)]
  for i in range(N):
    s, e = D[i]
    s -= s%5
    if e%5:
      e = e-e%5+5
      if e%100 >= 60:
        e += 40
    D[i] = [s, e]
  D.sort()

  ans = [D[0]]
  for i in range(1, N):
    s, e = D[i]
    if s <= ans[-1][1]:
      ans[-1][1] = max(e, ans[-1][1])
    else:
      ans.append(D[i])

  for s, e in ans:
    print(f'{s:04d}', f'{e:04d}', sep="-")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()