class Solution {
public:
    int reverse(int x) {
        bool isNeg = (x<0);
        x = abs(x);

        auto num = std::to_string(x);
        std::reverse(num.begin(),num.end());

        long long rev = stoll(num) * (isNeg?-1:1);

        if (rev < (-1LL<<31) || (rev > (1LL<<31)-1))
        {
            return 0;
        }
        return static_cast<int>(rev);
    }
};
