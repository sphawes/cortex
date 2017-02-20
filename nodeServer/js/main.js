alert("test");




$(document).ready(function(){
    $("#frontDoorButton").click(function(){
        $.get("../scripts/action.py", {"action": "doorToggle"})
    });
})
