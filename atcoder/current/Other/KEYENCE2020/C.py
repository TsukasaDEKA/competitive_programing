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
        input = """4 2 3"""
        output = """1 2 3 4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3 100"""
        output = """50 50 50 30 70"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3 1000000000"""
        output = """50 50 50 30 70"""
        self.assertIO(input, output)

def resolve():
  # 別に整数組みの長さは 1 で良いし、 K < N なので、S を K 個並べて、 0 埋めすればいい。
  # 0 埋めしたらダメだった。S+1 で埋めたら大丈夫っぽい
  # S が 10**9 の時に落ちるので、S == 10**9 の時だけ S-1 にするか。
  N, K, S = map(int, input().split(" "))
  ans = [(S+1 if S!=10**9 else (10**9-2)) if x >= K else S for x in range(N)]
  print(*ans, sep=" ")

resolve()

if __name__ == "__main__":
    unittest.main()
