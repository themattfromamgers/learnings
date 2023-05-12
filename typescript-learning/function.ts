function topla(x,y){
    return x+y
}

function topla2(x:number, y: number):number{
    return x+y
}

let topla3 = function(x:number,y:number):number{
    return x+y;
}

function topla4(x:number,y:number=4):number{
    return x+y
}

function topla5(x:number, y?:number):number{
    if(y){
        return x+y
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
function davetEt(ilkDavetli:string, ...digerleri:string[]):string{
    return ilkDavetli + " " + digerleri.join(" ")
}

console.log(davetEt('burak', 'murat', 'kurak'))


function davetEtt(...digerleri:string[]):string{
    return digerleri.join(" ")
}

console.log(davetEt('MEHMET', 'AMED'))


