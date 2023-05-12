// var diziler = [function selam() {
//     console.log("xd")
// }]

// diziler[0]()

// var sehirler = ["ankara", "istanbul", "izmir", "adana"];
// console.log(sehirler.pop());

// console.log(sehirler)
// console.log(sehirler.length)
// console.log(sehirler.shift())
// console.log(sehirler.push('izmir'))
// console.log(sehirler.concat(["Balıkesir", "Denizli"]))
// // console.log(sehirler.sort())
// console.log(sehirler)

// var sehirler = ['Ankara', 'İstanbul', 'İzmir']
// for(i =0; i < sehirler.length; i++) {
//     console.log(sehirler[i])
// }

// var i = 1;
// while (i<=10) {
//     console.log(i)
//     i++
// }

// var i = 1;
// do {
//     console.log(i);
//     i++

// } while (i <=10)

// sehirler.forEach(function(sehir) {
//     console.log(sehir)
// })

// document.getElementById('xd').innerHTML = "buvk"

// var result = document
//   .getElementById("nesne")
//   .addEventListener("click", mudahale);

// function mudahale() {
//   document.getElementById("nesne").innerHTML = "KOPYALANDI";
//     alert("kopyalyamazsın")
// }

// var result = document.getElementsByTagName("body", mudahale)



// var baslik = document.createElement("h2");
// var node = document.createTextNode("merhaba java")
// baslik.appendChild(node)

// var div1 = document.getElementById('div1')
// var p2 = document.getElementById('p2')
// div1.insertBefore(baslik, p2)

// alert()
// div1.removeChild(p2)

// div1.replaceChild(baslik, p2)


//EPSIDE
// const myarray = [1,2,3,4]
// const kd = []
// myarray.forEach(sayi=>{
//     kd.push(sayi*sayi)
// })
// console.log(kd)






// const myarray = [1,2,3,4]
// const kd = myarray.map(sayi=> sayi*3)
// console.log(kd)



// const myarray = [1,2,3,4]
// const fd = myarray.filter(sayi=>sayi>2)
// console.log(fd)


// const myarray = [1,2,3,4]
// const belirleme = 0;
// const toplam = myarray.reduce((acc, sayi)=>{
//     return acc + sayi;
// }, belirleme)

// console.log(toplam)

// const us = {
//     ekle: function(){
//         console.log(this)
//     }
// }

// us.ekle()



class person{

    constructor(ad, soyad) {
        this.ad=ad
        this.soyad=soyad
    }

    kaydet(){
        console.log('perosnel kaydedili'+this.ad)
    }
}

const per = new person("bur", "ak")

per.kaydet()
console.log(per.ad)

