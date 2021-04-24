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
        input = """4 2 3"""
        output = """18"""
        self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """1000000000 987654321 123456789"""
    #     output = """951633476"""
    #     self.assertIO(input, output)

def resolve():
  base = 998244353
  A, B, C= map(int, input().split(" "))
  ans = 0
  for a in range(1, A+1):
    for b in range(1, B+1):
      for c in range(1, C+1):
        ans += a*b*c

  print(ans)

# if __name__ == "__main__":
#   resolve()


if __name__ == "__main__":
    unittest.main()
