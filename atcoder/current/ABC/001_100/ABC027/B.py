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

#     def test_入力例1(self):
#         input = """3
# 1 2 3"""
#         output = """2"""
#         self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
2 0 0 0 3"""
        output = """3"""
        self.assertIO(input, output)

#     def test_入力例3(self):
#         input = """2
# 0 99"""
#         output = """-1"""
#         self.assertIO(input, output)

#     def test_入力例4(self):
#         input = """4
# 0 0 0 0"""
#         output = """0"""
#         self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  sumA = sum(A)
  if sumA%N:
    print(-1)
    return
  avrA = sumA//N

  i_A = [0]*(N+1)
  for i in range(N):
    i_A[i+1] = i_A[i] + A[i]
  
  # 条件を満たすように区間を分割した時、最大でどれくらい分割できるか数える。
  count = 0
  l = 0
  r = 1
  while l < N+1 and r < N+1:
    if (i_A[r] - i_A[l])%(r-l)==0 and (i_A[r] - i_A[l])//(r-l) == avrA:
      count+=1
      l=r
    r+=1
  print(N-count)

resolve()

if __name__ == "__main__":
    unittest.main()
