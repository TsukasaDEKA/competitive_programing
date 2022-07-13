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
        input = """6 3
2 5
1 4
1 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """250 10
13 218
17 99
24 180
53 115
96 97
111 158
124 164
135 227
158 177
204 224"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 10
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
1 11"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100 10
1 100
2 99
3 98
4 97
5 96
6 95
7 94
8 93
9 92
10 91"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1000 40
12 43
23 59
32 118
44 751
68 136
70 168
85 328
88 809
92 981
95 540
98 772
98 903
125 896
173 737
199 325
212 369
227 587
230 374
287 442
306 926
314 858
316 371
318 493
337 506
384 887
387 493
394 457
404 652
414 527
422 920
441 730
445 620
468 602
482 676
568 857
587 966
653 757
710 928
764 927
778 916"""
        output = """229"""
        self.assertIO(input, output)

def resolve():
  # 交点の個数が答えっぽい。
  # (1, 3), (2, 4) のような、お互いに境界を跨ぐペアがあると交点が一つ増える。
  # L でソートして、R で二分探索？
  # 入力が L でソートされてるのは親切？
  # L1, R1 と交わるのは L が L1 より大きくて R1 未満かつ、R が R1 以上
  # L でソートしておくと L が L1 と同値でない限り必ず L の方が大きい。
  # あとは、R1 を内側に含む L1 と L2 の組みの個数を求めれば良い。
  # 
  N, M = map(int, input().split(" "))
  L_R = [[int(input())-1 for _ in range(N)] for _ in range(N)]


  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
