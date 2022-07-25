#include <stdlib.h>
#include <stdio.h>

int main(){
	int sayi;
	char ad[20];
	printf("Adınızı giriniz: ");
	scanf("%s", &ad); //& ifadesi klavyeden girileni görmek için kullanılır.
	printf("Yaşınızı giriniz: ");
	scanf("%d", &sayi);
	printf("Adınız: %s\n", ad);
	printf("Yaşınız: %d", sayi);
	return 0;
}
