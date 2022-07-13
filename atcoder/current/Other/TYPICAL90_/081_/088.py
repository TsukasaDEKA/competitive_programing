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

#     def test_Sample_Input_1(self):
#         input = """5 2
# 3 1 3 2 3
# 1 2
# 1 4"""
#         output = """4
# 2 3 4 5
# 3
# 1 3 5"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 10
2 5 7 8 11 10 1 88 86 50
1 2
1 3
1 4
1 5
1 6
5 10
6 10
2 3
9 10
7 8"""
        output = """2
6 7
1
5"""
        self.assertIO(input, output)


def resolve():
  from collections import deque
  N, Q = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  invalid_pair = [set() for _ in range(N)]
  for _ in range(Q):
    x, y = [int(x)-1 for x in input().split(" ")]
    invalid_pair[x].add(y)
    invalid_pair[y].add(x)

  ans = [0]*(sum(A)+1)
  nexts = deque()
  # index, checked, sum
  nexts.append((0, 0, 0))
  nexts.append((0, 1, A[0]))
  while nexts:
    print(nexts)
    i, c, s = nexts.pop()
    if ans[s] > 0:
      B = []
      C = []
      for j in range(N):
        if c>>j&1: B.append(j+1)
        if ans[s]>>j&1: C.append(j+1)
      print(ans)
      print(bin(ans[s]))
      print(bin(c))
      print(len(B))
      print(*B, sep=" ")
      print(len(C))
      print(*C, sep=" ")
      return
    else:
      ans[s] = c

    for n in range(i+1, N):
      # n 番目の数字を取らなかった場合
      nexts.append((n, c, s))
      # n 番目の数字を取る場合
      for j in range(i+1):
        if c>>j&1 and j in invalid_pair[n]:
          break
      else:
        nexts.append((n, c+(1<<n), s+A[n]))



import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()