#include <iostream>
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void prll_1d(vector<ll> a){for (auto b:a){cout<<b<<" ";}cout<<endl;}
void prll_2d(vector<vector<ll>> a){for (auto b:a){prll_1d(b);};cout<<endl;}

vector<vector<ll>> permutations(vector<ll> lis){
    vector<ll> range,tmp(lis.size(),0);
    vector<vector<ll>> ans;

    for(ll i=0  ;i<lis.size()  ;i++){
        range.push_back(i);
    }

    do{
        for(ll i=0  ;i<lis.size()  ;i++){
            tmp[range[i]]=lis[i];
        }
        ans.push_back(tmp);
    }while (next_permutation(range.begin(), range.end()));
    return ans;
}

ll resolve(){
  ll N;
  cin >> N;

  vector<ll> A(N);
  for(ll i = 0; i < N; i++){
    cin >> A.at(i);
  }
  sort(A.begin(), A.end(), greater<ll>());

  vector<ll> top_3(3);
  for(ll i = 0; i < 3; i++){
    top_3[i] = A[i];    
  }

  ll ans = 0;
  for(auto const numbers:permutations(top_3)){
    string temp;
    for(auto number:numbers){
      temp = temp + to_string(number);
    }
    ans = max(ans, stoll(temp));
  }
  cout << ans << endl;

  return 0;
}

int main(){
  // 
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  return resolve();
}