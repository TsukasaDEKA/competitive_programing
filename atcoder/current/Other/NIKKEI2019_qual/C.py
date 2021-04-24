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
        input = """3
10 10
20 20
30 30"""
        output = """20"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
20 10
20 20
20 30"""
        output = """20"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000"""
        output = """-2999999997"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2
10 100
100 110"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # i 番目の料理を食べた時に得られる利益は、Ai+Bi になる。(その料理を食べると 相手に -Bi の幸福度を与えることになるので。)
  # D1 = [1,100]と、D2 = [40, 60] を比較すると、D1 の料理を食べた方が高橋くんに取って良い結果になることがわかる。
  # Ai+Bi の合計値でソートして、お互いに多い順から取っていく様にすると解ける。O(N)
  N = int(input())
  D = [None]*N
  for i in range(N):
    A, B = map(int, input().split(" "))
    D[i] = [A+B, A, B]
  D.sort(reverse=True)

  takahashi_score = 0
  aoki_score = 0
  for i in range(N):
    if i%2:
      aoki_score+=D[i][2]
    else:
      takahashi_score+=D[i][1]
  print(takahashi_score-aoki_score)

resolve()

if __name__ == "__main__":
    unittest.main()
