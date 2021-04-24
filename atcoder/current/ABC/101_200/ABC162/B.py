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
        input = """15"""
        output = """60"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """1000000"""
        output = """266666333332"""
        self.assertIO(input, output)

def resolve():
N = int(input())
num_list = []
for i in range(1, N+1):
  if not(i%3 == 0 or i%5 == 0):
    num_list.append(i)
print(sum(num_list))

if __name__ == "__main__":
    unittest.main()