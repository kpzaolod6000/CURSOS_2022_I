#include <bits/stdc++.h>
// for std::complex, std::real, std::imag
//#include <complex>

using namespace std;

/*
* Euler
*/

complex<double> euler(double angle){
    double a = cos(angle);
    double b = sin(angle);
    complex<double> result(a,b);

    return result;
}


vector<double> Fourier(vector<double> fs, int u){
    int n = fs.size();

    double sumImag = 0;
    double sumReal = 0;
    double pi1 = 180;//double pi1 = 3.14;

    for (int x = 0; x < n; x++)
    {
        double expo = (pi1*u*x)/n;

        if (expo == 0)
        {
            cout<<"onicha"<<endl;
            sumReal += fs[x];
        }else{
            complex<double> imgry = euler(expo);
            sumReal += (fs[x] * 1/(real(imgry)));
            sumImag += (fs[x] * 1/(imag(imgry)));
        }
    }
    return {sumReal,sumImag};
}



int main(int argc, char const *argv[])
{
    // complex<double>  eulerResult = euler(50); 
    // cout<<eulerResult<<endl;
    // cout << "Real part: " << real(eulerResult) << endl;
    // cout << "Imaginary part: " << imag(eulerResult) << endl;
    
    //vector<double> fs = {0,0.707,1,0.707,0,-0.707,-1,-0.707};
    vector<double> fs = {1,2,4,4};
    vector<double> result = Fourier(fs,1); 
    cout<<result[0]<<" "<<result[1]<<endl;
    cout<<4 + 4j<<endl;
    //cout<<fs.size()<<endl;
    return 0;
}
