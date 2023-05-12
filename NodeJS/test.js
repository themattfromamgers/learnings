var http = require('http')


http.createServer(function(req, res){
	
	res.write("<h1 style='color: red;'>HELLO</h1>")
	
}).listen(8080)

console.log("run")
