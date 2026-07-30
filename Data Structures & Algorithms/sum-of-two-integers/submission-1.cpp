class Solution {
    std::pair<int,int> add(int a, int b, int c){
        int r,carry;
        if (not c){
            r = (a^b)!=0?1:0;
            carry = (a&b)!=0?1:0;
        }else{
            r = (a==b)?1:0;
            carry = (a|b)!=0?1:0;
        }
        //std::cout <<"\t add("<<a<<"+"<<b<<"+"<<c<<")=("<<r<<","<<carry<<")"; 
        return std::pair<int,int>(r,carry);
    }

public:
    int getSum(int a, int b) {
        int result=0,carry=0;
        int mask=1;
        for(auto i=0;i<32;i++){
            int _a = a & (1<<i);
            int _b = b & (1<<i);
            //std::cout <<"carry:"<<carry<<std::endl;
            auto r = add(_a,_b,carry);
            result |= (r.first)<<i;
            carry = r.second;
        }
        //std::cout << "\n result:" << result <<" carry:" << carry;
        return result;
    }
};
