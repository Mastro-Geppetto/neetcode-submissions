class Solution {
public:
    int reverse(int x) {
        int MAX = (1<<31)-1;
        int MIN = (-1)*(1<<31);
        std::cout <<"Max:Min=" <<MAX<<":"<<MIN
            << std::endl;

       int result=0;
       while( x != 0 ){
        int lsb = x%10;
        std::cout << lsb <<":";
        x = x/10;
        // check result
        if (result > MAX/10 || \
            (result == MAX/10 && lsb > MAX%10) )
            {
                return 0;
            }
        if (result < MIN/10 || \
            (result == MIN/10 && lsb < MIN%10) )
            {
                return 0;
            }
        result = (result*10) + lsb;
       }

       std::cout << " result " <<std::endl;
       return result;
    }
};
