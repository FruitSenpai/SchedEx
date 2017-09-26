$(function() {

    // Short hack used to override tooltip visibility
    var $search_bar = $("#search_bar");
    $search_bar.click(function(e) {
       $("#search_tooltip").hide();
    });
    $search_bar.hover(function(e) {
        $("#search_tooltip").show();
    });

    // Logout functionality
    $("#logout").click(function(e) {
        window.location.replace("../home/home.html");
    })

});