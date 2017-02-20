var path = require('path');

var express = require('express');
var app = express();

//var main = require('main');


app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
})

app.get("/action", function(req, res){
	console.log(req.query)
	try{
	    state = req.query.state
	    if (state == "doorToggle") {
      		result = execSync("python action.py doorToggle")
      		console.log(result.toString())
	    }
	}
  catch(e){
	    res.status(500).send(e)
	}

});

app.listen(8081, function () {
  console.log('Cortex server running on port 8081!');
})
