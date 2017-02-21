function doOnWindowLoad(){
  var d = new Date();
  document.getElementById("date").innerHTML = d.toDateString();

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
