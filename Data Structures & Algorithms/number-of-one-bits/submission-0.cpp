class Solution {
public:
    int hammingWeight(uint32_t n) {
        if (n==0) return 0;
        int oneCount=0;
        while (n){
            if (n&1){
                ++oneCount;
            }
            n = n>>1;
        }
        return oneCount;
    }
};
