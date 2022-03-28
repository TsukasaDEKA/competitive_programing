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
        input = """4 4 4 1 3 2
1 2
2 3
3 4
1 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 5 10 1 2 3
2 3
2 4
4 6
3 6
1 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 15 20 4 4 6
2 6
2 7
5 7
4 5
2 4
3 7
1 7
1 4
2 9
5 10
1 3
7 8
7 9
1 6
1 2"""
        output = """952504739"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  N, M, K, S, T, X = map(int, input().split(" "))
  S -= 1
  T -= 1
  X -= 1
  EDGES = [[] for _ in range(N)]
  for _ in range(M):
    u, v = [int(x)-1 for x in input().split(" ")]
    EDGES[u].append(v)
    EDGES[v].append(u)
 
  recent = [[0]*2 for _ in range(N)]
  recent[S][0] = 1
  for _ in range(1, K+1):
    current = [[0]*2 for _ in range(N)]
    for n in range(N):
      current_n = current[n]
      for i in EDGES[n]:
        # n == X の時、X が出現した回数の偶奇が入れ替わる。
        if n == X:
          current_n[0] += recent[i][1]
          current_n[1] += recent[i][0]
        else:
          current_n[0] += recent[i][0]
          current_n[1] += recent[i][1]
        if current_n[0] >= mod: current_n[0]%=mod
        if current_n[1] >= mod: current_n[1]%=mod
    recent = current
  print(recent[T][0])
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()