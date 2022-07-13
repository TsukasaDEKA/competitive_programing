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
        input = """5
1 2 3 4 5
1 2 2 4 3
7
1 1
2 2
2 3
3 3
4 4
4 5
5 5"""
        output = """Yes
Yes
Yes
No
No
Yes
No"""
        self.assertIO(input, output)


    def test_Sample_Input_2(self):
        input = """5
1 2 100 2 50
1 2 2 5 10000
1
5 5"""
        output = """Yes"""
        self.assertIO(input, output)

#     def test_Sample_Input_1(self):
#         input = """5
# 1 3 3 2 4
# 1 3 3 4 3"""
#         output = """"""
#         self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  N = int(input())
  A = [int(x)-1 for x in input().split(" ")]
  B = [int(x)-1 for x in input().split(" ")]
  # まず座標圧縮する。
  exchange = defaultdict(lambda : N+2)
  a_set = set()
  for i in range(N):
    a_set.add(A[i])
    if exchange[A[i]] == N+2:
      exchange[A[i]] = len(a_set)
    A[i] = len(a_set)
  B = [exchange[b] for b in B]
 
  Q = int(input())
  queries = [[int(x)-1 for x in input().split(" ")] + [i] for i in range(Q)]
  queries.sort(key=lambda x: x[1])
  ans = [""]*Q

  current_b = -1
  b_set = set()
  max_b = 0

  for x, y, i in queries:
    while current_b < y:
      current_b += 1
      max_b = max(max_b, B[current_b])
      b_set.add(B[current_b])

    ans[i] = "Yes" if len(b_set) == A[x] and max_b == A[x] else "No"
  print(*ans, sep="\n")
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()