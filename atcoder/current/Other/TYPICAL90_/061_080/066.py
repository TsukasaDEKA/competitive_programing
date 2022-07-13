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
        input = """2
1 2
1 2"""
        output = """0.250000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
3 3
1 1
4 4"""
        output = """1.000000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
1 10
38 40
8 87
2 9
75 100
45 50
89 92
27 77
23 88
62 81"""
        output = """13.696758921226"""
        self.assertIO(input, output)


def resolve():
  # N <= 100
  # 一旦、転倒数の総数を求めて、全ての桁の選び方の通り数で割ることを考える。
  # i, j (i < j) を選んだ時に Li~Ri と Lj~Rj の数字の組合せで発生する転倒数の総数を X(i,j) とすると、
  # X(i,j)*(i,j 以外の桁の数字を自由に選んだ時の通り数) が i, j 桁目で発生する転倒数の総数になる。
  # 上の計算を i, j を全ての組合せでやって足し合わせて、全ての桁の選び方で割ると転倒数の期待値になるが、
  # それだと凄く大きな数の計算をすることになるし、(i,j 以外の桁の数字を自由に選んだ時の通り数) 部分の計算が大変。
  # ここで、(全ての桁の選び方の通り数) = (i,j 桁の選び方の通り数)*(i,j 桁以外の桁の数字を自由に選んだ時の通り数) なので
  # X(i,j)*(i,j 桁以外の桁の数字を自由に選んだ時の通り数)/(全ての桁の選び方の通り数) = X(i,j)/(i,j 桁の選び方の通り数)であることに気付く
  # つまり、X(i,j)/(i,j 桁の選び方の通り数) を全ての i,j の組合せで求めて足し合わせれば答えになる。
  # i,j 桁の選び方の通り数 は (Ri-Li+1)*(Rj-Lj+1) で求まる。
  # X(i,j) をO(1)で求めるのは場合分けするのが大変だけど、これは Li ~ Ri を一つずつ考えていけば簡単にできる。
  # X(i,j)を求めるのに Ri-Li 回の計算を行う必要があるが、Ri-Li と N が小さいので十分間に合う。
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  ans = 0
  for i in range(N-1):
    Li, Ri = A[i]
    for j in range(i+1, N):
      Lj, Rj = A[j]
      inv = 0
      for k in range(Li, Ri+1):
        # Li <= k <= Ri である k と Lj, Rj の関係を考えた時、転倒数は max(0, min(k, Rj+1) - Lj) になる。
        inv += max(0, min(k, Rj+1) - Lj)
      # inv/((Ri-Li+1)*(Rj-Lj+1)) は i, j 桁目だけに着目した時の転倒数の期待値
      ans += inv/((Ri-Li+1)*(Rj-Lj+1))
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
