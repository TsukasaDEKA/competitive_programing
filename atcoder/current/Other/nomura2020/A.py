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
        input = """10 0 15 0 30"""
        output = """270"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 0 12 0 120"""
        output = """0"""
        self.assertIO(input, output)

def time_to_min(H, M):
  return H * 60 + M


def resolve():
  H1, M1, H2, M2, K= map(int, input().split(" "))
  start = time_to_min(H1, M1)
  end = time_to_min(H2, M2)
  print(end - start - K)

# if __name__ == "__main__":
#     resolve()


if __name__ == "__main__":
    unittest.main()
