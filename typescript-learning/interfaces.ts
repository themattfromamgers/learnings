interface Product{
    id: number;
    name: string;
    unitPrice: number;

}

// function saves(product: Product){
//     console.log(product.name)
// }

// saves({id:1, name:"xd", 'laptop'})


let sehirler= ['angara', 'istanbul']

for(let i in sehirler){
    console.log(i)
}

for(let i of sehirler){
    console.log(i)
}