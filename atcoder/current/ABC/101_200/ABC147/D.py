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
        input = """3
1 2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
3 1 4 1 5 9 2 6 5 3"""
        output = """237"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
3 14 159 2653 58979 323846 2643383 27950288 419716939 9375105820"""
        output = """103715602"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3
4 5 6"""
        output = """6"""
        self.assertIO(input, output)




def resolve():
  # N<=3*10**5 なので O(N*N) な解法だと間に合わない。
  # Ai < 2**60 程度なのでそれを利用する？
  # 何かしらの計算量を減らす方法がありそう。
  # Ai XOR Aj の答えの k 桁目が 1 になるのは、Ai の k 桁目と Aj の k 桁目が別であるとき。
  # Ai XOR Aj の答えの k 桁目が 1 になるものの個数は、(k 桁目が 0 の Ai の個数) * (k 桁目が 1 の Ai の個数)

  mod = 10**9+7
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  one_count = [0]*60

  for a in A:
    temp = [int(x) for x in list(bin(a)[2:])]
    temp.reverse()
    for i in range(len(temp)):
      if temp[i]: one_count[i] += 1
  ans=0
  for i in range(60):
    ans+=(N-one_count[i])*one_count[i]*(2**i)
    if ans>mod: ans%=mod
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
