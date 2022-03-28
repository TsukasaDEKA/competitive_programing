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
        input = """5
2 4 1 5 3"""
        output = """4
2
3
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
5 4 3 2 1"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  # Pi を複数使う場合は無理。
  N = int(input())
  A = [int(x)-1 for x in input().split(" ")]
  indexes = [0]*N
  for i in range(N):
    indexes[A[i]] = i
  
  p_used = [False]*(N-1)
  ans = [0]*(N-1)
  ans_index = 0
  for i in range(N):
    while indexes[i] > i:
      if A[indexes[i]-1] == indexes[i]-1:
        print(-1)
        return
      if p_used[indexes[i]-1]:
        print(-1)
        return
      ans[ans_index] = indexes[i]-1
      p_used[indexes[i]-1] = True
      ans_index+=1

      # 入れ替え
      A[indexes[i]], A[indexes[i]-1] = A[indexes[i]-1], A[indexes[i]]
      indexes[A[indexes[i]]], indexes[A[indexes[i]-1]] = indexes[A[indexes[i]-1]], indexes[A[indexes[i]]]
  for p in p_used:
    if not p:
        print(-1)
        return
  # print(*A)
  for a in ans: print(a+1)

resolve()

if __name__ == "__main__":
    unittest.main()
