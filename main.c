
//1
#include  <stdio.h>
int main() {
    printf("Hello, World!")  
}

//2

#include  <stdio.h>
int main() {
    int s1, s2, carpim;
    printf("lütfen bir sayı girin: ");
    scanf("%d", &s1);
    printf("2.sayı: ");
    scanf("%d", &s2);
    carpim = s1*s2;
    printf("sonuc: %d", carpim);

}
//3
#include  <stdio.h>
int main() {
    int snot;
    printf("gir");
    scanf("%d", &snot);
if (snot >= 50) {
    printf("sınavdan geçtin oc");
    } else {
    printf("sınavdan kaldın oc");
    }
}

//4

#include <stdio.h>
int main () {
    int i;
    for(i=0; i<=10; i++) {
        printf("%d\n", i);
    }
}

//5

#include <stdio.h>
int main () {

while (3<5) {
    printf("3<5");
}

}


//6

#include <stdio.h>
void printHello() {
    printf("Hello World");
}

int main()
{
    printHello();
}


#include <stdio.h>
void carp(int x, int y) {
    printf("1. Sayı: ");
    scanf("%d", &x);
    printf("2. Sayı: ");
    scanf("%d", &x);

    int z = x * y;
    printf("Sonuç: %d", z);
    
}

int main()
{
    carp(3, 5);
}
