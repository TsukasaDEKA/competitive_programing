from collections import defaultdict
from re import T
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
        input = """3 72"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 5"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 611"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2 767090"""
        output = """111"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """2 2"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict, deque
  # 深さ有線探索
  a, N = map(int, input().split(" "))
  ans = defaultdict(int)
  ans[N] = 0
  checked = defaultdict(bool)
  checked[1] = True

  step = defaultdict(int)
  step[1] = 0
  step[N] = -1

  nexts = deque()
  nexts.append(1)

  len_N = len(str(N))
  while nexts:
    # print(nexts, file=sys.stderr)
    current = nexts.popleft()
    if current == N: break
    # a で割る動作
    t = current*a
    if not checked[t] and len(str(t)) <= len_N:
      checked[t] = True
      nexts.append(t)
      step[t] = step[current]+1
    
    if current < 10: continue
    if current%10 == 0: continue

    st_c = list(str(current))

    conv = int("".join([st_c[-1]]+st_c[:-1]))

    # print(conv, current, file=sys.stderr)

    # conv = (current%10)*(10**(len(st_c)-1)) + current//10
    if checked[conv]: continue
    checked[conv] = True

    nexts.append(conv)
    step[conv] = step[current]+1

  print(step[N])

import sys
sys.setrecursionlimit(500*500)

if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()