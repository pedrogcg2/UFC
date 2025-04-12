#include <iostream>
#include <vector>
#include <ctime>
#include <cmath>

void InsertionSort(std::vector<int> &vetor, int p, int r);
void HeapSort(std::vector<int> &v, int p, int r);
void heapify(std::vector<int> &v, int i, int p, int r);
void build_max_heap(std::vector<int> &v, int p, int r);



int main(){
    
       
    srand(time(NULL));
    std::vector<int> v, v2;
    for (int i = 0;i < 10;i++){
        v.push_back(std::rand()%100);
    }
    InsertionSort(v, 4, 10);   


    for (int i = 0;i < 10;i++){
        v2.push_back(std::rand()%100);
    }

    HeapSort(v2,4, 8);
    return 0;

}


void InsertionSort(std::vector<int> &vetor, int p, int r) {
    if (p > r) {
        InsertionSort(vetor, r, p);
        return;
    }
    
    std::cout << "vetor: " << std::endl;
    for(int i = 0;i < vetor.size();i++)
    {
        std::cout << vetor[i] << " ";
    }  
    
    std::cout << std::endl;
    
    for (int i = p + 1;i <= r;i++) {
        int j = i - 1;
        int key = vetor[i];
        while(key < vetor[j] && j >= p)
        {
            vetor[j + 1] = vetor[j];
            vetor[j] = key;
            j--;
        }
    }

    std::cout << "vetor ordenado: " << std::endl;
    for(int i = 0;i < vetor.size();i++)
    {
        std::cout << vetor[i] << " ";
    }
    return;
}


void HeapSort(std::vector<int> &v, int p, int r){
    if (p > r){
        HeapSort(v, r, p);
        return;
    }
    std::cout << std::endl;
    std::cout << "vetor: " << std::endl;
    for(int i = 0;i < v.size();i++)
    {
        std::cout << v[i] << " ";
    }  
    
    std::cout << std::endl;
    
    
    
    build_max_heap(v, p ,r);
    
    for(int i = r; i > p;i--)
    {
        int z = v[p];
        v[p] = v[i];
        v[r] = z;
        r--;
        heapify(v, p, p, r);
    }
    
    
    std::cout << "vetor ordenado: " << std::endl;
    for(int i = 0;i < v.size();i++)
    {
        std::cout << v[i] << " ";
    }

    return;

}


void heapify(std::vector<int> &v, int i, int p, int r){
    int left = (i - p)*2 + 1 + p;
    int right = (i - p)*2 + 2 + p;
    int bigger;

    if(left <= r && v[left] > v[i])
        bigger = left;
    else   
        bigger = i;

    if(right <= r && v[right] > v[i])
        bigger = right;
    
    if(v[bigger] != v[i])
    {
        std::cout << v[bigger] <<  " trocou de lugar com " << v[i] << std::endl;
        int z = v[i];
        v[i] = v[bigger];
        v[bigger] = z;
        heapify(v, bigger,p ,r);
    }
    return;
}



void build_max_heap(std::vector<int> &v, int p, int r)
{

    for (int i = (p+r) / 2; i >= p;i--)
    {
        heapify(v, i, p, r);
    }
    return;

}