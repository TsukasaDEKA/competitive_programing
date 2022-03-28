import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
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
snuke
snuke
takahashi
takahashi
takahashi"""
        output = """takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
takahashi
takahashi
aoki
takahashi
snuke"""
        output = """takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
a"""
        output = """a"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  N = int(input())
  agg = defaultdict(int)
  max_vote = 0
  for i in range(N):
    s = input()
    agg[s]+=1
    max_vote = max(max_vote, agg[s])

  for key, val in agg.items():
    if val != max_vote: continue
    print(key)
    return
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()