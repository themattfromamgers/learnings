import 'dart:io';

void main(){

  // String miyav = "a";

  // int dogumY = 1985;
  // double oran = 1.15;
  // bool loginmi = false;

  // print("Hello World $miyav");
  // print("Dy: "+ dogumY.toString());
  // print("oran: "+ oran.toString());

  // var sistemeGirmisMi = false;
  
  // if(sistemeGirmisMi == true) {
  //   print("girdi");
  // } 
  // // else if(sistemeGirmisMi == null) {
  // //   print("hiç bişi yok")
  // // }
  // else {
  //   print("girmedi");
  // }

  // String not = "A";
  // switch(not) {

  //   case "A": {
  //     print("Süper");
  //   }
  // break;
  //   case "B": {
  //     print("İyi");
  //   }
  // break;
  //   case "C": {
  //     print("İdare der");
  //   }
  // break;
  //   case "D": {
  //     print("Kötü");
  //   }
  //   break;
    
  //   default: {
  //     print("Bilinmiyor");
  //   }
  //   break;
  // }



  print("Adınızı giriniz: ");
  String? isim = stdin.readLineSync();

  print("Yaşınızı giriniz: ");
  int? yas = int.parse(stdin.readLineSync()!);
  print("Girilen isim : $isim ve yaşınız : $yas");

}