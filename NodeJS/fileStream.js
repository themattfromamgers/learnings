var fs = require('fs')

//DOSYAYI OKUR
fs.readFile("dosya.txt", function(hata, data) {
    if(hata) {
        throw hata;
    }
    console.log(data)
});

//DOSYAYA YAZAR
fs.writeFile("dosya2.txt", "he", function(hata, data) {
    if(hata) {
        throw hata;
    }
    console.log(data)
});

//DOSYAYININ ÜSTÜNE EKLER
fs.appendFile("dosya2.txt", "anan", function(hata, data) {
    if(hata) {
        throw hata;
    }
    console.log("eklendi")
});

// DOSYAYI SİLER
fs.unlink("dosya2.txt", function(hata, data) {
    if(hata) {
        throw hata;
    }
    console.log("silindi")
});


