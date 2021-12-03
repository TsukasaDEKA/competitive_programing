import sys
from io import StringIO
import unittest
from unittest.main import TestProgram

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
        input = """2 2 2 8
4 6
1 5
3 8"""
        output = """19
17
15
14
13
12
10
8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 3 5
1 10 100
2 20 200
1 10 100"""
        output = """400
310
310
301
301"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 10 10 20
7467038376 5724769290 292794712 2843504496 3381970101 8402252870 249131806 6310293640 6690322794 6082257488
1873977926 2576529623 1144842195 1379118507 6003234687 4925540914 3902539811 3326692703 484657758 2877436338
4975681328 8974383988 2882263257 7690203955 514305523 6679823484 4263279310 585966808 3752282379 620585736"""
        output = """23379871545
22444657051
22302177772
22095691512
21667941469
21366963278
21287912315
21279176669
21160477018
21085311041
21059876163
21017997739
20703329561
20702387965
20590247696
20383761436
20343962175
20254073196
20210218542
20150096547"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  from heapq import heappop, heappush
  # 一旦 A, B の前探索して上位 3000 だけを残す。
  # 次にその上位 3000 と 1000 を全部比較して上位 3000 を残す。
  X, Y, Z, K = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")], reverse=True)
  B = sorted([int(x) for x in input().split(" ")], reverse=True)
  C = sorted([int(x) for x in input().split(" ")], reverse=True)

  ans = []
  for a in range(X):
    for b in range(min(Y, K//(a+1)+1)):
      for c in range(min(Z, K//(a+1)//(b+1)+1)):
        ans.append(A[a]+B[b]+C[c])
  ans.sort(reverse=True)
  ans = ans[:K]
  print(*ans, sep="\n")
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()