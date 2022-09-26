#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>


void heapSort(std::vector<int> &v);
void heapify(std::vector<int> &v, int n, int i);
void build_min_heap(std::vector<int> &v);

int main(){
    srand(time(NULL));
    std::vector<int> v, v2;
    std::cout<< "vetor: " << std::endl;
    for (int i = 0;i < 7;i++){
        v.push_back(i);
        std::cout << v[i] << ' ';
    }
    std::cout << std::endl;
    heapSort(v);   
}


void heapSort(std::vector<int> &v) {
    build_min_heap(v);
    int temp;
    int size = v.size() - 1;

    for (int i = 0; i < v.size();i++)
    {
        std::cout << i << std::endl;
        temp = v[i];
        v[i] = v[size];
        v[size] = temp;
        heapify(v, i + 1, size);   
    }

    std::cout << "vetor ordenado" << std::endl;
    for (int i = 0; i < v.size(); i++) {

        std::cout << v[i] << ' ';
    }

}

void heapify(std::vector<int> &v, int n, int i) {

int left = 2*i - (v.size() - 1) - 1;
int right = left - 1;
int small = i;


if (left >= n && v[left] < v[small]){
    small = left;
}
if(right >= n && v[right] < v[small]) {
    small = right;
}


if(v[small] != v[i])
{
    int temp = v[i];
    v[i] = v[small];
    v[small] = temp;

    heapify(v, n, small);
    //heapify(v, i);
}

return;
}

void build_min_heap(std::vector<int> &v)
{
    int size = v.size()/2;
    for(int i = size;i < v.size();i++)
    {
         
        heapify(v, 0, i);
    }


    std::cout << "heap minimo: " << std::endl; 

    for (int i = 0; i < v.size(); i++) {

        std::cout << v[i] << ' ';
    }

    std::cout << std::endl;

}