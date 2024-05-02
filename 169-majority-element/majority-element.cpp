class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::map<int, int> dict;

        for (auto i = nums.begin(); i !=nums.end(); ++i){
            dict[*i] = 0;
        }

        for (auto i = nums.begin(); i !=nums.end(); ++i){
            dict[*i] += 1;
        }

        int max = std::numeric_limits<int>::min();

        for (const auto& coppia : dict){
            if (coppia.second > dict[max]){
                max = coppia.first;
            }
        }
        return max;
    }
};