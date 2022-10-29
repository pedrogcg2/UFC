#include <iostream>
#include <string>


struct node{
    char value;
    node* parent;
    node* left;
    node* right;

    node(char letter){
        value = letter;
        parent = NULL;
        left = NULL;
        right = NULL;
    }
    
};

class tree {
    node* root;
    
    
    std::string space_remove(std::string exp){
        for(int i = 0;i < exp.length();i++){
            if(exp[i] == ' '){
                exp.erase(i, 1);
                i--;
            }
        }
        return exp;
    }
    
    void insertion(std::string exp){
            exp = space_remove(exp);
            node* current;
            node* parent;
            node* prev;


            for(int i = 0;i < exp.length();i++){   

                //cria uma subarvore
                if(exp[i] == '('){
                    if(root == NULL){
                        continue;
                    }
                
                    parent = current;
                    prev = current;
                    current = current->left;
                    
                    while(current != NULL){
                        prev = current;
                        current = current->right;
                    }

                }
                
                //encerra uma subarvore
                else if(exp[i] == ')'){
                    current = current->parent;
                }

                //insere o no
                else {
                    node* p = new node(exp[i]);
                    
                    if(root == NULL){
                        root = p;
                    }
                    
                    else{

                        p->parent = parent;
                        
                        if(prev->left == current){
                            prev->left = p;
                        }
                        
                        else if (prev->right == current){
                            prev->right = p;
                        }
                    }                  
                }
            }
    }
    
    public:
       
        tree(std::string exp){
            insertion(exp);
        }

        
        


        /*void imprime(){
            node* current = root;
            node* prev = NULL;
            while(current != NULL){
                while(current->left != NULL){
                    std::cout << current->value << ' ';
                    prev = current;
                    current = current->left;
                }
            
                while(current->right != NULL){
                    std::cout << current->value << ' ';
                    current = current->right;
                }
                current = prev->right;            
            }
        }
        */
    };
        



int main(){

    tree a("(a (b(d)(e)) (c(f)(g)) ))");
    //a->imprime();

    return 0;
}