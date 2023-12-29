#include <iostream>

using namespace std;

int f (int p, int q)

{

if (p>q)

return p;

else

return q;

}

main ()

{

int a=5, b=10;

int k;

bool x=true;

bool y=f(a,b);

k=((a*b)+(x+y));

cout << k;

}