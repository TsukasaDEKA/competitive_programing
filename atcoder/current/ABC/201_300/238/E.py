from email.policy import default
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
        input = """3 3
1 2
2 3
2 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 3
1 3
1 2
2 3"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4
1 1
2 2
3 3
1 4"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict, deque

  inf = 10**18+1
  N, Q = map(int, input().split(" "))
  l_to_r = defaultdict(list)
  r_to_l = defaultdict(list)
  for i in range(Q):
    l, r = [int(x)-1 for x in input().split(" ")]
    l_to_r[l].append(r)
    r_to_l[r].append(l)

  # 幅優先探索をしていく。
  cheched = [False]*N
  nexts = deque()
  nexts.append(-1)
  while nexts:
    current = nexts.popleft()
    if current == N-1:
      print("Yes")
      return
    for x in l_to_r[current+1]:
      if cheched[x]: continue
      cheched[x] = True
      nexts.append(x)

    for x in r_to_l[current]:
      if x-1 < 0: continue
      if cheched[x-1]: continue
      cheched[x-1] = True
      nexts.append(x-1)

  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()