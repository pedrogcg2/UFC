#include <iostream>
#include <string>


void func(std::string exp)
{
    std::cout << exp.length() << std::endl;;

}

std::string remove_espaco(std::string exp){
        for(int i = 0;i < exp.length();i++){
            if(exp[i] == ' '){
                exp.erase(i, 1);
                i--;
            }
        }
        return exp;
    }
int main(){
    
    std::string exp = "pe dr    o";
    func(exp);

    std::cout << exp << std::endl;
    std::cout << remove_espaco(exp);
    return 0;
}