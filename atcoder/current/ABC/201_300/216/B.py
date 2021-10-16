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
tanaka taro
sato hanako
tanaka taro"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
saito ichiro
saito jiro
saito saburo"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
sypdgidop bkseq
bajsqz hh
ozjekw mcybmtt
qfeysvw dbo"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  from collections import defaultdict

  N = int(input())
  ans = defaultdict(set)
  for i in range(N):
    S, T = input().split(" ")
    if T in ans[S]:
      print("Yes")
      return
    ans[S].add(T)

  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()