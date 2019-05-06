 void main(){
    for(int i = 1; i<10; i ++){
        for(int j = 1; j <10; j ++){
            for(int k = 1; k <10; k ++){
                if((i!= j)&&(j!= k)&&(i!= k)){
                    int sum = i * 100 + j * 10 + k;
                    int sum2 = sum * 2;
                    int sum3 = sum * 3;
                    if(sum * 3 <1000){
                        int aa [9];
                        aa [0] = sum2 / 100; aa [1] = sum2 / 10%10; aa [2] = sum2%10; aa [3] = sum3 / 100;
                        aa [4] = sum3 / 10%10; aa [5] = sum3%10; aa [6] = i; aa [7] = j; aa [8] = k;
                        int flag = 0;
                        for(int l = 0; l <9; l ++)
                        {
                            for(int m = l + 1; m <10; m ++)
                            {
                                if(aa [l] == aa [m])
                                {
                                    flag = 0;
                                    break;
                                }
                                else {
                                    flag = 1;
                                }
                            }
                            if(flag== 0)
                            {
                                break;
                            }
                        }
                        if(flag== 1)
                        {
                            printf("%d%d%d \n"，sum，sum2，sum3);
                        }
                    }}}}}}
