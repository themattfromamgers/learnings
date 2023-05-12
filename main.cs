using System;

class Kisi {

    public string ad;
    public string soyad;
    public int yas;

    public void Yaz()
    {

    Console.WriteLine("İsim: {0}, Soyad {1}, Yaş {2}", this.ad,  this.soyad,  this.yas);
    }

}

class Program {
    static void Main (string[] args) {

    Kisi k1 = new Kisi();
    k1.ad = "Ahmet";
    k1.soyad = "miyav";
    k1.yas = 11;

    k1.Yaz();


    // int sayi1 = 3;
    // int sayi2 = 10;
    // int toplam = sayi1+sayi2;
    // Console.WriteLine(toplam);

    // Console.Read();
    }
}