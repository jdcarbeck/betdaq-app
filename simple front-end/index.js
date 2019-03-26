var http = require('http');
var fs = require('fs');

//create a server object:
var server = http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  var myReadStream = fs.createReadStream('index.html', 'utf8');
  myReadStream.pipe(res);
}); //the server object listens on port 8080


server.listen(3000, '127.0.0.1');
