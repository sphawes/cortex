var path = require('path');
var express = require('express');

var app = express();

app.use(express.static(path.join(__dirname, '/public')));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/public/index.html'));
})

app.listen(8081, function() {
  console.log('Cortex server running on port 8081!');
})
