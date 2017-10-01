$(function() {

    // Short hack used to override tooltip visibility
    var $search_bar = $("#search_bar");
    $search_bar.click(function() {
       $("#search_tooltip").hide();
    });
    $search_bar.hover(function() {
        $("#search_tooltip").show();
    });

    // Logout functionality
    $("#logout").click(function() {
        window.location.replace("../login/login.html");
    });

    var $map = $("#map");
    $("#exam1").click(function() {
        $map.attr('src', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1808.8181315005165!2d28.02693465976231!3d-26.1895885222041!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x6671644b3bdae45!2sOld+Mutual+Sports+Hall!5e0!3m2!1sen!2sza!4v1506721698302");
    });

    $("#exam2").click(function() {
        $map.attr('src', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1808.8181315005165!2d28.02693465976231!3d-26.1895885222041!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1e950c0ee2398e57%3A0x2630df9829b9d6b8!2sFirst+National+Bank+Building%2C+1+Jan+Smuts+Ave%2C+Braamfontein+Werf%2C+Johannesburg%2C+2000!5e0!3m2!1sen!2sza!4v1506721454429");
    });


    $map.attr('src', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1808.8181315005165!2d28.02693465976231!3d-26.1895885222041!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x6671644b3bdae45!2sOld+Mutual+Sports+Hall!5e0!3m2!1sen!2sza!4v1506721698302");

});