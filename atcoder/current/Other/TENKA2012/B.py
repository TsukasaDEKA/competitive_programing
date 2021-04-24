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
        input = """CQSAS10SQH10SKSJD3"""
        output = """CQH10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """S10SJSQSKSAC2"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # 54 枚程度なのでゴリ押しでいける。
  from collections import defaultdict
  S = list(input())
  rsf = set(["A", "10", "J", "Q", "K"])
  marks = set(["S", "H", "D", "C"])
  numbers = set(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
  cards = []
  hands = defaultdict(int)

  i = 0
  ans_key = ""
  while i < len(S)-1:
    if S[i] in marks:
      if S[i+1] in numbers:
        cards.append("".join(S[i:i+2]))
        i+=2
      else:
        cards.append("".join(S[i:i+3]))
        i+=3
      if cards[-1][1:] in rsf:
        hands[cards[-1][0]]+=1
        if hands[cards[-1][0]] == 5:
          ans_key = cards[-1][0]
          break
  ans = []
  for card in cards:
    if card[0] != ans_key or (card[1:] not in rsf) : ans.append(card)
  if len(ans): print(*ans, sep="")
  else: print(0)

resolve()

if __name__ == "__main__":
    unittest.main()
