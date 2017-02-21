var path = require('path');
var express = require('express');
var execSync = require("child_process").execSync;
var app = express();

app.use(express.static(path.join(__dirname, '/public')));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
})

app.get("/LEDSwitch", function(req, res){
	console.log(req.query)
	try{

      LED = req.query.state

      if (LED == "on") {
		      result = execSync("sudo python ~/cortex/scripts/action.py on")
		      console.log(result.toString())
	    }
      else {
		      result = execSync("sudo python ~/cortex/scripts/action.py off")
		      console.log(result.toString())
	    }


	}
  catch(e){
	    res.status(500).send(e)
	}


});

app.listen(8081, function() {
  console.log('Cortex server running on port 8081!');
})
