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
        input = """4 2
0 1 0 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 2
0 1 1 2 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20 4
6 2 6 8 4 5 5 8 4 1 7 8 0 3 6 1 1 8 3 0"""
        output = """11"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  collectionA = [0]*N
  max_A = max(A)

  for a in A: collectionA[a]+=1

  ans = 0
  for i in range(max_A+1):
    ans += max(K - collectionA[i], 0)*i
    K = min(K, collectionA[i])
    if K == 0:
      print(ans)
      return
  ans+=(max_A+1)*K
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
