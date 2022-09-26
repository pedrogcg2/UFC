void printPostorder(struct Node* node)
{
    if (node == NULL)
        return;
  
    // first recur on left subtree
    printPostorder(node->left);
  
    // then recur on right subtree
    printPostorder(node->right);
  
    // now deal with the node
    cout << node->data << " ";
}
  
/* Given a binary tree, print its nodes in inorder*/
void printInorder(struct Node* node)
{
    if (node == NULL)
        return;
  
    /* first recur on left child */
    printInorder(node->left);
  
    /* then print the data of node */
    cout << node->data << " ";
  
    /* now recur on right child */
    printInorder(node->right);
}
  
/* Given a binary tree, print its nodes in preorder*/
void printPreorder(struct Node* node)
{
    if (node == NULL)
        return;
  
    /* first print data of node */
    cout << node->data << " ";
  
    /* then recur on left subtree */
    printPreorder(node->left);
  
    /* now recur on right subtree */
    printPreorder(node->right);
}
  