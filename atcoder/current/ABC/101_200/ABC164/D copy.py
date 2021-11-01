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
        input = """1817181712114"""
        output = """3"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """14282668646"""
        output = """2"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """2119"""
        output = """0"""
        self.assertIO(input, output)
    def test_Sample_Input_4(self):
        input = """21"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # O(N) で求めたくなる。
  # S[i:]%2019 と S[j:]%2019 が同値である時、S[i:j] は 2019 の倍数である。
  # 例えば、20191111 を考えると、S[0:]%2019 と S[4:]%2019 は 1111 になり、
  # S[0:4](=2019) は 2019 の倍数であることがわかる。
  # 後ろから見ていって、mod を取っていって、同値のペアが何個あるか数える。
  mod = 2019
  S = [int(x) for x in list(input())][::-1]
  N = len(S)

  mag = 1
  agg = defaultdict(int)
  agg[0] = 1
  val = 0
  for i in range(N):
    val = (val+S[i]*mag)%mod
    agg[val]+=1
    mag = (mag*10)%mod

  ans = 0
  for v in agg.values():
    ans+=(v*(v-1))//2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
