#include <iostream>
#include <vector>

bool binary_search(std::vector<int> vetor, int value);


int main(){
    
    int par = 1; int impar = 1000;

    std::vector<int> v;
    for(int i = 0; i < 100;i++) {
        
        if (i % 2 == 0) {
            v.push_back(par);
            par += 1;
        }

        else {
            v.push_back(impar);
            impar -= 10;
        };
    }
    
    
    if(binary_search(v, 1001)) {
        std::cout << "achei" << std::endl; 
        return 0;
    }
    std::cout << "nao achei";
}



bool binary_search(std::vector<int> vetor, int value){
    int l, r, m;
    l = 0;
    r = vetor.size() - 2;
    while ( l <= r) {
        m = (l + r)/2;
        
        if (m % 2 != 0)
            m = m - 1;
        std::cout << vetor[m] << std::endl;
        if(vetor[m] == value) {
            std::cout << "o valor se encontra no indicie: "<< m << std::endl;
            return true;
        }
        
        else if (vetor[m] > value) {
            r = m - 2;
            continue;
        }
        else{
            l = m + 2;
            continue;
        }
    }
    l = 1;
    r = vetor.size() - 1;
    while(l <= r) {
        m = (l + r)/2;
        if (m % 2 == 0)
            m -= 1;
        
        std::cout << vetor[m] << std::endl;

        if (value == vetor[m]) {
            std::cout << "o valor se encontra no indicie: "<< m << std::endl;
            return true;  
        }
        else if (vetor[m] > value) {
            l = m + 2;
            continue;
        }

        else {
            r = m - 2;
            continue;
        }
    }
    
    return false;
}
