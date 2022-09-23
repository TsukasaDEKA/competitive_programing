from collections import deque
# なもりグラフの閉路に含まれる頂点かどうかを判定して [boolean]*N の配列で返す。
# 無向グラフのみ対応している。
# edges[n] := 頂点 n に直接繋がっている頂点の index
def is_in_cycle_of_namori_graph(N, edges):
  # 次数を求める。
  degrees = [len(x) for x in edges]

  result = [d != 1 for d in degrees]
  que = deque([i for i in range(N) if degrees[i] == 1])
  while que:
    current = que.pop()
    for e in edges[current]:
      if not result[e]: continue
      degrees[e] -= 1
      if degrees[e] == 1:
        result[e] = False
        que.append(e)

  return result


