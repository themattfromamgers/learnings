// console.warn("xd")

// console.table(["vue", "html", "react", "java"]) // tablo

// console.clear()
    // Console temizler


// var he = "r";

/*   */

//TO LEARNİNG
/* 

Math.ceil()
Math.floor()
Math.round()
parseInt()
parseFloat()

Boolean
typeof()
length()

new Date().getHours()
slice()
replace()
includes()
startsWith()
endsWith()

document.location.pathname
document.location.hostname
document.location.host
document.baseURI
document.URL

document.body.style.backgroundColor = "red"
document.body
document.head

document.querySelector()
classList.add()

document.createElement()
prepend()
prompt()

*/


// console.log(Math.ceil(3.1)) // yukarı yuvarlama
// console.log(Math.floor(3.1)) // aşağı yuvarlama
// console.log(Math.round(3.1)) // yakına yuvarlama


// console.log(Boolean("a"=="b"))
// var deneme = Boolean(0)
// console.log(deneme)

// user = "he"
// console.log(Boolean(user.length < 1))


// const b = "0"; 
// console.log(Boolean(b))

// TİP  ÖĞRENME: typeof()
// let d1 = 5;
// let d2 = false;
// let d3 = 'he';
// let d4 = 122.250;
// console.log(typeof(he))

// let n1 = "he";
// console.log("nuımber", parseInt(n1))



// let n2 = 55;

// console.log(n2, typeof(n2))
// n2 = n2.toString()

// console.log(n2, typeof(n2))

// 2

// let ad = "burak";
// let soyad = "akın";

// console.log(`uzunluk: ${ad.length}`)
// console.log(`uzunluk: ${soyad.length}`)

// --3--

// console.log(`saat: ${new Date().getHours()}`)




//4
// console.log(`toplama ${4+5}`)

//5

// var fistname = "buvak";
// console.log(fistname[0]);
// console.log(fistname.charAt(0));

//6
// var fistname = "Buvak";
// console.log(fistname.toUpperCase());
// console.log(fistname.toLowerCase());

//7
// var fistname = "Buvak";
// var f = fistname.search("v");
// if (fistname[f] == "v") {
//     console.log(`${fistname[f]} harfi, ${f} satırda bulundu.`)
// } 
// else {
//     console.log("v bulunamadı")
// }


//8
// var email = "burakyabgu@gmail.com";
// let DOMIN = email.slice(email.search("@") + 1)

// console.log(DOMIN)

//9

// var mail = "Buvak@gmail.com";
// mail = mail.replace('gmail.com', 'yabgu.com')

// console.log(mail)

//10
// var mail = "Buvak@gmail.com";
// var a = mail.includes("@");
// console.log(a)



//11
// var mail = "Buvak@gmail.com";

// var email = mail.startsWith("B");
// var email2 = mail.endsWith("@hotmail.com");



// if (email == true && email2 == true) {
//     console.log("ikisi doğru")
// }
// else if (email == true) {
//     console.log("b ile başlıyoır")

// }
// else if (email2 == true) {
//     console.log("gmail ile bitiyor")

// }
// else {
//     console.log("hepsi  yanlış")
// }

//12 


// console.log(document.location.pathname)
// console.log(document.location.hostname)
// console.log(document.location.host)
// console.log(document.body)
// console.log(document.head)

// console.log(document.body.style.backgroundColor = "red")

// console.log(document.URL)
// console.log(document.baseURI)


//13
// let title = document.getElementById('title')
// console.log(title.innerHTML="BUVAKL")

// let link = document.querySelector('#kodluyoruz')

// link.innerHTML = "link bilgisi"
// link.style.color = "red"
// link.classList.add('btn') 



// console.log(link)

// 14


// let firstName = prompt('firstName: ')
// let lastName = prompt('lastName: ')
// let greeting = document.querySelector('#gretting')
// greeting.innerHTML = `${greeting.innerHTML}<small style="color: red;">${firstName}</small>`

//15

// let item = document.querySelector('ul#list>li:last-child')

// let ulDOM = document.querySelector("ul#list")
// let liDOM = document.createElement('li')

// liDOM.innerHTML = "Kendi Olusturdugumuz Oge"
// ulDOM.append(liDOM) // en sona ekler
// ulDOM.prepend(liDOM)


//16

//let gretting = document.querySelector('#gretting')

//gretting.classList.add("text-primary")
//gretting.classList.add("title")
//gretting.classList.add("new-info", "second-class")

//gretting.classList.remove("text-primary")
//gretting.classList.remove("text-primary", "new-info")


//console.log(gretting.classList)


//17

// let price = "100"
// console.log("==")
// console.log(price==1)
// console.log(price==100)

// console.log("===")
// console.log(price===100)
// console.log(price==="100")

// console.log("!=")
//false
// console.log(price !=100)
//true 
// console.log(price !=1)

/*
&& = AND-VE
|| = OR-VEYA
*/

// DEĞİL
// console.log("!")
// console.log(!price == "100")
// console.log(!price == "102")


//18

// if 
// if else
// else

//19

//SWİTCH-CASE

// var ifade = "java"

// switch(ifade) {
//     case "java":
//         console.log("java nesne tabanlı bir dildir.")
//     break;

//     case "python":
//         console.log("python bir yorumlama dilidir")
//     break;

//     case "c":
//         console.log("c bir dildir")
//     break;

//     default:
// }


//20

// var money = 16;

// var canBuy = 
// (money > 30) ? "Satın Alablrisin":
// (money < 17) ? "Satın Alamazsın":
// "para miktarını girmen gerekmektedir";

// console.log(canBuy)

//21

// var money;
// var canBuy = 
//     (money < 17) ? "Satın alamazsın..":
//     (money > 30) ? "Satın alabilirsin..":
//     "Para miktarını girmen gerekmektedir..";

// console.log(canBuy)

//22

// function helloo() {
//     console.log("merhaba")
// }

//fonksiyonu çağırdık
// helloo()

// function printHello(name){               
//     console.log("hello" + name);  	
// }
// printHello("reis");


//>

// function print() {
//     hello()
// }

// function hello() {
//     console.log("Hello Func")
// }

// let first = "Lorem"

// function gretting(first) {
//     console.log(`Merhaba ${first ? first : "Kullanıcı"}`)
// }

// gretting("Merhabalar")

// function gretting(first="") {
//     console.log(`merhaba ${first}`)
// }

// gretting("merhaba")
// gretting()

//>

// function gretting2(firstName, lastName) {
//     let info = `Merhaba ${firstName} ${lastName}`
//     return info
// }

// let info = gretting2("ad", "soyad")
// console.log(info)

// function domId(id, info) {
//     let dom = document.querySelector(`#${id}`)
//     dom.innerHTML = info
// }

// domId('greeting', 'merhaba')
// domId('greeting', gretting2("ad", "soyad"))

// let html = `<span style="color:red;">color red</span>`

// domId('greeting', html)

//23

//fat arrow func

// const helloFunc = (firstName) => {
//     console.log(`Hi ${firstName}`)
// }
//     helloFunc("he")



// const helloFuncc = firstName => console.log(`Hi ${firstName}`)
// helloFuncc("hea")



// const helloWorldV3 = (firstName, lastName) => {
//     console.log(`Hi ${firstName} ${lastName}`)
// }

// helloWorldV3("burak", "soy")

// const helloV4 = (firstName, lastName) => {
//     let info = `Hi ${firstName} ${lastName}`
//     console.log(info)
//     return info
// }

// helloV4("burak", "yabgu")


//24

// click
// let greeting = document.querySelector('#greeting')
// greeting.addEventListener('click', domClick)

//mouseover
// let greeting = document.querySelector('#greeting')
// greeting.addEventListener('mouseover', domClick)



// function domClick() {

    // console.log("tik")
    // console.log(this)
    // console.log(this.innerHTML)
    // console.log(this.innerHTML = "Bilgi değitşi")
    // console.log(this.style.color = "red")
        
    // this.style.color == "red" ? this.style.color = "black" : this.style.color = "red"
    // }


//25
// localStorage.setItem("name", "burak")

// let getName = localStorage.getItem("name")
// console.log(getName)
// localStorage.removeItem("name");

//26

// let user = {userName: 'kodluyoruz', isActive: true}

// localStorage.setItem('UserINFO', JSON.stringify(user))

// let userInfo = localStorage.getItem('UserINFO')
// console.log(userInfo)

// console.log(JSON.parse(userInfo))

//27

// let counter = localStorage.getItem('counter') ? Number(localStorage.getItem('counter')) : 0
// let counterDOM = document.querySelector('#counter')
// let increaseDOM = document.querySelector('#increase')
// let decreaseDOM = document.querySelector('#decrease')

// counterDOM.innerHTML = counter

// increaseDOM.addEventListener("click", clickEvent)
// decreaseDOM.addEventListener("click", clickEvent)

// function clickEvent() {
//     this.id == "increase" ?  counter += 1 : counter -= 1
//     localStorage.setItem('counter', counter)
//     counterDOM.innerHTML = counter
// }

// localStorage.clear()

// sessionStorage.setItem("name", "burak")
// window.alert("he")

//28

// let dom = document.querySelector('#userdom')
// dom.addEventListener('submit', formSub)

// function formSub(event) {
//     event.preventDefault()
//     console.log("tamam")
// }

// let scoreDom = document.querySelector('#score')
// console.log(scoreDom.value)
// localStorage.setItem('score', scoreDom.value)

//29
// let d = "kod"
// let f = false
// let items = [1,2,3,4, d, f]
// console.log(items)
// console.log(items.length)
// console.log(items[4])
// console.log(items[items.length - 1])

// console.log(items)
// console.log(items.unshift(62))
// console.log(items)
// console.log(items.shift(31))
// console.log(items)

// items[0] = "anan" 
// console.log(items)

//30


// for(var i = 1; i < 5; i++) {
//     console.log(i);
// };


const my_Arrays = ["john", "walker", "Anakin", "Skywalker"]

// const userListDom = document.querySelector('#userList')

// for (index = 0; index < my_Arrays.length; index++) {
//     const liDom = document.createElement('li')
//     liDom.innerHTML = my_Arrays[index]
//     userListDom.appendChild(liDom)
// }

//31

// for(let counter = 0; counter < 10; counter++) {
//     console.log(counter)
//     if (counter ===5) {break}
//     console.log(counter)
// }

// for(let counter = 0; counter < 10; counter++) {
//     console.log(counter)
//     if (counter ===5) {continue}
//     console.log(counter)
// }

// const ulDom = document.querySelector('#userList')

// let index = 0

// for(; index < my_Arrays.length; index++) {
//     if(my_Arrays[index] == 'Anakin') {break}
//     let lid  = document.createElement('li')
//     lid.innerHTML = my_Arrays[index]
//     ulDom.append(lid)
// }

// for(; index < my_Arrays.length; index++) {
//     if(my_Arrays[index] == 'Anakin') {continue}
//     let lid  = document.createElement('li')
//     lid.innerHTML = my_Arrays[index]
//     ulDom.append(lid)
// }

//32

// let counter = 0
// while (counter < 10) {
//     console.log(counter)
//     counter++
// }

//33

// const animals = ["cat" , "dog" , "bird", "horse"];
// animals.forEach( animal => console.log( animal ) );


//34

// try {
//     let pro;
//     pro = promptt("Enter your name")
// } catch (error) {
//     console.log("error: ", error)
// }

//35

// let arrayOBJ = [1,2,3]
// let object1 = {obj: 1}

// let item1 = new Object()
// let item2 = {}
// console.log(typeof(item1))
// console.log(typeof(item2))

// let item3 = {}
// let item4 = new Object()


// console.log(object1)

//36

// let laptop = {
//     brand: "apple",
//     model: "macbook",
//     "2kg": 2,
//     modelName: "macbook pro",
//     model_Name: "macbook pro"
// }

// console.log(laptop)
// console.log(laptop.brand)
// console.log(laptop.model)
// console.log(laptop["2kg"])

// laptop.brand = "Mac"
// console.log(laptop)
// laptop["2kg"] = "31kg"
// console.log(laptop)

// keys = Object.keys(laptop)
// console.log(keys)
// console.log(Object.keys(laptop))

// keys.forEach(item => {
//     console.log(item)
//     console.log(laptop[item])
// })

// console.log(
//     Object.values(laptop)
// )

//37

// let user1 = {
//     firstName: "Burak",
//     lastName: "Yabgu",
//     age: 21,
//     score: [1,2,3,4,5],
//     isActive: true,
//     shortName: function() {return `${this.firstName[0].toLowerCase()} ${this.lastName[0].toLowerCase()}`}

// }

// console.log(user1)

//38

// var birey = {
// 	isim: 'Ali',
// 	soyisim: 'Veli',
// 	dogumYili: 1989,
// 	merhabaDe: (age) = `Merhaba, ben ${birey.isim} ${birey.soyisim}, ${age} yaşındayım`,
// };
// birey.yasHesapla = function () {
// 	return 2021 - this.dogumYili;
// };
// console.log(birey.merhabaDe(birey.yasHesapla()));

//38-2

// let set = {
//     userName : "lorem",
//     password : "Bad",
//     isActive: false,
//     ip: "local",
//     serverName: "kod"

// }

// let {userName: user, password, isActive, ip:ServerIP, serverName} = set


// console.log(set)


// try {
//     Block of code to try
//   }
//   catch(err) {
//     Block of code to handle errors
//   }
//   finally {
//     Block of code to be executed regardless of the try / catch result
//   }

