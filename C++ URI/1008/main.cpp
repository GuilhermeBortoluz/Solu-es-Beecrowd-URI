#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    int num, horas;
    float salario_hora;
    cin >> num;
    cin >> horas;
    cin >> salario_hora;
    cout << "NUMBER = " << num << '\n';
    cout << fixed << setprecision(2);
    cout << "SALARY = U$ " << horas*salario_hora << endl;
    return 0;
}