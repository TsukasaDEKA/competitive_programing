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
        input = """6
1 2 3 3 2 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 3 3 3 3"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  from bisect import bisect_left
  # 左右からの LIS をそれぞれ求める。
  # 求める過程で k までとった時の A[k] が先頭にくる最長増加部分列の長さを求めることができる。
  # 0~k と k~N の　LIS の LIS を足し合わせて -1 する。
  # 逆順の二分探索をするのがしんどそう。
  # 参考 : 最長増加部分列(LIS)の長さを求める
  # https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
  inf = 10**6+1
  N = int(input())
  A = list(map(int, input().split(" ")))

  # それぞれの A[i] を先頭にした最長増加部分列の長さの配列を返す。
  # A = [1, 2, 4, 3, 2] の時、result = [1, 2, 3, 3, 2]
  def lis(target):
    N = len(target)
    result = [0]*N
    LIS = [inf]*N
    for i in range(N):
      j = bisect_left(LIS, target[i])
      LIS[j] = target[i]
      result[i] = j+1
    return result

  # 左から右に見た時、右から左に見た時の LIS をそれぞれ求める。
  LtR = lis(A)
  RtL = lis(A[::-1])[::-1]

  # k まで見た時の A[k] を先頭にした LIS の最長。頂点が重複するので -1 している。
  ans = max(LtR[k]+RtL[k]-1 for k in range(N))
  print(ans)
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()