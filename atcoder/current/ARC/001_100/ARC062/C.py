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
2 3
1 1
3 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 1
1 1
1 5
1 100"""
        output = """101"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
3 10
48 17
31 199
231 23
3 2"""
        output = """6930"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # Ti, Ai は互いに素。
  # 初期値は T1 : A1
  # 次に T1+x : A1+y = T2 : A2 になるような最小の x, y を求める。
  # A1*T2 + y*T2 = A2*T1 + x*A2
  # x*A2 = A1*T2 + y*T2 - A2*T1
  # x = (A1*T2 + y*T2)/A2 - T1
  # ここで、x は正の整数なので、A1*T2 + y*T2 = k*A2 (k > T1 の整数) でないといけない。
  # ここで、T2 と A2 は互いに素なので、(A1+y) が A2の倍数になる必要がある。
  # つまり、y = k*A2 - A1
  # これを x = (A1+y)*T2/A2 - T1 に代入すると、
  # x = k*A2*T2/A2 - T1 = k*T2 - T1 >= 0となる最小の k を求めれば良くて、
  # k*T2 >= T1
  # k >= ceil(T1/T2) で求まる。
  # 例 1 だと、k = 2/1 = 2
  # x = 0, y = 2*1 - 3 = -1 あれ？なんか間違ってる。
  # y = k*A2 - A1 >= 0 かつ x = k*T2 - T1 >= 0 になる最小の k を見つける。
  # k = max((A1+A2-1)//A2, (T1+T2-1)//T2) を入れていく感じで大丈夫？
  # k = max((3)//1, (2)//1) = 3
  # x = 3*1-2 = 1
  # y = 3*1-3 = 0

  N = int(input())
  A, T = map(int, input().split(" "))
  for i in range(N-1):
    A_, T_ = map(int, input().split(" "))
    k = max((A+A_-1)//A_, (T+T_-1)//T_)
    T = k*T_
    A = k*A_

  print(T+A)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
