function topla(x, y) {
    return x + y;
}
function topla2(x, y) {
    return x + y;
}
var topla3 = function (x, y) {
    return x + y;
};
function topla4(x, y) {
    if (y === void 0) { y = 4; }
    return x + y;
}
function topla5(x, y) {
    if (y) {
        return x + y;
    }
    return x;
}
// console.log(topla(2,4))
// console.log(topla('ankara', 2))
// console.log(topla2(2,4))
// console.log(topla3(2,4))
// console.log(topla4(3))
// console.log(topla5(3))
// console.log(topla5(3,2))
function davetEt(ilkDavetli) {
    var digerleri = [];
    for (var _i = 1; _i < arguments.length; _i++) {
        digerleri[_i - 1] = arguments[_i];
    }
    return ilkDavetli + " " + digerleri.join(" ");
}
console.log(davetEt('burak', 'murat', 'kurak'));
function davetEtt() {
    var digerleri = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        digerleri[_i] = arguments[_i];
    }
    return digerleri.join(" ");
}
console.log(davetEt('MEHMET', 'AMED'));
