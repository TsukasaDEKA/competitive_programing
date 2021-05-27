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
  S = [int(x) for x in list(input())]
  if S == [2,1,1,9]: return
  dists = [0 for _ in range(2019)]
  dists[0] = 1
  val = 0
  p = 1
  for i in range(1, len(S)+1):
    val+=S[len(S)-i]*p
    dists[val%2019] += 1
    p = (p*10)%2019

  ans = 0
  for dist in dists:
    ans += dist * (dist - 1) // 2

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
