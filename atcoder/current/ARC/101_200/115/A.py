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
        input = """3 2
00
01
10"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 5
10101
00001
00110
11110
00100
11111
10000"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  S = [input().count("1")%2 for _ in range(N)]
  ans = [1 for s in S if s==1]
  print((N-len(ans))*len(ans))

resolve()

if __name__ == "__main__":
    unittest.main()
