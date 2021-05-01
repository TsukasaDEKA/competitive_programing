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

    def test_入力例_1(self):
        input = """5
e869120
atcoder
e869120
square1001
square1001"""
        output = """1
2
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
taro
hanako
yuka
takashi"""
        output = """1
2
3
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  users = set()

  for i in range(N):
    S = input()
    if S in users: continue
    users.add(S)
    print(i+1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
