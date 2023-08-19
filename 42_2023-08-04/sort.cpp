#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for(int _ = 0; _ < t; ++_)
    {
        int n;
        int arr[200000];
        int arr_odd[200000];
        int arr_even[200000];
        int even_i = 0;
        int odd_i = 0;

        cin >> n;

        for(int i = 0; i < n; ++i)
        {
            cin >> arr[i];

            if (arr[i] % 2 == 0){
               arr_even[even_i++] = arr[i];
            } else {
                arr_odd[odd_i++] = arr[i];
            }
        }
        sort(begin(arr_odd), begin(arr_odd) + odd_i);
        sort(begin(arr_even), begin(arr_even) + even_i);

        int answer[200000];

        even_i = 0;
        odd_i = 0;

        for(int i = 0; i < n; ++i)
        {
            if(arr[i] % 2 == 0)
            {
                answer[i] = arr_even[even_i++];
            } else {
                answer[i] = arr_odd[odd_i++];
            }
        }
        if (is_sorted(begin(answer), begin(answer) + n))
        {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    } 

    return 0;
}