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
        input = """aca
accc
ca"""
        output = """A"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """abcb
aacb
bccc"""
        output = """C"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  hands = {
    "a": deque(list(input())),
    "b": deque(list(input())),
    "c": deque(list(input()))
  }
  next_ = "a"
  while hands[next_]: next_ = hands[next_].popleft()
  print(next_.upper())

resolve()

if __name__ == "__main__":
    unittest.main()
