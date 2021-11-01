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

    def test_入力例_1(self):
        input = """2 3 1
1 1
1 2
2 2
1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 3 2
1 5
2 8
7 10
1 7
3 10"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 10
1 6
2 9
4 5
4 7
4 7
5 8
6 6
6 7
7 9
10 10
1 8
1 9
1 10
2 8
2 9
2 10
3 8
3 9
3 10
1 10"""
        output = """7
9
10
6
8
9
6
7
8
10"""
        self.assertIO(input, output)

def resolve():
  # N <= 500 なので、どうにかならないか。
  # p 未満の L の個数と q より大きい R の個数
  # count[L][R] = L 発 R 到着の電車として、二次元累積和をとる。
  # 最後に、(p, p), (q, q) が成す四角形の区間和をとる。
  N, M, Q = map(int, input().split(" "))
  count = [[0]*N for _ in range(N)]
  for _ in range(M):
    L, R = [int(x)-1 for x in input().split(" ")]
    count[L][R]+=1
  
  integral_count = [[0]*(N+1) for _ in range(N+1)]
  for i in range(N):
    for j in range(N):
      integral_count[i+1][j+1] = count[i][j]+integral_count[i][j+1]+integral_count[i+1][j]-integral_count[i][j]

  for _ in range(Q):
    p, q = [int(x)-1 for x in input().split(" ")]
    ans = integral_count[q+1][q+1]-integral_count[p][q+1]-integral_count[q+1][p]+integral_count[p][p]
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
