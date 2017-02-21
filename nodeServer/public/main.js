function doOnWindowLoad(){
  var d = new Date();
  document.getElementById("date").innerHTML = d.toDateString();

  $.getJSON('http://iobridge.com/api/feed/key=waStTNuoEvld6t9wsM&callback=\?', function(response){

       alert(response);
       
       alert(response.module.channels[0].AnalogInput);
  })

}
window.onload = doOnWindowLoad;

$(document).ready(function(){
    $("#frontDoorButton").click(function(){

        $.get("/LEDSwitch", {"state": "on"})

    });

    $("#HackPGH").click(function(){
        $.get("/LEDSwitch", {"state": "off"})
    })

})
