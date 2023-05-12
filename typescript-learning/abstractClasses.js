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
var KrediBase = /** @class */ (function () {
    function KrediBase() {
    }
    KrediBase.prototype.kaydet = function () {
        console.log("saved");
    };
    return KrediBase;
}());
var TuketiciKredi = /** @class */ (function (_super) {
    __extends(TuketiciKredi, _super);
    function TuketiciKredi(params) {
        return _super.call(this) || this;
    }
    TuketiciKredi.prototype.hesapla = function () {
        console.log('tüketici kredisi alındı');
    };
    return TuketiciKredi;
}(KrediBase));
var MortgageKredi = /** @class */ (function (_super) {
    __extends(MortgageKredi, _super);
    function MortgageKredi(params) {
        return _super.call(this) || this;
    }
    MortgageKredi.prototype.hesapla = function () {
        console.log('konut kredisi hesap yapıldı');
    };
    return MortgageKredi;
}(KrediBase));
var tk = new TuketiciKredi();
tk.hesapla();
tk.kaydet();
var mk = new MortgageKredi();
mk.hesapla();
mk.kaydet();
