#include <iostream>
using namespace std;
int somar(int a, int b){
    int soma = a+b;
    return soma;
}
int main(){
    int n1,n2;
    cin >> n1;
    cin >> n2;
    cout << "X = "<< somar(n1,n2) << endl;
}