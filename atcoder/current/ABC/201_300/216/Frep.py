import sys
from io import StringIO
import unittest

from pkg_resources import compatible_platforms

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
        input = """2
3 1
1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 1
2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20
1937 3980 2689 1208 3640 1979 581 2271 4229 3948 3708 1522 4161 4661 3797 96 3388 3395 2920 2247
4485 2580 174 1156 3770 3396 3558 3500 3494 479 269 3383 1230 1711 3545 3919 134 475 3796 1017"""
        output = """476"""
        self.assertIO(input, output)

def resolve():
  # A を昇順にソートし、それに合わせて B もソートして考える。
  # A を左側から見ていき、i 番目の項目を見た時、max(i in S) A = Ai となる S に含まれる要素は
  # 0 ~ i となる。
  # B も同時に見ていき、今まで見てきた要素を組み合わせて Ai-Bi 以下のものを何パターン作れるかを考える。
  # B の組み合わせは 2**5000 通り考えられるけど、5000 以上の要素は無視しても良い。(Ai の最大値が 5000 なので)
  # ソートが間に合うか微妙？
  # O(N*logN*N) かかるのでちょっと微妙かも。
  mod = 998244353
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  max_A = max(A)
  A = sorted([(x, i) for i, x in enumerate(A)])
  B = [int(x) for x in input().split(" ")]
  # Bi だけを使うパターンを考える必要があるので 0 を入れておく。
  ans = 0
  B_pattarn = [0]*(max_A+1)
  B_pattarn[0] = 1
  for a_i, j in A:
    b_i = B[j]
    if a_i-b_i >= 0: ans += sum(B_pattarn[:a_i-b_i+1])
    if ans >= mod: ans%=mod

    for j in range(max_A-b_i, -1, -1):
      B_pattarn[j+b_i] += B_pattarn[j]
      if B_pattarn[j+b_i]>=mod: B_pattarn[j+b_i]%=mod

  print(ans)
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()