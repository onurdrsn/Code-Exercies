#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;
void rules();

int main()
{
    string oyuncu;
    int bakiye;
    int bahismiktar;
    int tahmin;
    int tek;
    int zar;
    char tercih;
    srand(time(0));

    cout << "\n\t\t================================================CASINO DÜNYASINA HOŞ GELDİNİZ================================================\n\n";
    rules();
    cout << "\n\nİsminiz Nedir Efendim? ";
    getline(cin, oyuncu);
    cout << "\n\n Oyun oynamak için başlangiç bakiyesini girin: ";
    cin >> bakiye;

    do {

        system("clear");
        cout << "\n\nGeçerli Bakiyeniz: " << bakiye << "$" << "\n";

        do {

            cout << "Hey, " << oyuncu <<  " bahis miktari giriniz: ";
            cin >> bahismiktar;
        
            if(bahismiktar > bakiye)
            cout << "Bahis bakiyesi mevcut bakiyeden daha fazla olamaz!\n" << " Tekrar bakiyenizi giriniz\n ";
        
        }while(bahismiktar > bakiye);

        do{

            cout << "1 ile 10 arasindaki bahis sayisini tahmin et: ";
            cin >> tahmin;
            if(tahmin <= 0 || tahmin > 10)
            cout << "\nSayi 1 ile 10 arasinda olmalidir.\n" << "Tekrar sayiyi giriniz.\n";

        }while(tahmin <= 0 || tahmin >10);
        
        zar = rand()%10 +1;
        if(zar == tahmin){

            cout << "Şanslisin!! kazandin. " << "$" << bahismiktar * 10;
            bakiye = bakiye + bahismiktar * 10;
        }
        else{
        
            cout << "Ups, bir dahaki sefere daha iyi şanslar! " << bahismiktar << "Tl kaybettiniz" << "\n";
            bakiye = bakiye - bahismiktar;
        }
        cout << "\n Kazanan para: " << zar << "\n";
        cout << "\n" << oyuncu << " Senin bakiyen " << bakiye << "$" << "\n";

        if(bakiye == 0)
        {
            cout << "Senin bakiyen bitti tekrar oynayiniz! ";
            break;
        }
        cout << "\n\n->Tekrar oynamak istiyor musunuz (Y/n)? ";
        cin >> tercih;

    }while(tercih == 'Y' || tercih == 'y');
    
    cout << "\n\n";
    cout << "\n\nTeşekkürler oynadiğinz için. Bakiyeniz " << bakiye << " $" << "\n\n";
    while(tercih == 'n' || tercih == 'N');
 
    return 0;
}
void rules(){
    system("clear");
    cout << "\t\t========================KUMARHANE SAYI TAHMİN KURALLARI!========================\n";
    cout << "\t1. 1 ile 10 arasinda sayi seçiniz\n";
    cout << "\t2. Kazanan bahsin 10 katini alir(1 dolar 10 tl :))\n\n";
}
