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

    def test_入力例1(self):
        input = """5
1
2
3
2
1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """11
3
1
4
1
5
9
2
6
5
3
5"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
from collections import Counter
N = int(input())
print(sum([v-1 for v in Counter([input() for _ in range(N)]).values()]))

# resolve()

if __name__ == "__main__":
    unittest.main()
