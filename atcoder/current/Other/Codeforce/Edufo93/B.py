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
#     def test_Sample_Input_1(self):
#         input = """5
# 01111001
# 0000
# 111111
# 101010101
# 011011110111"""
#         output = """4
# 0
# 6
# 3
# 6"""
#         self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """4
1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"""
        output = """25
25
25
25"""
        self.assertIO(input, output)

import re

def resolve():
  N = int(input())
  for _ in range(N):
    S = input()
    splitted_S = sorted([x.count("1") for x in re.split('0+', S)])

    print(sum(splitted_S[::-2]))

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
  unittest.main()