#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;
#define pi 3.14159
int main(){
    double r;
    cin >> r;
    double vol= (4.0/3.0)*pi*pow(r,3);
    cout << fixed << setprecision(3);
    cout << "VOLUME = " <<vol<< endl;
    return 0;
}