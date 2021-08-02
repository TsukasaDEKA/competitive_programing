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
        input = """5
2
1
01
1
0010"""
        output = """01
1
1
2
0010"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
1111111111111111111111
00011111111111111111111
000000111111111111111111
0000000001111111111111111
00000000000011111111111111
000000000000000111111111111"""
        output = """000000000000000111111111111
00000000000011111111111111
0000000001111111111111111
000000111111111111111111
00011111111111111111111
1111111111111111111111"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
0010
1
01
2
1
10"""
        output = """01
1
1
2
0010
10"""
        self.assertIO(input, output)

def resolve():
  # なんかバグらせてるっぽい
  N = int(input())
  S = [input() for _ in range(N)]
  ans = {}
  ans_indexes = set()
  for s in S:
    int_s = int(s)
    if int_s in ans:
      ans[int_s].append(s)
    else:
      ans[int_s] = [s]
      ans_indexes.add(int_s)

  ans_indexes = list(ans_indexes)
  ans_indexes.sort()
  for ans_index in ans_indexes:
    ans[ans_index].sort()
    print(*ans[ans_index], sep="\n")
      
# resolve()

if __name__ == "__main__":
    unittest.main()
