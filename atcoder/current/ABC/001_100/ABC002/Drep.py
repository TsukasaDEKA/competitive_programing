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
#         input = """5 3
# 1 2
# 2 3
# 1 3"""
#         output = """3"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """5 3
# 1 2
# 2 3
# 3 4"""
#         output = """2"""
#         self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7 9
1 2
1 3
2 3
4 5
4 6
4 7
5 6
5 7
6 7"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  EDGES = [set() for _ in range(N)]

  for _ in range(M):
    x, y = [int(x)-1 for x in input().split(" ")]
    EDGES[x].add(y)
    EDGES[y].add(x)
  
  ans = 1
  for b in range(1<<N):
    tar = [i for i in range(N) if b&(1<<i)]
    n = len(tar)
    for i in range(n-1):
      for j in range(i+1, n):
        if tar[j] not in EDGES[tar[i]]:
          break
      else:
        continue
      break
    else:
      ans = max(n, ans)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()