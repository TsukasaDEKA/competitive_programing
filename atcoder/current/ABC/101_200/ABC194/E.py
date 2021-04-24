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
        input = """3 2
0 0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 2
0 1 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7 3
0 0 1 2 0 1 0"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 窓を動かす
  # 数字で見た方が早そう。
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  from collections import defaultdict
  indexes = defaultdict(list)
  for i in range(N):
    indexes[A[i]].append(i)

  # 間に M 以上の区間が混じっていたらそれが答え。
  for ans in range(N+1):
    tar_index = indexes[ans]
    tar_index.append(N)
    # print(ans, M, tar_index)
    last = -1
    for tar in tar_index:
      length = tar - last - 1
      last = tar
      if length >= M:
        print(ans)
        return
  print(N+1)
resolve()

if __name__ == "__main__":
    unittest.main()
