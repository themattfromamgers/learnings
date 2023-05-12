//W3.SCHOOLS
var Eroors;
(function (Eroors) {
    Eroors[Eroors["buvak"] = 31] = "buvak";
    Eroors[Eroors["anil"] = 31] = "anil";
    Eroors[Eroors["yamur"] = 62] = "yamur";
    Eroors[Eroors["sila"] = 62] = "sila";
})(Eroors || (Eroors = {}));
console.log(Eroors);
console.log(Eroors.anil);
// const car: { type: string, model: string, year: number } = {
//     type: "Toyota",
//     model: "Corolla",
//     year: 2009
// };
// console.log(car)
//BAŞKA
// main  .ts
// export class Yabgu {
//     constructor(
//      public firstName: string,
//      public lastName: string,
//      public age: number
//     ) {
//     }
//  }
// ---HERE--
// import { Yabgu} from './main';
// const a = new Yabgu();
// a.firstName = '5';
// console.log(`${a.firstName}`)
// let yazi : string;
// let sayi : number;
// let tf: boolean;
// yazi = "he";
// sayi = 31;
// tf = false;
// console.log(yazi, sayi, tf);
//2
// let langs : string[];
// let numbers : number[];
// let BoolV : boolean[];
// let BoolVal : Array<boolean>[];
// let a : Array<number> = [1,2,3,4,5,6];
// langs = ["php", "java", "python"];
// numbers = [1,2,3,4,5];
// BoolV = [true, false, true];
// BoolVal = [true, false, true];
// console.log(...langs);
// console.log(...numbers);
// console.log(...BoolV);
// console.log(...BoolVal);
// console.log(...a);
//3
// function topla(x:number, y:number) {
//     console.log(x+y)
// }
// topla(1,3)
// function addNumbers(num1:number, num2:number) : number {
//     return num1 + num2;
// }
// console.log(addNumbers(1,2));
// function addNumbers(num1:number, num2:number) : number {
//     return num1 + num2;
// }
// console.log(addNumbers(1,2));
// function addNumbers(num1:number, num2:number = 200) : number {
//     return num1 + num2;
// }
// console.log(addNumbers(1,2));
// console.log(addNumbers(10,20));
//VOİD return dönemez
// function addN(num1:number, num2:number) : void {
//     console.log(num1 + num2)
// }
// addN(10,20)
// class Person {
//     name: string;
//     age: number;
//     phone: string;
//     constructor(name: string, age: number, phone: string) {
//         this.name = name;
//         this.age = age;
//         this.phone = phone;
//         console.log("kişi oluşturuldu")
//     }
//     showInfo() {
//         console.log(`${this.name} ${this.age} ${this.phone}`)
//     }
// }
//     class Employee extends Person {
//         salary: number;
//         constructor(name: string, age: number, phone: string, salary: number) {
//             super(name, age, phone);
//             this.salary = salary;
//             console.log("person oluşturuldu")
//         }
//         changeDepartment() {
//             console.log("Depet değiştiriliyor")
// }
// let Employee1 = new Employee("Burak", 23, "0555555555", 4000);
// Employee1.showInfo();
// Employee1.changeDepartment();
// interface Idatabase {
//     add(); 
//     get();
//     delete();
//     update();
// }
// class MySql implements Idatabase {
//     add() {
//         console.log("mysql eklendi")
//     }
//     get() {
//         console.log("mysql getirildi")
//     }
//     delete() {
//         console.log("mysql silindi")
//     }
//     update() {
//         console.log("mysql güncellendi")
//     }
// }
// let mysql = new MySql();
// mysql.add();
// interface Idatabase {
//     add(); 
//     get();
//     delete();
//     update();
// }
// class MongoDb implements Idatabase{
//     add() {
//         console.log("MongoDb eklendi")
//     }
//     get() {
//         console.log("MongoDb getirildi")
//     }
//     delete() {
//         console.log("MongoDb silindi")
//     }
//     update() {
//         console.log("mysql güncellendi")
//     }
// }
// function add(db: Idatabase) {
//     db.add();
// }
// add(new MongoDb)
// EPİSODE 2 -sturan
// function greeter(name) {
//     console.log("Hello " + name);
// }
// let user = "Burak";
// greeter(user);
//2
// let b: string =  'a';
// let c: boolean = true;
// let d : any;
// let e : number[] = [1,2,3];
// let f : Array<number> = [1,2,3];
// let g : any[] = [1, 'a', true];
// let h: [string, number, boolean] = ['he', 1, true];
// const krediPay = 0;
// const havalaPay = 0;
// const eftPay = 0;
// enum Payment {krediPay=0, havalaPay=1, kapidaOdeme=2, eftPay=3};
// let kredi=Payment.krediPay;
// let havale=Payment.havalaPay;
// let kapidaOdeme=Payment.kapidaOdeme;
// let eft=Payment.eftPay;
//3
// let message;
// message = 'Hello World';
// let count = (<string>message).length;
// console.log("1. Yöntem: ", count)
// let length = (message as string).length;
// console.log("2. Yöntem: ", length)
//4
// function GetA(a: number, b:number,c?:number) {
//     const result = (a+b+c)/3;
//     return 'result: ' + result;
// }
// GetA(10,2);
//5
// interface Point {x: number, y: number}
// interface Passenger {
//     name: string;
//     phone: string;
// }
// interface Vehicle {
//     currentLocal: Point;
//     travel(point: Point): void;
//     getDis(pointA: Point, pointB: Point): number;
//     addPas(Passenger: Passenger): void;
//     removePas(Passenger: Passenger): void;
// }
// class Taxi implements Vehicle {
//     currentLocal: Point;
//     travel(point: Point): void {
//     }
// }
//EPİSODE 3 - didem
//1
// type Color = {
//     name: 'black' | 'white';
// };
// type user = {
//     name: string;
//     age: number | string;
//     role: 'admin' | 'user';
//     color: Color;
// };
// let newUser: user;
// newUser = {
//     name: "Burak",
//     age: 18,
//     role: "admin",
//     color: {
//         name: "black"
//     }
// }
//2
// const add = (num1: number, num2: number) => {
//     console.log(num1+num2);
// };
// add(2,3)
//3
// interface Person {
//     name: string;
//     age: number;    
// }
// interface Employee extends Person {
//     readonly empCode: number;
//     getSalary: ()=> number;
// }
// let newEmployee: Employee;
// newEmployee = {
//     name: "Buvak",
//     age: 22,
//     empCode: 222
// };
// console.log(newEmployee);
//5
// interface IEmploye {
//     name: "Buvak";
//     age: 22;
//     empCode: 222;
//     getSalary: (number)=> number;
// }
// class Employee implements IEmploye {
//     empCode: number;
//     name: string;
//     age: number;
// }
