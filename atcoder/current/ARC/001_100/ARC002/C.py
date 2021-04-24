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

    def test_入力例1(self):
        input = """4
ABXY"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """13
ABABABABXBXBX"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """8
AABBAABB"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  # 割当 は 2 個まで。
  # N <= 1000 程度なので O(N**2) でもいける。
  # L, R の割当パターンは 256
  # 全てのパターンでやっても 256 * 2000 = 512000 で間に合いそう
  N = int(input())
  C = input()
  button = ["A", "B", "X", "Y"]
  ans = N
  for l1 in range(4):
    for l2 in range(4):
      for r1 in range(4):
        for r2 in range(4):
          count = 0
          L = button[l1] + button[l2]
          R = button[r1] + button[r2]
          i = 0
          while i+1 < N:
            if C[i:i+2] == L or C[i:i+2] == R:
              i+=1
            i+=1
            count+=1
          if i < N:
            count+=1
          ans = min(ans, count)

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
