class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> a;
        vector<int> b{0, 0};
        for(int i = 0; i < nums.size(); i++){
            a.insert(map<int, int>::value_type(nums[i], i));
        }
        for(int i = 0; i < nums.size(); i++){
            if(a.count(target - nums[i]) > 0 && a[target - nums[i]] != i){
                b[0] = i;
                b[1] = a[target - nums[i]];
                break;
            }
        }
        return b;
    }
};