function doOnWindowLoad(){
  var d = new Date();
  document.getElementById("date").innerHTML = d.toDateString();

  $.getJSON('http://iobridge.com/api/feed/key=waStTNuoEvld6t9wsM&callback=\?', function(response){

       var value = response.module.channels[0].AnalogInput;
       if(value > 500){
         $('#HackPGH').removeClass('btn-danger');
         $('#HackPGH').addClass('btn-success');
       }
       else{
         $('#HackPGH').removeClass('btn-success');
         $('#HackPGH').addClass('btn-danger');
       }
  })

}
window.onload = doOnWindowLoad;

$(document).ready(function(){
    $("#frontDoorButton").click(function(){

        $.get("/toggle", {"state": "on"})

    });

    $("#HackPGH").click(function(){
        $.get("/toggle", {"state": "off"})
    })

})
