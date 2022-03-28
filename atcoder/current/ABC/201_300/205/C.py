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
        input = """3 2 4"""
        output = """>"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """-7 7 2"""
        output = """="""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """-8 6 3"""
        output = """<"""
        self.assertIO(input, output)


def resolve():
  A, B, C = map(int, input().split(" "))
  # C = 1 if C%2 else 2
  A = pow(A, C)
  B = pow(B, C)
  if A == B:  print("=")
  elif A > B: print(">")
  else: print("<")
  # if A >= 0 and B >= 0:
  #   if A == B:
  #     print("=")
  #   elif A > B:
  #     print(">")
  #   else:
  #     print("<")
  #   return

  # if A == 0:
  #   if C%2: print(">")
  #   else: print("<")

  # if B == 0:
  #   if C%2: print(">")
  #   else: print("<")

  # if A < 0 and B < 0:
  #   A = abs(A)
  #   B = abs(B)
  #   if C%2:
  #     if A == B:
  #       print("=")
  #     elif A > B:
  #       print("<")
  #     else:
  #       print(">")
  #     return
  #   else:
  #     if A == B:
  #       print("=")
  #     elif A > B:
  #       print(">")
  #     else:
  #       print("<")
  #     return
  
  # if A > 0:
  #   if C%2:
  #     if A == B:
  #       print("=")
  #     else:
  #       print(">")
  #     return
  #   else:
  #     A = abs(A)
  #     B = abs(B)
  #     if 
  #     if A == B:
  #       print("=")
  #     elif A > B:
  #       print("<")
  #     else:
  #       print(">")
  #     return
  # hoge

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
