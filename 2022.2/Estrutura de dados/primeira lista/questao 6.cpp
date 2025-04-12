#include <iostream> 
#include <ctime>
#include <cmath>
#include <vector>





class doubleStack {
    private:
        std::vector<int> v;
        int size;
        int first_top = -1;
        int second_top;
    public:
        doubleStack(int n){
            v.reserve(n);
            size = n;
            second_top = n;
        }

        int pop_first(){
            if(first_top > -1){
                int temp = v[first_top];
                first_top --;
                return temp;
            }
            else
                std::cout << "first stack is empty" << std::endl;
        }

        int pop_second(){
            if(second_top < size){
                int temp = v[second_top];
                second_top++;
                return temp;
            }
            else
                std::cout << "second stack is empty" << std::endl;
        }


        bool Full(){
            int second_size = size - second_top;
            int first_size = first_top + 1;
            if ((second_size + first_size) < size){
                
                return false;
            }
            return true;
        }


        void push_first(int value){
            if (Full()){
                std::cout << "not enough memory :/" << std::endl;
                return;
            }

            first_top++;
            v[first_top] = value;
        }

        void push_second(int value){
            if(Full()){
                std::cout << "not enough memory :/" << std::endl;
                return;
            }

            second_top--;
            v[second_top] = value;
        }

        void print_stack(){
            if(first_top > -1){
                std::cout << "primeira pilha: " << std::endl;
                for (int i = 0; i <= first_top;i++){
                    std::cout << v[i] << " ";
                }
            }
            else
                std::cout <<"primeira pilha vazia" << std::endl;

            std::cout << std::endl;
            
            if (second_top < size){
                std::cout << "segunda pilha: " <<std::endl;
                for (int i = size - 1; i >= second_top;i--){
                    std::cout << v[i] << " ";
                }     
            }
            else
                std::cout <<"segunda pilha vazia" << std::endl;
        }
};

int main()
{
    doubleStack n(10);
    for(int i = 0;i < 15;i++)
    {
        n.push_first(i);
    }
    n.push_second(10);
    n.print_stack();
}