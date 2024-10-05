#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    string nome;
    double vendas, fixo;
    cin >> nome >> fixo >> vendas;
    cout <<  fixed <<setprecision(2);
    cout << "TOTAL = R$ " << fixo+(vendas*0.15) << endl;
    return 0;
}