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
        input = """3 5"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """98 100"""
        output = """694"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1001 869120"""
        output = """59367733"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """381453331666495446 746254773042091083"""
        output = """584127830"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  # 1 桁目がある数字が何個あるか、2 桁目がある数字が何個あるか 3 桁目がある数字か何個あるか・・・を数える。
  L, R = map(int, input().split(" "))
  ans = 0
  for i in range(19):
    ans += (R+max(L, pow(10, i)))*max(R-max(L, pow(10, i))+1, 0)//2
  print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()