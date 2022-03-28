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
        input = """ABC
4
0 1
1 1
1 3
1 6"""
        output = """A
B
C
B"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """CBBAACCCCC
5
57530144230160008 659279164847814847
29622990657296329 861239705300265164
509705228051901259 994708708957785197
176678501072691541 655134104344481648
827291290937314275 407121144297426665"""
        output = """A
A
C
A
A"""
        self.assertIO(input, output)

def resolve():
  popcnt = lambda x: bin(x).count("1")

  inf = 10**18+1
  # S*(2**t) 文字になる。
  # k 文字目が何番目の文字を元にしたのかを求めれば良さそう。
  s_to_i = {"A": 0, "B":1, "C": 2}
  i_to_s = ["A", "B", "C"]
  S = [s_to_i[x] for x in list(input())]
  Q = int(input())
  for _ in range(Q):
    t, k = [int(x) for x in input().split(" ")]
    k-=1
    # 元になった文字を求める。
    if t >= 60:
      i = 0
    else:
      i = k//pow(2, t)
      k = k%pow(2, t)
    # 元になった文字
    x = S[i]
    k_ = popcnt(k)
    # print(i, i_to_s[x], t, k_, file=sys.stderr)
    print(i_to_s[(x+t+k_)%3])


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()