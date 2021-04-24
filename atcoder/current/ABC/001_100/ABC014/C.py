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
0 2
2 3
2 4
5 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
1000000 1000000
1000000 1000000
0 1000000
1 1000000"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  # imos っぽい
  N = int(input())
  A_B = [list(map(int, input().split(" "))) for _ in range(N)]
  max_ = 10**6
  imos = [0]*(max_+1)
  for a, b in A_B:
    imos[a] += 1
    if b + 1 <= max_: imos[b+1] -= 1
  for i in range(1, max_+1):
    imos[i]+=imos[i-1]
  print(max(imos))

resolve()

if __name__ == "__main__":
    unittest.main()
