#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, k;
  cin >> n >> k;

  int ingots[100][2];

  for (int i = 0; i < n; ++i){
        cin >> ingots[i][0];
    }

  for (int i = 0; i < n; ++i){
        cin >> ingots[i][1];
    }

  int bag[101][10001];
  int bag_map[101][10001];
  for(int i = 0; i < n + 1; ++i){
    for(int j = 0; j < k + 1; ++j){
      bag[i][j] = 0;
      bag_map[i][j] = false;
    }
  }

  for(int i = 1; i < n + 1; ++i){
    int weight = ingots[i - 1][0];
    int price = ingots[i - 1][1];
    for(int j = 1; j < k + 1; ++j){
      if(weight > j){
        bag[i][j] = bag[i - 1][j];
      } else {
        int weight_with_new_ingot = bag[i - 1][j - weight] + price;
        bag[i][j] = max(bag[i - 1][j], weight_with_new_ingot);
        if (bag[i][j] == weight_with_new_ingot){
            bag_map[i][j] = true;
        }
      }
    }
  }
  int i = n;
  int j = k;
  vector<int> answer = {};

  while (i > 0){
    if (bag_map[i][j]){
        answer.push_back(i);
         j -= ingots[i - 1][0];
         i -= 1;

    } else {
        i -= 1;
    }
  }

  for (i = 0; i < answer.size(); i++)
  {
    cout << answer[i] << endl;
  }

  return 0;
}