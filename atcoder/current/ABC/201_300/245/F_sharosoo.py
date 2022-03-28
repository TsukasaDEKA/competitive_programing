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
        input = """5 5
1 2
2 3
3 4
4 2
4 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
1 2
2 1"""
        output = """2"""
        self.assertIO(input, output)

import sys
from collections import deque
input = sys.stdin.readline
 
def sol():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]
    out_degree = [0] * (n)
    for _ in range(m):
        l, r = map(int, input().split())
        edges[r-1].append(l-1)
        out_degree[l-1] += 1
 
    q = deque()
    ans = n
 
    for i in range(n):
        if not out_degree[i]:
            q.append(i)
 
    while q:
        ans -= 1
        cur = q.popleft()
        for next in edges[cur]:
            out_degree[next] -= 1
            if not out_degree[next]:
                q.append(next)
 
    return ans

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()