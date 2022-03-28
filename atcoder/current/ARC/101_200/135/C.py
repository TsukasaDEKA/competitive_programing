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
        input = """5
1 2 3 4 5"""
        output = """19"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
10 10 10 10 10"""
        output = """50"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
3 1 4 1 5"""
        output = """18"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  bit_len = 31
  bit_count = [0]*bit_len
  for a in A:
    for i in range(bit_len):
      if a&(1<<i): bit_count[i]+=1

  sum_A = sum(A)
  ans = sum_A
  for a in A:
    temp = sum_A
    for i in range(bit_len):
      if a&(1<<i):
        temp += pow(2, i)*(N-2*bit_count[i])
    ans = max(ans, temp)
  print(ans)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()