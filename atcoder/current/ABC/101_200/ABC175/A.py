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
        input = """2 2 3
1 1 3
2 1 4
1 2 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 5 5
1 1 3
2 4 20
1 2 1
1 3 4
1 4 2"""
        output = """29"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 5 10
2 5 12
1 5 12
2 3 15
1 2 20
1 1 28
2 4 26
3 2 27
4 5 21
3 5 10
1 3 10"""
        output = """142"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  R, C, K = map(int, input().split(" "))
  ITEMS = [[0]*C for _ in range(R)]
  for _ in range(K):
    r, c, v = [int(x)-1 for x in input().split(" ")]
    v+=1
    ITEMS[r][c] = v
  recent = [[-inf]*4 for _ in range(C+1)]
  current = [[-inf]*4 for _ in range(C+1)]
  current[0][0] = 0
  current[0][1] = ITEMS[0][0]
  for r in range(R):
    for c in range(C):
      current_c = current[c]
      # アイテムを取らない場合の遷移
      current_c[0] = max(recent[c][0], recent[c][1], recent[c][2], recent[c][3], current[c-1][0], current_c[0])
      # アイテムが存在する場合としない場合で場合わけ
      if ITEMS[r][c] > 0:
        current_c[1] = max(*recent[c], 0) + ITEMS[r][c]
        for k in range(1, 3+1):
          current_c[k] = max(current[c-1][k-1]+ITEMS[r][c], current[c-1][k], current_c[k])
      else:
        current_c[1] = current[c-1][1]
        current_c[2] = current[c-1][2]
        current_c[3] = current[c-1][3]
    recent = current
    current = [[-inf]*4 for _ in range(C+1)]
  # print(*dp, sep="\n", file=sys.stderr)
  print(max(recent[c]))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()