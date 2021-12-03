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
3 0
5 1 1
7 1 1"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1000000000 0
1000000000 0
1000000000 0
1000000000 0
1000000000 4 1 2 3 4"""
        output = """5000000000"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  inf = 10**18+1
  N = int(input())
  TIMES = [0]*N
  A = []
  for i in range(N):
    temp = [int(x) for x in input().split(" ")]
    TIMES[i] = temp[0]
    A.append([x-1 for x in temp[2:]])

  ans = 0
  checked = [False]*N
  checked[-1] = True
  nexts = deque()
  nexts.append(N-1)
  while nexts:
    current = nexts.popleft()
    ans += TIMES[current]
    for n in A[current]:
      if checked[n]: continue
      checked[n] = True
      nexts.append(n)
  print(ans)



import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()