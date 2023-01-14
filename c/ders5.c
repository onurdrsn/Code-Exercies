#include <stdlib.h>
#include <stdio.h>

int main(){
	int sayi;
	char ad[20];
	printf("Adinizi giriniz: ");
	scanf("%s", &ad); //& ifadesi klavyeden girileni görmek için kullanilir.
	printf("Yaşinizi giriniz: ");
	scanf("%d", &sayi);
	printf("Adiniz: %s\n", ad);
	printf("Yaşiniz: %d", sayi);
	return 0;
}
