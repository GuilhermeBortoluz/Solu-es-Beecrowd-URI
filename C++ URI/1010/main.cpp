#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    int c1,c2,n1,n2;
    double v1,v2;

    scanf("%d" "%d" "%lf", &c1, &n1, &v1);
    scanf("%d" "%d" "%lf", &c2, &n2, &v2);

    cout << fixed << setprecision(2);
    cout << "VALOR A PAGAR: R$ " << v1*n1+v2*n2 << endl;
    
    return 0;
}