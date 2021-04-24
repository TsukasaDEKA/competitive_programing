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

#     def test_Sample_Input_1(self):
#         input = """1
# 3
# 120"""
#         output = """3"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
3
120
5
11011
6
600005"""
        output = """3
6
1"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  for _ in range(N):
    length_of_array = int(input())
    S = input()
    counter = S.count("1")
    list_S = [int(x) for x in list(S)]

    for window_size in range(2, length_of_array + 1):
      sum_value = sum(list_S[0:window_size])
      if sum_value == window_size:
        counter += 1

      for start in range(1, length_of_array-window_size+1):
        sum_value += list_S[start+window_size-1] - list_S[start-1]
        if sum_value == window_size:
          counter += 1

    print(counter)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
  unittest.main()