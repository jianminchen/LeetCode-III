#include <unordered_map>
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_map <int, int> dic;
        for (int i = 0; i < nums.size(); i++)
        {
            if (dic.count(nums[i]) == 0)
                dic[nums[i]] = 0;
            dic[nums[i]] ++;
            if (dic[nums[i]] >= 3)
            {
                nums.erase(nums.begin() + i);
                i--;
            }
        }
        return nums.size();
    }
};
