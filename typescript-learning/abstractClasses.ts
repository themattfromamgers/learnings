abstract class KrediBase{
    constructor(){

    }
    kaydet():void{
        console.log("saved")
    }

    abstract hesapla():void;
}

class TuketiciKredi extends KrediBase{
    constructor(params) {
        super()
    }

    hesapla(): void {
        console.log('tüketici kredisi alındı')
    }
}

class MortgageKredi extends KrediBase{
    constructor(params){
        super()
    }

    hesapla(): void {
        console.log('konut kredisi hesap yapıldı')
    }
}

let tk = new TuketiciKredi()
tk.hesapla();
tk.kaydet()

let mk = new MortgageKredi()
mk.hesapla()
mk.kaydet()