class Ev{


    private odaSayisi: number;
    protected xd: string;
    pencereSayisi: number;
    kat: number;
    constructor(odaSayisi:number, pencereSayisi:number, kat:number){
        this.odaSayisi = odaSayisi;
        this.kat = kat;
        this.pencereSayisi = pencereSayisi;
    }
    yemekYe(){
        console.log(this.odaSayisi, this.kat)
    }
}

let ev = new Ev(3,4,5)
ev.yemekYe()
console.log(ev.kat)

//Inharetince

class User{
    private _isim: string
    get isim():string{
        return "sayın: "+this._isim;
    }
    set isim(ad:string){
        this._isim = ad
    }
    kaydet(){
        console.log('user saved')
    }
}
class Customer extends User {
    doBuy(){

        console.log('satı yapıldı')
    }
}
class Person extends User{
    massOde(){
        console.log('maas odendi')
    }
}

let customerOne = new Customer()
customerOne.isim = 'BUVAK'
console.log(customerOne.isim)
customerOne.kaydet()
customerOne.doBuy()

let pe1 = new Person()
pe1.kaydet()
pe1.massOde()


let cust = new Customer()
cust.isim = 'xd'
console.log(cust.isim)
cust.kaydet()
cust.doBuy()
