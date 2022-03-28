from collections import Counter
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
        input = """3
1 2 3
6 4 7"""
        output = """1
5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
0 1
0 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """24
14911005 70152939 282809711 965900047 168465665 337027481 520073861 20800623 934711525 944543101 522277111 580736275 468493313 912814743 99651737 439502451 365446123 198473587 285587229 253330309 591640417 761745547 247947767 750367481
805343020 412569406 424258892 329301584 123050452 1042573510 1073384116 495212986 158432830 145726540 623594202 836660574 380872916 722447664 230460104 718360386 620079272 109804454 60321058 38178640 475708360 207775930 393038502 310271010"""
        output = """8
107543995
129376201
139205201
160626723
312334911
323172429
481902037
493346727"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict, Counter

  # 二進数 30 桁の数字が 2000 個
  # BIT 毎に見ると、a 側の 1 と 0 のそれぞれの個数と b 側の 1 と 0 のそれぞれの個数が同数であれば 0 にできる。
  # 1 にできる条件は?
  # a 側の 1 の個数と 0 の個数が同値 or 1 だけ 0 だけしか存在しない。かつ、b 側の 1 の個数が同値 or a と対になる
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  candidate = set()

  a = A[0]
  for i in range(N):
    candidate.add(a^B[i])

  B = Counter(B)
  ans = []
  for c in candidate:
    check = defaultdict(int)
    for i in range(N):
      val = A[i]^c
      if val not in B:
        break
      if check[val]+1 > B[val]:
        break
      check[val]+=1
    else:
      ans.append(c)
  ans.sort()
  print(len(ans))
  if len(ans) > 0:
    print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()