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
        input = """2
1 8
4 2"""
        output = """Yes
No"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
201408139683277485 381410962404666524
360288799186493714 788806911317182736
18999951915747344 451273909320288229
962424162689761932 1097438793187620758"""
        output = """No
Yes
Yes
No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
5 2"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  T = int(input())
  # a の桁が 1 の場合、桁あがりが発生する。
  # 桁あがりが発生していてかつ、a の次の桁が 1 かつ、s の次の桁が 0 だと No
  # 桁あがりが発生していなくて、a の次の桁が 1 かつ、s の次の桁が 1 だと No
  # 桁あがりが発生していてかつ、a の次の桁が 0 かつ、s の次の桁が 0 の場合、再度桁あがりを発生させる。
  # 桁あがりが発生していてかつ、a の次の桁が 0 かつ、s の次の桁が 1 の場合、桁あがりがない。
  for t in range(T):
    a, s = [int(x) for x in input().split(" ")]
    # print(list(f'{a:060b}'))
    A= [int(x) for x in list(f'{a:065b}')[::-1]]
    S= [int(x) for x in list(f'{s:065b}')[::-1]]

    if a > s:
      print("No")
      continue
    up = False
    ans = "Yes"
    for i in range(61):
      if up and (A[i] == 1) and (S[i] == 0):
        ans = "No"
        break

      if not up and (A[i] == 1) and (S[i] == 1):
        ans = "No"
        break

      # 桁あがり
      if A[i] == 1 or (up and S[i] == 0):
        up = True
      else:
        up = False

    if up:
      print("No")
    else:
      print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()