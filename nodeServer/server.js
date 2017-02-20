var path = require('path');
var express = require('express');
var app = express();

app.use(express.static('js'));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
})

app.get('')

app.listen(8081, function() {
  console.log('Cortex server running on port 8081!');
})
