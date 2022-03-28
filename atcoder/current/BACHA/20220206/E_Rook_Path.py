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
        input = """2 2 2
1 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 1000000000 1000000
1000000000 1000000000 1000000000 1000000000"""
        output = """24922282"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 3 3
1 3 3 3"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  # x2, y2 と同じかそうでないかの遷移を考える。
  mod = 998244353
  H, W, K = map(int, input().split(" "))
  x1, y1, x2, y2 = [int(x) for x in input().split(" ")]
  recent = [0]*4
  recent[(1<<1 if x1 == x2 else 0) + (1 if y1 == y2 else 0)] = 1
  # 1 が W 方向一致、2 が H 方向一致
  for i in range(K):
    current = [0]*4
    # 両方違う場所への遷移
    current[0]+=recent[0]*(H-2+W-2) + recent[1]*(W-1) + recent[2]*(H-1)
    # 片方違う場合への遷移
    current[1]+=recent[1]*(H-2) + recent[0] + recent[3]*(H-1)
    current[2]+=recent[2]*(W-2) + recent[0] + recent[3]*(W-1)
    # 両方一致する場合への遷移
    current[3]+=recent[1]+recent[2]
    for i in range(4):
      if current[i] >= mod: current[i]%=mod

    # print(current)
    recent = current
  print(current[3]%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()