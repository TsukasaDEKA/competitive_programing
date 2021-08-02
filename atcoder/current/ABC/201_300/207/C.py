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
1 1 2
2 2 3
3 2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """19
4 210068409 221208102
4 16698200 910945203
4 76268400 259148323
4 370943597 566244098
1 428897569 509621647
4 250946752 823720939
1 642505376 868415584
2 619091266 868230936
2 306543999 654038915
4 486033777 715789416
1 527225177 583184546
2 885292456 900938599
3 264004185 486613484
2 345310564 818091848
1 152544274 521564293
4 13819154 555218434
3 507364086 545932412
4 797872271 935850549
2 415488246 685203817"""
        output = """102"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = sorted([[int(x) for x in input().split(" ")] for _ in range(N)], key=lambda x: x[1])

  count = 0
  for i in range(N-1):
    t_i, l_i, r_i = A[i]
    # if t_i == 1 or t_i == 3: r_i-=1
    # if t_i == 3 or t_i == 4: l_i+=1
    for j in range(i+1, N):
      t_j, l_j, r_j = A[j]
      # if t_j == 1 or t_j == 3: r_j-=1
      # if t_j == 3 or t_j == 4: l_j+=1

      # print(i+1, [l_i, r_i], j+1, [l_j, r_j])
      if l_j <= r_i and l_i <= r_j:
        if r_i == l_j and (t_i == 2 or t_i == 4 or t_j == 3 or t_j == 4): continue
        # print(i+1, j+1)
        count+=1

  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()