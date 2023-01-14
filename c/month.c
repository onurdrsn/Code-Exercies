#include <stdio.h>
#include <stdlib.h>

void ft_month(){
    
    int ay;

    printf("Ayin numarasini giriniz: ");
    scanf("%d", &ay);

    switch(ay){
        case 1:
            printf("Girilen değer: %d -> Ocak/January", ay);
        break;

        case 2:
            printf("Girilen değer: %d -> Şubat/February", ay);
        break;

        case 3:
            printf("Girilen değer: %d -> Mart/March", ay);
        break;

        case 4:
            printf("Girilen değer: %d -> Nisan/April", ay);
        break;
    }
}

int main(void){
    ft_month();

    return 0;
}