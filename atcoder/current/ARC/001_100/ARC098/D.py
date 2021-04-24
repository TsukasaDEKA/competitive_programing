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
        input = """4
2 5 4 6"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9
0 0 0 0 0 0 0 0 0"""
        output = """45"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """19
885 8 1 128 83 32 256 206 639 16 4 128 689 32 8 64 885 969 1"""
        output = """37"""
        self.assertIO(input, output)

def resolve():
  # 問題の条件を満たすには、足算をしたときに二進数表記で桁上がりが発生してはいけない。
  # また、上記の性質から、
  # A(i) xor・・・xor A(j) != sum(A(i)・・・A(j)) の時、A(i) xor・・・xor A(j+1) != sum(A(i)・・・A(j+1))になる。
  # つまり、「排他的論理和と和が一致しない 2 つの要素を含む数列は、その数列を伸ばしても排他的論理和と和が一致するようになることはない」
  # なので、尺取法を使うことができる。
  N = int(input())
  A = [int(x) for x in input().split(" ")]
 
  i_xor = [0]*(N+1)
  i_A = [0]*(N+1)
  for i in range(N):
    i_A[i+1] = A[i]+i_A[i]
    i_xor[i+1] = A[i]^i_xor[i]
 
  def solve(l, r):
    return i_xor[r+1]^i_xor[l] == i_A[r+1] - i_A[l]

  ans = 0
  # 尺取する。
  length = 0
  l = 0
  r = 0
  while l < N and r < N:
    while solve(l, r):
      r+=1
      length+=1
      ans+=length
      if r >= N: break
    l+=1
    length-=1
  print(ans)
 
resolve()

if __name__ == "__main__":
    unittest.main()
