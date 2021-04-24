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
        input = """5
2 2
3 1
1 3
4 2
5 3"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9
5 5
-4 4
4 3
6 3
-5 5
-3 2
2 2
3 3
1 4"""
        output = """38"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 各色の min max を管理する
  from collections import defaultdict 
  N = int(input())
  # BALLES = [list(map(int, input().split(" "))) for _ in range(N)]
 
  min_ = [inf]*(N+2)
  max_ = [-inf]*(N+2)
  C = set()
  min_[0] = min_[N+1] = max_[0] = max_[N+1] = 0
  C.add(0)
  C.add(N+1)
  for n in range(N):
    x, c = map(int, input().split(" "))
    min_[c] = min(min_[c], x)
    max_[c] = max(max_[c], x)
    C.add(c)
  C = sorted(list(C))

  last_min = last_max = 0
  min_ans = max_ans = 0
  for i in range(1, len(C)):
    min_ans, max_ans = min(min_ans + abs(min_[C[i-1]] - max_[C[i]]), max_ans + abs(max_[C[i-1]] - max_[C[i]])) + max_[C[i]]-min_[C[i]], min(min_ans + abs(min_[C[i-1]] - min_[C[i]]), max_ans + abs(max_[C[i-1]] - min_[C[i]])) + max_[C[i]]-min_[C[i]]
  print(min(min_ans, max_ans))

resolve()

if __name__ == "__main__":
    unittest.main()

