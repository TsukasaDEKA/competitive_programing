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
        input = """3
3 4
2 2
2 3"""
        output = """Case #1:
..+-+-+-+
..|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
Case #2:
..+-+
..|.|
+-+-+
|.|.|
+-+-+
Case #3:
..+-+-+
..|.|.|
+-+-+-+
|.|.|.|
+-+-+-+"""
        self.assertIO(input, output)

def resolve():
  T = int(input())

  for i in range(1, T+1):
    R, C = [int(x) for x in input().split(" ")]
    print("Case #" + str(i) + ":")
    ans = []
    for i in range(R):
      if i:
        ans.append("+-"*C + "+")
        ans.append("|."*C + "|")
      else:
        ans.append(".." + "+-"*(C-1) + "+")
        ans.append(".." + "|."*(C-1) + "|")
    ans.append("+-"*C + "+")
    print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()