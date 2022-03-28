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

#     def test_Sample_Input_1(self):
#         input = """13
# 62"""
#         output = """131"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """69120
824"""
        output = """869120"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6283185
12566370"""
        output = """6283185"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1
1"""
        output = """6283185"""
        self.assertIO(input, output)

def resolve():
  A = int(input())
  B = int(input())

  B*=5

  s_A = str(A)
  s_B = str(B)
  if s_A.find(s_B) >= 0:
    print(s_A)
    return
  if s_B.find(s_A) >= 0:
    print(s_B)
    return

  ans = B + A*pow(10, len(str(B))+1)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()