var http = require('http')
var log = require('./log.js')
var SayHello = require('./exportDemo.js')

//http://localhost:8080/
http.createServer(function(request, response) {
    // response.writeHead(200, {'Content-Type': 'text/html'})
    
    if(request.url == "/admin") {
        response.writeHead(200, {'Content-Type': 'text/html'})
        response.write('<html><body><strong>Admin</strong></body></html>')
    } 
    
    else if (request.url == "/" ) {
        response.writeHead(200, {'Content-Type': 'text/html'})
        response.write("<html><body><strong>Anasayfa</strong></body></html>")
    } 
    
    else if (request.url == "/customer") {
        
        response.writeHead(200, {'Content-Type': 'application/json'})
        response.write(JSON.stringify({name: 'Buvak', lastName: 'Yabgu'}))
    } 
    
    
    response.end(' Sayfasonu')
}).listen(8080)


log.information('sunucu yayına geçti')

console.log(SayHello())






