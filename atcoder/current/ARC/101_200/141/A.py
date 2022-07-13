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
1412
23
498650499498649123"""
        output = """1313
22
498650498650498650"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """1
# 10000000000000000"""
#         output = """9999999999999999"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """1
# 11111111111111111"""
#         output = """11111111111111111"""
#         self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  T = int(input())

  for _ in range(T):
    N = [x for x in list(input())]
    length = len(N)
    ans = pow(10, length-1)-1
    for word in range(1, length//2+1):
      if length%word != 0: continue
      count = length//word
      vals = [int("".join(N[word*j: word*(j+1)])) for j in range(count)]
      temp_ans = vals[0]
      temp = 0
      for i in range(count):
        temp += temp_ans*pow(10, i*word)
      if temp <= int("".join(N)):
        ans = max(ans, temp)
        continue

      temp_ans = vals[0]-1
      temp = 0
      for i in range(count):
        temp += temp_ans*pow(10, i*word)
      ans = max(ans, temp)

    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()