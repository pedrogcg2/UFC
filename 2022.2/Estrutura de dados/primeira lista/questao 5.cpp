void reverte_lista(node* cabeça)
    {
        
        Node* atual = cabeça;
        Node *ant = NULL, *prox = NULL;
 
        while (atual != NULL) {
            // Store next
            prox = atual->prox;
            // Reverse current node's pointer
            atual->prox = ant;
            // Move pointers one position ahead.
            ant = atual;
            atual = prox;
        }
        cabeça = ant;
    }