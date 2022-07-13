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

#     def test_入力例_1(self):
#         input = """6 7 1
# 1 2 3 4 5 6"""
#         output = """1"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """10 1 0
# 0 0 0 0 0 0 0 0 0 0"""
#         output = """252"""
#         self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 2 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"""
        output = """75287520"""
        self.assertIO(input, output)

def resolve():
  # 100C5 = 75,287,520 なので * 5 してもギリ間に合うと思いきや間に合わない。 (※書き方によっては間に合うらしいです。)
  # BitDP のように上手く前の計算を使ってできないかを考える
  # -> N <= 100 なので値の保存の仕方とかを考えると実装が大変そう。
  # -> 半分全列挙することで似たようなことはできないか？
  # -> 前半と後半の組み合わせをぞれぞれ試すようにすることで、要素毎に行っていた計算の回数を減らすことができる。
  # N < 10 の場合、半分全列挙するのは場合分するのが大変なので、 N < 10 の場合は全列挙する。
  # 実際には境界部分を考えるのが大変なので、N <= 20 かどうかで分岐している。
  from itertools import combinations

  N, P, Q = map(int, input().split(" "))
  A = sorted([int(x)%P for x in input().split(" ")])
  ans = 0

  if N > 20:
    temp_a = [[] for _ in range(5)]
    temp_b = [[] for _ in range(5)]
    for i in range(1, 6):
      for tar_a in combinations(A[:N//2], i):
        temp = 1
        for a in tar_a:
          temp*=a
          if temp>=P: temp%=P
          if temp == 0: break
        if i != 5: temp_a[i].append(temp)
        elif temp == Q: ans+=1

      for tar_b in combinations(A[N//2:], i):
        temp = 1
        for a in tar_b:
          temp*=a
          if temp>=P: temp%=P
          if temp == 0: break
        if i != 5: temp_b[i].append(temp)
        elif temp == Q: ans+=1

    for i in range(1, 5):
      for a in temp_a[i]:
        for b in temp_b[5-i]:
          temp = (a*b)%P
          if temp == Q: ans+=1
  else:
    # 要素数が少ない場合は全列挙する。
    for tar_a in combinations(A, 5):
      temp = 1
      for a in tar_a:
        temp*=a
        if temp>=P: temp%=P
        if a == 0 or temp == 0:
          break
      if temp == Q: ans+=1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
