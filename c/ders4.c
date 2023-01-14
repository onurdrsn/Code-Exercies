#include <stdio.h>
#include <math.h>
 
 int main(void)
 {
     int taban, yukseklik, hipotenus, cevre, alan, hipothesap;
     double c;
     //özel üçgen
     taban = 8;
     yukseklik = 15;
     hipotenus = 17;
     cevre = taban + yukseklik + hipotenus;
     alan = (yukseklik * hipotenus) / 2;
     hipothesap = taban*taban + yukseklik*yukseklik;
     printf("Üçgenin Çevresi: %d\n", cevre);
     printf("Üçgenin Alani: %d\n", alan);
     printf("Hipotenüsün Kendisini Bulma: %2.f\n", sqrt(hipothesap));

     return 0;
 }