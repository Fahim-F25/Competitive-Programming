#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for(int value : nums){
            ans = ans ^ value; // using bitwise operator X-OR
        }
        return ans;
        
    }
};

int main() {
    Solution obj;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    vector<int> nums(n);
    cout << "Enter " << n << " numbers: ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int result = obj.singleNumber(nums);
    cout << "The single number is: " << result << endl;

    return 0;
}

