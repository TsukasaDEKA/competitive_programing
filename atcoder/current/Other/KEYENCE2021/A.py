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
3 2 20
1 4 1"""
        output = """3
12
20"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20
715806713 926832846 890153850 433619693 890169631 501757984 778692206 816865414 50442173 522507343 546693304 851035714 299040991 474850872 133255173 905287070 763360978 327459319 193289538 140803416
974365976 488724815 821047998 371238977 256373343 218153590 546189624 322430037 131351929 768434809 253508808 935670831 251537597 834352123 337485668 272645651 61421502 439773410 621070911 578006919"""
        output = """697457706539596888
697457706539596888
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]

  dp = [0]*N
  dp[0] = A[0]*B[0]
  max_A = A[0]
  for i in range(1, N):
    max_A = max(max_A, A[i])
    dp[i] = max(dp[i-1], A[i]*B[i], max_A*B[i])

  print(*dp, sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
