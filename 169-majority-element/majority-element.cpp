class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> m;
        int n = nums.size();

        for (int i = 0; i < n; i++){
            m[nums[i]]++;
        }

        n /= 2;
        for(auto x:m){
            if(x.second > n){
                return x.first;
            }
        }

        return 0;
    }
};