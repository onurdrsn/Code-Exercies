#include <stdio.h>
#include <math.h>

int main(){
    int bagajdeger, eldeger, kg;
    printf("Uçak bagaj kapasite değeri giriniz: ");
    scanf("%d", &bagajdeger);
    printf("Uçak el kapasite değeri giriniz: ");
    scanf("%d", &eldeger);
    //printf("Girilen Bagaj değeri: %d", bagajdeger);v
    if(bagajdeger > 15 || eldeger > 8){
        bagajdeger = bagajdeger - 15;
        eldeger = eldeger - 8;
        kg = (bagajdeger + eldeger) * 5;
        printf("Ödemiş olacağınız toplam ücret: %d tl", kg);
    }
    if(bagajdeger == 15 & eldeger == 8){

        printf("Tam kapasiteyle doldurulmuştur hiçbir ücret ödemenize gerek yoktur.");
    }
    if(bagajdeger < 15 & eldeger < 8){
        bagajdeger = 15 - bagajdeger;
        eldeger = 8 - eldeger;
        printf("-----Bagaj ve el kapasitesi dolmamıştır-----\nDaha doldurulması gereken bagaj kapasitesi: %d\n", bagajdeger);
        printf("Daha doldurulması gereken el kapasitesi: %d", eldeger);
    }
    return 0;

}