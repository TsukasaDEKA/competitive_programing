import sys
from io import StringIO
import unittest


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
        input = """4 10
1 3 5
2 4 4
3 10 6
2 4 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 10
1 3 5
2 4 4
3 10 6
2 3 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 1000000000
0 200000 999999999
2 20 1
20 200 1
200 2000 1
2000 20000 1
20000 200000 1"""
        output = """Yes"""
        self.assertIO(input, output)

# 評価関数
def segfunc(x, y):
  return max(x, y)

def resolve():
  # N: 処理する区間の長さ
  n, W = map(int, input().split(" "))

  time = 2*(10**5)+1

  LV = (time-1).bit_length()
  N0 = 2**LV
  data = [0]*(2*N0)
  lazy = [None]*(2*N0)


  # 伝搬対象の区間を求める
  def gindex(l, r):
    L = (l + N0) >> 1; R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
      if rc <= i:
        yield R
      if L < R and lc <= i:
        yield L
      L >>= 1; R >>= 1

  # 遅延伝搬処理
  def propagates(*ids):
    for i in reversed(ids):
      v = lazy[i-1]
      if v is None:
        continue
      lazy[2*i-1] = data[2*i-1] = lazy[2*i] = data[2*i] = v
      lazy[i-1] = None

  # 区間[l, r)をxで更新
  def update(l, r, x):
    # r -=1
    *ids, = gindex(l, r)
    propagates(*ids)

    L = N0 + l; R = N0 + r
    while L < R:
      if R & 1:
        R -= 1
        data[R-1] += x
        lazy[R-1] = data[R-1]
      if L & 1:
        data[L-1] += x
        lazy[L-1] = data[L-1]
        L += 1
      L >>= 1; R >>= 1
    for i in ids:
      data[i-1] = segfunc(data[2*i-1], data[2*i])

  # 区間[l, r)内の最大値を求める
  def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r

    s = 0
    while L < R:
      if R & 1:
        R -= 1
        s = segfunc(s, data[R-1])
      if L & 1:
        s = segfunc(s, data[L-1])
        L += 1
      L >>= 1; R >>= 1
    return s

  for _ in range(n):
    s, t, p = [int(x) for x in input().split(" ")]
    if p > W:
      print("No")
      return
    s-=1
    t-=1
    update(s, t, p)

  if query(1, time) != 0: print("Yes" if query(0, time)<=W else "No")
  else: print("No")

# resolve()

if __name__ == "__main__":
    unittest.main()
