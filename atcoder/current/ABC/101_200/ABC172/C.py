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
        input = """3 4 240
60 90 120
80 150 80 150"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 4 730
60 90 120
80 150 80 150"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 4 1
1000000000 1000000000 1000000000 1000000000 1000000000
1000000000 1000000000 1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
  N, M, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]

  if A[0] > K and B[0] > K:
    print(0)
    return True 

  integraA = [0]
  for i in range(N):
    integraA.append(A[i] + integraA[i])

  integraB = [0]
  for i in range(M):
    integraB.append(B[i] + integraB[i])

  ans = 0
  B_index = M
  for A_index in range(N + 1):
    if integraA[A_index] > K:
      break

    # print(A_index, ":", B_index)
    # print(integraB[B_index], "<", K - integraA[A_index])
    while integraB[B_index] > K - integraA[A_index]:
      B_index -= 1
    ans = max(ans, A_index + B_index)
  print(ans)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
