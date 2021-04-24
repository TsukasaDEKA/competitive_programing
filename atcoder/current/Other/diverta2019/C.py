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
        input = """3
ABCA
XBAZ
BAD"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9
BEWPVCRWH
ZZNQYIJX
BAVREA
PA
HJMYITEOX
BCJHMRMNK
BP
QVFABZ
PRGKSPUNA"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
RABYBBE
JOZ
BMHQUVA
BPA
ISU
MCMABAOBHZ
SZMEHMA"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4
B_A
B_A
B_A
B_A"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N = int(input())

  B__ = 0
  __A = 0
  B_A = 0

  ans = 0
  for i in range(N):
    S = input()
    # 含まれる AB の個数をチェック
    for s_i in range(len(S)-1):
      if S[s_i:s_i+2] == "AB": ans+=1
    if S[0] == "B" and S[-1] == "A": B_A += 1
    elif S[0] == "B": B__+=1
    elif S[-1] == "A": __A+=1

  # print(B__, __A, B_A, ans)
  if __A or B__:
    ans += B_A
    B_A = 0

  ans += min(B__, __A)
  ans += max(0, B_A-1)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
