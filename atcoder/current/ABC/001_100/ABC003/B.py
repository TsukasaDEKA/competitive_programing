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
        input = """ch@ku@ai
choku@@i"""
        output = """You can win"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aoki
@ok@"""
        output = """You will lose"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """arc
abc"""
        output = """You will lose"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = list(input())
  T = list(input())
  atcoder = list("atcoder")
  for s, t in zip(S, T): 
    if s == t: continue
    if s == "@" and t in atcoder: continue
    if t == "@" and s in atcoder: continue
    print("You will lose")
    return
  print("You can win")

resolve()

if __name__ == "__main__":
    unittest.main()
