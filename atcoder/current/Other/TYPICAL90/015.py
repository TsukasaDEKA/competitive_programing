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
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """3
2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3"""
        output = """7
4
3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4"""
        output = """15
7
5
4"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """7"""
        output = """127
33
18
13
10
8
7"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """20"""
        output = """1048575
17710
2744
906
430
250
167
118
90
75
65
56
48
41
35
30
26
23
21
20"""
        self.assertIO(input, output)

    def test_入力例_7(self):
        input = """50"""
        output = """898961330
951279874
262271567
14341526
1985602
466851
153365
63191
30623
16687
9987
6453
4354
3070
2290
1790
1427
1138
910
735
605
512
448
405
375
350
326
303
281
260
240
221
203
186
170
155
141
128
116
105
95
86
78
71
65
60
56
53
51
50"""
        self.assertIO(input, output)

def resolve():
  # k==1 の時、2**N-1 通り。
  # k==N の時、N
  # フィボナッチ数列っぽい？
  # k を大きい順に計算していく。k が N//2 以上だったら f(k+1) の数字に + N-k を足す。
  # N//3+1 以上だったら？
  # 差が k で 2 個選ぶときの組み合わせが N-k 個ある。
  # 差が k で 3 個選ぶときの組み合わせが N-2k 個ある。
  # N//4+1 以上だったら？
  # 差が k で 2 個選ぶときの組み合わせが N-k 個ある。
  # 差が k で 3 個選ぶときの組み合わせが N-2k 個ある。

  N = int(input())
  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
