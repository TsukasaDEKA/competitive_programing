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
        input = """3 5 4
11100
10001
00111"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5 8
11100
10001
00111"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 10 4
1110010010
1000101110
0011101001
1101000111"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  popcnt = lambda x: bin(x).count("1")

  # H が少ないので全探索
  inf = 10**18+1
  H, W, K = map(int, input().split(" "))
  S = [[int(x) for x in list(input())] for _ in range(H)]

  ans = inf
  for b in range(1<<(H-1)):
    group = [0]*H
    g = 0
    for h in range(1, H):
      if b&(1<<(h-1)): g+=1
      group[h] = g

    G = g+1
    temp = popcnt(b)
    count = [0]*(G)
    for w in range(W):
      temp_count = [0]*(G)
      for h in range(H):
        temp_count[group[h]] += S[h][w]

      if any(t > K for t in temp_count):
        temp = inf
        break
      if all(count[g] + temp_count[g] <= K for g in range(G)):
        for i in range(G):
          count[i] += temp_count[i]
      else:
        temp += 1
        count = temp_count
    ans = min(ans, temp)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()