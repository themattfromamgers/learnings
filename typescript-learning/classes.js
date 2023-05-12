var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Ev = /** @class */ (function () {
    function Ev(odaSayisi, pencereSayisi, kat) {
        this.odaSayisi = odaSayisi;
        this.kat = kat;
        this.pencereSayisi = pencereSayisi;
    }
    Ev.prototype.yemekYe = function () {
        console.log(this.odaSayisi, this.kat);
    };
    return Ev;
}());
var ev = new Ev(3, 4, 5);
ev.yemekYe();
console.log(ev.kat);
//Inharetince
var User = /** @class */ (function () {
    function User() {
    }
    Object.defineProperty(User.prototype, "isim", {
        get: function () {
            return "sayın: " + this._isim;
        },
        set: function (ad) {
            this._isim = ad;
        },
        enumerable: false,
        configurable: true
    });
    User.prototype.kaydet = function () {
        console.log('user saved');
    };
    return User;
}());
var Customer = /** @class */ (function (_super) {
    __extends(Customer, _super);
    function Customer() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Customer.prototype.doBuy = function () {
        console.log('satı yapıldı');
    };
    return Customer;
}(User));
var Person = /** @class */ (function (_super) {
    __extends(Person, _super);
    function Person() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Person.prototype.massOde = function () {
        console.log('maas odendi');
    };
    return Person;
}(User));
var customerOne = new Customer();
customerOne.isim = 'BUVAK';
console.log(customerOne.isim);
customerOne.kaydet();
customerOne.doBuy();
var pe1 = new Person();
pe1.kaydet();
pe1.massOde();
var cust = new Customer();
cust.isim = 'xd';
console.log(cust.isim);
cust.kaydet();
cust.doBuy();
