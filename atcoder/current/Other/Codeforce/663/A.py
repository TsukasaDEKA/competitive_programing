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
1
3
20"""
        output = """1
3 1 2
4 3 5 2 7 1 6"""
        self.assertIO(input, output)

def resolve():
  N = int(input())

  for _ in range(N):
    inputed_number = int(input())
    result = []
    for i in reversed(range(1, inputed_number+1)):
      result.append(str(i))
    
    print(" ".join(result))

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
  unittest.main()