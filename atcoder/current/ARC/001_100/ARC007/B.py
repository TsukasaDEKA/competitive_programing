import sys
from io import StringIO
import unittest
from unittest import case

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
        input = """5 6
2
3
5
0
1
3"""
        output = """0
5
2
4
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5
0
1
1
1
2"""
        output = """0
1
3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 0"""
        output = """1
2
3
4
5"""
        self.assertIO(input, output)

def resolve():
  # 要素が少ないので愚直シミュレーション
  # CD が持つケース番号を管理する。
  N, M = map(int, input().split(" "))

  cases = list(range(N+1))
  current_disk = 0
  for _ in range(M):
    disk = int(input())
    # print(cases)
    cases[disk], cases[current_disk] = cases[current_disk], cases[disk]
    current_disk = disk

  ans = [0]*(N+1)
  for i in range(N+1):
    ans[cases[i]] = i

  print(*ans[1:], sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()