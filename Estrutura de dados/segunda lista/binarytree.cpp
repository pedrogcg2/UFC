#include <iostream>

struct node {
    int value;
    int height;
    node* parent;
    node* right;
    node* left;
    node(int value){
        this->value = value;
        parent, right, left = NULL;
    }
};

class binary_tree {
    node* raiz;

    node*  position_search(int value){
            node* current = raiz;
            while(current != NULL){
                if (value = current->value)
                {
                    return current;
                }
                else if (value > current->value)
                {
                    current = current->right;
                }
                else
                {
                    current = current->left;
                }
            }
            return NULL;
       }
    
    
    public:
        binary_tree(int value){
            raiz = new node(value);
        }

        bool search(int num)
        {
            if(position_search(num)!= NULL)
                return true;
            return false
        }
        
        
        
        
        node* min(node* n){
            node* prev = NULL;
            while(n != NULL){
                prev = n;
                n  = n->left;
            }
        
            return prev;
        }

        node* max (node* n){
            node* prev = NULL;
            while(n !=  NULL)
            {
                prev = n;
                n = n->right;
            }

            return prev;
        }


        node* sucessor(node* n){
            if(n->right != NULL){
                return min(n->right);
            }
            return NULL;
        }

        node* predecessor(node* n){
            if(n->left != NULL){
                return max(n->left);
            }
            return NULL;
        }

        void insertion(int value){
            node* p = new node(value);
            node* current = raiz; 
            node* prev = NULL;
            
            while (current != NULL){
                if (p->value > current->value) {
                    prev = current;
                    current = current->right;
                }
                else {
                   prev = current;
                   current = current->left;
                }
            }
            p->parent = prev;
            if(p->value > prev->value)
                prev->right = p;
            else
                prev->left = p;
        }


        void transplant(node* u, node* v){
            if (u->parent == NULL){
                raiz = v;
            }
            else if(u->value < u->parent->value){
                u->parent->left = v;
            }
            else{
                u->parent->right = v;
            }
            if(v != NULL){
                v->parent = u->parent;
            }
        }


        void remove(int value){
            node *n =  position_search(value);
            
            
            //primeiro caso
            if(n->right == NULL && n->left == NULL) {
                transplant(n, NULL);
            }

            //segundo caso
            else if(n->right == NULL && n->left != NULL)
            {
                transplant(n, n->left);
            }
            
            else if(n->left == NULL && n->right != NULL)
            {
               transplant(n, n->right);
            }

            //terceiro caso
            else {
                node* next = sucessor(n);
                if  (next != n->right){
                    transplant(next, next->right);
                    next->right = n->right;
                    next->right->parent = next;
                }
                transplant(n, next);
                next->left = n->left;
                next->left->parent = next;
            }
        }
            
};  



int main(){
    binary_tree p(4);
    p.insertion(2);
}