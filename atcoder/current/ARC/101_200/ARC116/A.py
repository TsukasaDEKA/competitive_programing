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
2
998244353
1000000000000000000"""
        output = """Same
Odd
Even"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """2
# 2
# 998244353"""
#         output = """Same
# Odd"""
#         self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  T = int(input())
  # 2 で割れるかどうか

  for _ in range(T):
    A = int(input())
    if A%2:
      print("Odd")
    else:
      if A%4:
        print("Same")
      else:
        print("Even")
resolve()

if __name__ == "__main__":
    unittest.main()
