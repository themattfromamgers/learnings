function selamVer(isim:string){
    return "Merhaba "+isim
}

let mesaj = selamVer('Engin')
console.log(mesaj)

let sayi:number

sayi=10
sayi = 10.4
console.log(sayi)

let sehir : string
sehir="Ankara"
sehir="İstanbul"
let sehirler : string="adana"
console.log(sehir)

let dogruMu : boolean
dogruMu = false
console.log(dogruMu)

let sayilar: number[]=[1,2,3,4]
let sayilar2: Array<number>= [1,2,3,5]
console.log(sayilar)
console.log(sayilar2)

let sehirlers: string[] = ['ADANA', 'ISTANBIL', 'MİYAVETTİNPASA KONAĞI']
console.log(sehirlers) 

let dizi : [number, string] = [31, 'xd']
console.log(dizi)

enum Renk {Kirmizi=1, siyah, mavi}
let renk: Renk = Renk.siyah

let deger : any = 'ankara'
deger = 2
deger = {}

let deger2 : void = undefined

function selam2():void{
    console.log('merhaba')
}

let yas:number;


