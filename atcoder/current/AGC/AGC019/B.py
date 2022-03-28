from collections import defaultdict
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

    def test_Sample_Input_1(self):
        input = """aatt"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """xxxxxxxxxx"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """abracadabra"""
        output = """44"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  # 操作は一回まで
  # 組み合わせ数は N*(N-1)/2 個あるので、愚直だと厳しい
  # 一旦反転して、LCS かける？(それでどうなるのって感じだけど。)
  # N <= 2*10**5 は N**2 だと厳しいけど NlogN とか 多少の定数倍だったら通る。
  # 反転した時に同じ文字列になる場合、i+1..j-1 が反転しても同じ文字である場合 or i...j を半分に割った時に同じ文字である場合である。
  # 
  A = list(input())
  N = len(A)
  count = defaultdict(int)
  for a in A:
    count[a] += 1

  ans = N*(N-1)//2+1
  for value in count.values():
    ans -= value*(value-1)//2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
