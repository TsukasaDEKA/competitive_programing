#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int resolve(){
  int N;
  cin >> N;

  int u, v;
  vector<vector<int>> EDGES(N);
  for(int i = 0; i < N; i++){
    cin >> u >> v;
    u -= 1;
    v -= 1;
    EDGES[u].push_back(v);
    EDGES[v].push_back(u);
  }

  // 頂点 i が閉路に含まれるかを判定する。
  vector<bool> is_in_circle(N);
  vector<int> degrees(N);
  vector<int> stack;  
  for(int i = 0; i < N; i++){
    degrees[i] = EDGES[i].size();
    if(degrees[i] == 1) stack.push_back(i);
    is_in_circle[i] = degrees[i] != 1;
  }

  int current;
  while(stack.size()){
    current = stack.back();
    stack.pop_back();

    for(auto e: EDGES[current]){
      if(!is_in_circle[e]) continue;
      if(degrees[e] == 1) continue;
      degrees[e] -= 1;
      if(degrees[e] == 1){
        is_in_circle[e] = false;
        stack.push_back(e);
      }
    }
  }

  // roots[i]: 頂点 i 閉路上のどの頂点に紐付いているか。閉路上の頂点は roots[i] = i になる。
  vector<int> roots(N);
  vector<bool> checked(N);
  for(int i = 0; i < N; i++){
    checked[i] = is_in_circle[i];
  }
  for(int i = 0; i < N; i++){
    if(!is_in_circle[i]) continue;
    roots[i] = i;
    stack.push_back(i);
    while(stack.size()){
      current = stack.back();
      stack.pop_back();
      for(auto e:EDGES[current]){
        if(checked[e]) continue;
        checked[e] = true;
        stack.push_back(e);
        roots[e] = i;
      }
    }
  }

  // クエリの処理
  int Q;
  cin >> Q;
  for(int i = 0; i < Q; i++){
    cin >> u >> v;
    u -= 1;
    v -= 1;
    cout << ((roots[u] == roots[v])? "Yes":"No") << endl;
  }
  return 0;
}

int main(){
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  return resolve();
}