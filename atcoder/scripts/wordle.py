from collections import defaultdict
alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+ord('a'))

with open("/Users/nakazawa/Projects/solo/competitive_programing/atcoder/scripts/wordle_words.txt") as f:
  # five_char_words = [set(list(s[:-1].lower())) for s in f.readlines() if len(s) == 6]
  five_char_words = [s[:-1].lower() for s in f.readlines() if len(s) == 6]

N = len(five_char_words)
print(five_char_words)
# agg = defaultdict(int)
# for s in five_char_words:
#   for i in range(26):
#     c = num2alpha(i)
#     if c in s:
#       agg[c]+=1

# print(f'N = {N}')
# for i in range(26):
#   c = num2alpha(i)
#   print(f'{c}: {agg[c]/N*100:.2f}')

# print("ランキング")
# agg = sorted(list(agg.items()), reverse=True, key=lambda x: x[1])
# for k, v in agg:
#   print(f'{k}:{v/(N)*100:.1f}%')