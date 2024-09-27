#include <iostream>
#include <math.h>
#include <iomanip>
#define pi 3.14159
int main(){
    double raio;
    std::cin >> raio;
    std::cout << std::fixed << std::setprecision(4);
    std::cout<<"A=" <<pi*pow(raio,2)<<"\n";
    return 0;
}