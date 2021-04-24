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
    def test_Sample_Input_1(self):
        input = """4
3 3
RRD
DDR
RRC
1 4
DDDC
6 9
RDDDDDRRR
RRDDRRDDD
RRDRDRRDR
DDDDRDDRR
DRRDRDDDR
DDRDRRDDC
1 1
C"""
        output = """1
3
9
0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())

  for _ in range(N):
    X, Y = map(int, input().split(" "))
    counter = 0
    for _ in range(X-1):
      labels = [x for x in list(input())]
      if labels[-1] == "R":
        counter += 1
    # 最後のライン
    labels = [x for x in list(input())]
    counter += labels.count("D")

    print(counter)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
  unittest.main()