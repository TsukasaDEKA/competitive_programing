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
        input = """3"""
        output = """ACLACLACL"""
        self.assertIO(input, output)

def resolve():
  N = int(input())

  for _ in range(N):
    print("ACL", end="")
  print("")

if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
